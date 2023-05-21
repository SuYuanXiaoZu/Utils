from datetime import datetime
import json
import binascii

import csv
import os
import sys

Filter_command = ["data", "http.unknown_header", "http.file_data"]

hosts = ["99.999.9.3", "99.999.9.5", "99.999.9.7", "99.999.9.10", "99.999.9.11", "99.999.9.12", "99.999.9.13",
         "99.999.9.14", "99.999.9.16", "99.999.9.17", "99.999.9.18", "99.999.9.19", "99.999.9.20", "99.999.9.21",
         "99.999.9.22", "99.999.9.23", "99.999.9.25", "99.999.9.26", "99.999.9.27", "99.999.9.28", "99.999.9.29",
         "99.999.9.30", "99.999.9.31", "99.999.9.32", "99.999.9.33", "99.999.9.34", "99.999.9.35", "99.999.9.36",
         "99.999.9.37"]
last_time_dict = {}
first_time_dict = {}


def hex_a2b(string):  # 十六进制转ASCII接口
    str_out = string.replace(":", "")

    # print(str_out)
    if len(str_out) % 2 != 0:
        str_out = str_out[:len(str_out) - 1]

    text = binascii.a2b_hex(str_out)

    return text


analysis_dir = '../../Analysis/'


def interpret(attack_ip):
    res_dir = analysis_dir + attack_ip
    if not os.path.isdir(res_dir):
        os.mkdir(res_dir)

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

                    tcp = layers.get("tcp")
                    if tcp:
                        tcp_payload = tcp.get("tcp.payload")

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

                                host = http.get("http.host")
                                post_data = layers.get("urlencoded-form")
                                if host:
                                    content_write[2] = host
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


if __name__ == '__main__':
    if not os.path.isdir(analysis_dir):
        os.mkdir(analysis_dir)
    if len(sys.argv) == 2:
        interpret(sys.argv[1])
    else:
        for ip in hosts:
            interpret(ip)

