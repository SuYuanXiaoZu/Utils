from datetime import datetime
import json
import binascii

import csv
import os
import sys

decode_keys = ["tcp.payload", "data.data", "tcp.segment_data", "tcp.reassembled.data", "http.chunk_data", "media.type",
               "image-jfif.entropy_coded_segment", "knet.payload.data", "gryphon.padding", "gryphon.data.header_data",
               "gryphon.data.data", "gryphon.data.extra_data", "gryphon.event.data", "gryphon.data"]

hosts = ["99.999.9.3", "99.999.9.5", "99.999.9.7", "99.999.9.10", "99.999.9.11", "99.999.9.12", "99.999.9.13",
         "99.999.9.14", "99.999.9.16", "99.999.9.17", "99.999.9.18", "99.999.9.19", "99.999.9.20", "99.999.9.21",
         "99.999.9.22", "99.999.9.23", "99.999.9.25", "99.999.9.26", "99.999.9.27", "99.999.9.28", "99.999.9.29",
         "99.999.9.30", "99.999.9.31", "99.999.9.32", "99.999.9.33", "99.999.9.34", "99.999.9.35", "99.999.9.36",
         "99.999.9.37"]

def hex_a2b(string):  # 十六进制转ASCII接口
    str_out = string.replace(":", "")
    if len(str_out) % 2 != 0:
        str_out = str_out[:len(str_out) - 1]

    text = binascii.a2b_hex(str_out)
    return text


analysis_dir = '../../Analysis/'


def flat_collector(dict):
    if hasattr(dict, 'items'):
        for k, v in dict.items():
            if k in decode_keys:
                yield k, v
            for val in flat_collector(v):
                yield val


def interpret(attack_ip):
    res_dir = analysis_dir + attack_ip
    if not os.path.isdir(res_dir):
        os.mkdir(res_dir)

    with open(f'../Slice/{attack_ip}/OneHop.json', 'r') as FJ:
        with open(res_dir + f"/decode_light.csv", "w", encoding="utf-8") as fw:
            writer = csv.writer(fw)
            writer.writerow(decode_keys)
            frame = json.load(FJ)
            # 读取json文件内容
            cnt_list = [0 for _ in decode_keys]
            cnt = 0
            for data in frame:
                if cnt == len(decode_keys):
                    break
                content_write = ["" for _ in decode_keys]
                for k, v in flat_collector(data['_source']['layers']):
                    ind = decode_keys.index(k)
                    content_write[ind] = hex_a2b(v)
                    if cnt_list[ind] == 0:
                        cnt_list[ind] = 1
                        cnt += 1
                writer.writerow(content_write)


if __name__ == '__main__':
    if not os.path.isdir(analysis_dir):
        os.mkdir(analysis_dir)
    if len(sys.argv) == 2:
        interpret(sys.argv[1])
    else:
        for ip in hosts:
            interpret(ip)
