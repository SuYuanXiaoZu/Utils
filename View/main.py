from datetime import datetime
import json
import binascii

import csv
import os
import sys

Filter_command = ["data", "http.unknown_header", "http.file_data"]
none = " "


def hex_a2b(string):  # 十六进制转ASCII接口
    str_out = string.replace(":", "")

    # print(str_out)
    if len(str_out) % 2 != 0:
        str_out = str_out[:len(str_out) - 1]

    text = binascii.a2b_hex(str_out)

    return text


def unicode(string):  # UNICODE转ASCII接口
    str_out = string[0].decode('unicode_escape')  # .encode("EUC_KR")
    print(str_out)


if __name__ == '__main__':
    attack_ip = ""
    if len(sys.argv) == 2:
        attack_ip = sys.argv[1]
    else:
        print("Usage: python main.py attack_ip. Example: python main.py 99.999.9.35")
    res_dir = '../../Analysis/' + attack_ip
    if not os.path.isdir(res_dir):
        os.mkdir(res_dir)
    time_dict = {}
    with open(f'../Slice/{attack_ip}/OneHop.json', 'r') as FJ:
        with open(res_dir + f"/basic.csv", "w", encoding="utf-8") as fw:
            writer = csv.writer(fw)
            writer.writerow([f'FRAME_TIME', 'HTTP', 'HOST', 'POST', 'TCP_DECODE', 'HTTP_DECODE', 'DATE'])
            frame = json.load(FJ)
            # 读取json文件内容
            for data in frame:  #
                source = data.get("_source")
                if source:
                    layers = source.get("layers")
                if layers:
                    frame = layers.get("frame")
                    if frame:
                        frame_time = frame.get("frame.time")
                    eth = layers.get("eth")
                    if eth:
                        eth_dst = eth.get("eth.dst")

                    ip = layers.get("ip")

                    tcp = layers.get("tcp")
                    if tcp:
                        tcp_payload = tcp.get("tcp.payload")
                        tcp_flags_tree = tcp.get("tcp.flags_tree")
                        if tcp_flags_tree:
                            tcp_flags_str = tcp_flags_tree.get("tcp.flags.str")

                    http = layers.get("http")
                    if http:
                        content = list(http.keys())
                        HTTP_chunked_response = http.get("HTTP chunked response")
                        if content[0] not in Filter_command:
                            if frame_time:
                                content_write = [frame_time[:21], content[0], "", "", "", "", ""]
                                date = http.get("http.date")
                                if date:
                                    content_write[-1] = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT")
                                if content[0].startswith("POST"):
                                    host = http.get("http.host")
                                    post_data = layers.get("urlencoded-form")
                                    if host:
                                        content_write[2] = host
                                        if date and not (host in time_dict.keys() and date <= time_dict[host]):
                                            time_dict[host] = date
                                    if post_data:
                                        content_write[3] = str([key[12:] for key in post_data])

                                if tcp_payload:
                                    content_write[4] = hex_a2b(tcp_payload)

                                if HTTP_chunked_response:
                                    for Data_chunk in HTTP_chunked_response:
                                        # print(Data_chunk)
                                        if str("Data") in Data_chunk:
                                            # print(Data_chunk)
                                            http_chunk_data = HTTP_chunked_response.get(Data_chunk)
                                            http_chunk_data = http_chunk_data.get("http.chunk_data")
                                            if http_chunk_data:
                                                content_write[5] = hex_a2b(http_chunk_data)
                                writer.writerow(content_write)
    with open(res_dir + f"/latest_dates.csv", "w", encoding="utf-8") as fw:
        writer = csv.writer(fw)
        writer.writerow([f'TARGET IP', 'LATEST DATE'])
        for host in time_dict:
            writer.writerow([host, time_dict[host]])
