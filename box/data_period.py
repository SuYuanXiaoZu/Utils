from datetime import datetime
import json
import csv
import os
from tqdm import trange

Filter_command = ["data", "http.unknown_header", "http.file_data"]

hosts = ["99.999.9.3", "99.999.9.5", "99.999.9.7", "99.999.9.10", "99.999.9.11", "99.999.9.12", "99.999.9.13",
         "99.999.9.14", "99.999.9.16", "99.999.9.17", "99.999.9.18", "99.999.9.19", "99.999.9.20", "99.999.9.21",
         "99.999.9.22", "99.999.9.23", "99.999.9.25", "99.999.9.26", "99.999.9.27", "99.999.9.28", "99.999.9.29",
         "99.999.9.30", "99.999.9.31", "99.999.9.32", "99.999.9.33", "99.999.9.34", "99.999.9.35", "99.999.9.36",
         "99.999.9.37"]


def getDate(data):
    source = data.get("_source")
    if source:
        layers = source.get("layers")
    if layers:
        http = layers.get("http")
        if http:
            content = list(http.keys())
            if content[0] not in Filter_command:
                date = http.get("http.date")
                if date:
                    return datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT")
                else:
                    return ""
    return ""


if __name__ == '__main__':
    last_time_dict = {}
    first_time_dict = {}
    analysis_dir = '../../Analysis/'
    if not os.path.isdir(analysis_dir):
        os.mkdir(analysis_dir)
    for ip in hosts:
        with open(f'../Slice/{ip}/OneHop.json', 'r') as FJ:
            frame = json.load(FJ)
            # 读取json文件内容
            for i in range(len(frame)):
                data = frame[i]
                date = getDate(data)
                if date:
                    if ip not in first_time_dict.keys() or date < first_time_dict[ip]:
                        first_time_dict[ip] = date
                    else:
                        break
            for i in range(len(frame) - 1, -1, -1):
                date = getDate(frame[i])
                if date:
                    if ip not in last_time_dict.keys() or date > last_time_dict[ip]:
                        last_time_dict[ip] = date
                    else:
                        break
        print(ip)
    sorted_dict = dict(sorted(first_time_dict.items(), key=lambda x: x[1]))
    with open("period.csv", "w", encoding="utf-8") as fw:
        writer = csv.writer(fw)
        writer.writerow(['ATTACK IP', 'FIRST DATE', 'LATEST DATE'])
        for host in sorted_dict:
            writer.writerow([host, first_time_dict[host], last_time_dict[host]])
