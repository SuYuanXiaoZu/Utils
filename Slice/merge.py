import os
import json

encoding = 'ISO-8859-1'
hosts = ["99.999.9.10", "99.999.9.16", "99.999.9.19", "99.999.9.23", "99.999.9.27", "99.999.9.35"]

def mergeHop(hop):
    for host in hosts:
        hops = []
        filelist = os.listdir(host)
        filelist = list(filter(lambda fn: fn.startswith(hop+"-"), filelist))
        filelist.sort(key=lambda fn: int(fn.split('.')[0][7:]))
        for file in filelist:
            path = os.path.join(host, file)
            try:
                with open(path, "r", encoding=encoding) as f:
                    df = json.load(f)
                    hops.extend(df)
            except json.decoder.JSONDecodeError:
                print(path)
        with open(f"{host}/{hop}.json", "w", encoding=encoding) as f:
            json.dump(hops, f, indent=4)
        print(f"Done processing for {host}.")


if __name__ == "__main__":
    mergeHop("OneHop")
    mergeHop("TwoHop")
