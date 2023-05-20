import json
import os
from tqdm import trange
import csv
from itertools import zip_longest
dataDir = "../.."


def read_json(path):
    with open(path, "r", encoding="utf8") as f:
        df = json.load(f)
        return df


def studentIP(ip):
    return ip.startswith('99.999.9')


if __name__ == "__main__":
    ips = set()
    src_ips = set()
    dst_ips = set()
    chunkNum = 20
    ip_time_mp = {}
    for i in trange(chunkNum, desc="IPCount"):
        path = f"{dataDir}/xa{chr(ord('a') + i)}"
        df = read_json(path)
        for j in range(len(df)):
            try:
                ipSrc = df[j]['_source']['layers']['ip']['ip.src']
                ipDst = df[j]['_source']['layers']['ip']['ip.dst']
                src_ips.add(ipSrc)
                dst_ips.add(ipDst)
                if studentIP(ipSrc):
                    ips.add(ipSrc)
                if studentIP(ipDst):
                    ips.add(ipDst)
                # endif
            except KeyError:  # no IP
                continue

        # endfor
    # endfor
    print(ips)
    print(len(ips))
    print(src_ips)
    print(len(src_ips))
    print(dst_ips)
    print(len(dst_ips))
    csv_file = 'ips.csv'
    max_length = max(len(ips), len(src_ips), len(dst_ips))

    # 将集合数据转换为列表，并使用zip_longest函数处理长度差异
    data = zip_longest(ips, src_ips, dst_ips, fillvalue='')
    # Write set data into CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['student_ip', 'src_ip', 'dst_ip'])  # Write header if needed
        writer.writerows(data)
