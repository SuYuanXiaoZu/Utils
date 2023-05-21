import csv
import json
import os
from tqdm import trange
from datetime import datetime
import sys
from main import hex_a2b

dataDir = "dataset"
# hosts = ["99.999.9.10", "99.999.9.16", "99.999.9.19", "99.999.9.23", "99.999.9.27", "99.999.9.35"]
# hosts = ["10.1.0.25"]
date_format = "%a, %d %b %Y %H:%M:%S %Z"
frame_date_format = "%b %d, %Y %H:%M:%S.%f"

def slicePcap(dateRange, df):
    assert len(dateRange) == 2
    left_date = dateRange[0]
    right_date = dateRange[1]
    resultDf = []
    resultIP = set()
    trigger = False
    the_left = sys.maxsize
    the_right = 0
    for i in range(len(df)):
        try:
            data = df[i]
            ipSrc = data['_source']['layers']['ip']['ip.src']
            ipDst = data['_source']['layers']['ip']['ip.dst']
            source = data.get("_source")
            if source:
                layers = source.get("layers")
                if layers:
                    frame = layers.get("frame")
                    if frame:
                        tcp = layers.get("tcp")
                        date = frame.get("frame.time")
                        if tcp:
                            tcp_payload = tcp.get("tcp.payload")
                        if date and tcp and tcp_payload:
                            frame["frame.time"] = date = date.replace(" 中国标准时间", "")[:-3]
                            date = datetime.strptime(date, frame_date_format)
                            delta_left = (date - left_date).total_seconds()
                            delta_right = (right_date - date).total_seconds()
                            if delta_left > 0. and delta_right > 0.:
                                trigger = True
                                result = hex_a2b(tcp["tcp.payload"])
                                tcp["tcp.payload"] = result.decode("utf-8", errors='ignore')
                            else:
                                trigger = False

                            if date.timestamp() > the_right:
                                the_right = date.timestamp()
                            if date.timestamp() < the_left:
                                the_left = date.timestamp()

                            if trigger and tcp and tcp_payload and ipSrc == host:
                                resultDf.append(df[i])
                                resultIP.add(ipSrc)
                                resultIP.add(ipDst)

                        # http = layers.get("http")
                        # if http:
                        #     date = http.get("http.date")
                        #     if date:
                        #         date = datetime.strptime(date, date_format)
                        #         delta_left = (date - left_date).total_seconds()
                        #         delta_right = (right_date - date).total_seconds()
                        #         if delta_left > 0. and delta_right > 0.:
                        #             trigger = True
                        #         else:
                        #             trigger = False
                        #
                        #         if date.timestamp() > the_right:
                        #             the_right = date.timestamp()
                        #         if date.timestamp() < the_left:
                        #             the_left = date.timestamp()

            # if trigger:
            #     resultDf.append(df[i])
            #     resultIP.add(ipSrc)
            #     resultIP.add(ipDst)

            # endif
        except KeyError:  # no IP
            continue
    # endfor
    # the_left = datetime.fromtimestamp(the_left)
    # the_right = datetime.fromtimestamp(the_right)
    # print(f"\nLeft: {the_left.ctime()}\tRight: {the_right.ctime()}")
    return resultDf, resultIP


def read_json(path):
    with open(path, "r", encoding="utf8") as f:
        df = json.load(f)
        return df


def to_json(df, path):
    with open(path, "w", encoding="utf8") as f:
        json.dump(df, f, indent=4)


def get2Hop(dateRange, chunkNum=20):
    the_format = "%d %b %Y %H:%M:%S %Z"
    left_date = datetime.strptime(dateRange[0], the_format)
    right_date = datetime.strptime(dateRange[1], the_format)
    dateRange = [left_date, right_date]
    ips = set()
    for i in trange(chunkNum, desc="OneHop"):
        path = f"{dataDir}/xa{chr(ord('a') + i)}"
        # dataset = pd.read_json(path)
        dataset = read_json(path)
        df, ip = slicePcap(dateRange, dataset)
        dirName = f"{left_date.day}_{left_date.hour}-{right_date.day}_{right_date.hour}"
        if not os.path.isdir(dirName):
            os.makedirs(dirName)
        fileName = f"dateRange-{i}.json"
        ips = ips.union(ip)
        if df:
            to_json(df, os.path.join(dirName, fileName))
        # endfor
    # endfor


if __name__ == "__main__":
    dateRange = ["24 Apr 2023 21:00:42 GMT", "24 Apr 2023 21:59:42 GMT"]
    the_format = "%d %b %Y %H:%M:%S %Z"
    left_date = datetime.strptime(dateRange[0], the_format)
    right_date = datetime.strptime(dateRange[1], the_format)
    dateRange = [left_date, right_date]
    # get2Hop(dateRange)
    host = "99.999.9.35"
    df, _ = slicePcap(dateRange, read_json(f'{host}/OneHop.json'))
    dirName = f"{host}"
    if not os.path.isdir(dirName):
        os.makedirs(dirName)
    fileName = f"dateRange.json"
    if df:
        to_json(df, os.path.join(dirName, fileName))

    with open(f"{host}/tcp.csv", "w", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([f'FRAME_TIME', 'TCP_DECODE'])
        for data in df:
            writer.writerow([data["_source"]["layers"]['frame']["frame.time"], data["_source"]["layers"]["tcp"]["tcp.payload"]])


