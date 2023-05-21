import os
import json
from datetime import datetime

encoding='ISO-8859-1'
hosts1 = ["99.999.9.10", "99.999.9.16", "99.999.9.19", "99.999.9.23", "99.999.9.27", "99.999.9.35"]
hosts = ["99.999.9.3", "99.999.9.5", "99.999.9.7", "99.999.9.10", "99.999.9.11", "99.999.9.12", "99.999.9.13", "99.999.9.14", "99.999.9.16", "99.999.9.17", "99.999.9.18", "99.999.9.19", "99.999.9.20", "99.999.9.21", "99.999.9.22", "99.999.9.23", "99.999.9.25", "99.999.9.26", "99.999.9.27", "99.999.9.28", "99.999.9.29", "99.999.9.30", "99.999.9.31", "99.999.9.32", "99.999.9.33", "99.999.9.34", "99.999.9.35", "99.999.9.36", "99.999.9.37"]


if __name__ == "__main__":
    time_dict = {}
    for host in hosts:
        filelist = os.listdir(host)
        filelist = list(filter(lambda fn: fn.startswith("OneHop-"), filelist))
        filelist.sort(key=lambda fn:int(fn.split('.')[0][7:]))
        if filelist:
            file = filelist[-1]
            path = os.path.join(host, file)
            with open(path, "r", encoding=encoding) as f:
                data = json.load(f)
                for i in range(len(data)-1, -1, -1):
                    try:
                        time = data[i].get("_source").get("layers").get("frame").get("frame.time")
                        time = time[:time.rfind(' ')][:-3]
                        date_format = "%b %d, %Y %H:%M:%S.%f"
                        time_obj = datetime.strptime(time, date_format)
                        time_dict[host] = time_obj
                        break
                    except KeyError:
                        continue
    sorted_dict = dict(sorted(time_dict.items(), key=lambda x: x[1]))
    print(sorted_dict)