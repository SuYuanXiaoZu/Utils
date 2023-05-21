import json
import csv
import os


filter_keys = ["data-text-lines"]
filter_prefix = ["GET", "POST", "Form item:", "HTTP/1.1", "Data chunk (", "Content-encoded entity body (gzip):", " [truncated]", "CONNECT ", "Data: (", "Extension:"]
hosts = ["99.999.9.3", "99.999.9.5", "99.999.9.7", "99.999.9.10", "99.999.9.11", "99.999.9.12", "99.999.9.13",
         "99.999.9.14", "99.999.9.16", "99.999.9.17", "99.999.9.18", "99.999.9.19", "99.999.9.20", "99.999.9.21",
         "99.999.9.22", "99.999.9.23", "99.999.9.25", "99.999.9.26", "99.999.9.27", "99.999.9.28", "99.999.9.29",
         "99.999.9.30", "99.999.9.31", "99.999.9.32", "99.999.9.33", "99.999.9.34", "99.999.9.35", "99.999.9.36",
         "99.999.9.37"]

analysis_dir = '../../Analysis/'


def flat_collector(dict):
    if hasattr(dict, 'items'):
        for k, v in dict.items():
            if not any(k.startswith(prefix) for prefix in filter_prefix):
                yield k, v
            if k not in filter_keys:
                for val in flat_collector(v):
                    yield val


if __name__ == '__main__':
    if not os.path.isdir(analysis_dir):
        os.mkdir(analysis_dir)
    kv_dict = {}
    for attack_ip in hosts:
        with open(f'../Slice/{attack_ip}/OneHop.json', 'r') as FJ:
            frame = json.load(FJ)
            # 读取json文件内容
            for data in frame:
                for kv in flat_collector(data['_source']['layers']):
                    if kv[0] not in kv_dict:
                        kv_dict[kv[0]] = kv[1]
        print(attack_ip)
    with open(analysis_dir + "/all_kv.csv", "w", encoding="utf-8") as fw:
        writer = csv.writer(fw)
        writer.writerow(['KEY', 'VALUE'])
        for k, v in kv_dict.items():
            writer.writerow([k, v])
