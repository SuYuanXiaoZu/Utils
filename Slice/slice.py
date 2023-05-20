import json
import os
from tqdm import trange
encoding='ISO-8859-1'
dataDir = "../.."
hosts1 = ["99.999.9.10", "99.999.9.16", "99.999.9.19", "99.999.9.23", "99.999.9.27", "99.999.9.35"]
hosts2 = ["99.999.9.3", "99.999.9.5", "99.999.9.7", "99.999.9.10", "99.999.9.11", "99.999.9.12", "99.999.9.13", "99.999.9.14", "99.999.9.16", "99.999.9.17", "99.999.9.18", "99.999.9.19", "99.999.9.20", "99.999.9.21", "99.999.9.22", "99.999.9.23", "99.999.9.25", "99.999.9.26", "99.999.9.27", "99.999.9.28", "99.999.9.29", "99.999.9.30", "99.999.9.31", "99.999.9.32", "99.999.9.33", "99.999.9.34", "99.999.9.35", "99.999.9.36", "99.999.9.37"]
hosts = [_ for _ in hosts2 if _ not in hosts1]
def slicePcap(ips, df, filterIps=None):
    if filterIps is None:
        filterIps = []
    oneHopDf = []
    oneHopIp = set()
    for i in range(len(df)):
        try:
            ipSrc = df[i]['_source']['layers']['ip']['ip.src']
            ipDst = df[i]['_source']['layers']['ip']['ip.dst']
            if ipSrc in ips and ipDst not in filterIps:
                oneHopDf.append(df[i])
                oneHopIp.add(ipDst)
            # endif
            if ipDst in ips and ipSrc not in filterIps:
                oneHopDf.append(df[i])
                oneHopIp.add(ipSrc)
            # endif
        except KeyError:  # no IP
            continue
    # endfor
    return oneHopDf, oneHopIp


def read_json(path):
    with open(path, "r", encoding=encoding) as f:
        df = json.load(f)
        return df


def to_json(df, path):
    with open(path, "w", encoding=encoding) as f:
        json.dump(df, f, indent=4)


def get2Hop(chunkNum=20):
    oneHopIps = [set() for _ in range(len(hosts))]
    for i in trange(chunkNum, desc="OneHop"):
        path = f"{dataDir}/xa{chr(ord('a') + i)}"
        dataset = read_json(path)
        for j, host in enumerate(hosts):
            oneHopDf, oneHopIp = slicePcap([host], dataset)
            dirName = f"{host}"
            if not os.path.isdir(dirName):
                os.makedirs(dirName)
            fileName = f"OneHop-{i}.json"
            oneHopIps[j] = oneHopIps[j].union(oneHopIp)
            if oneHopDf:
                to_json(oneHopDf, os.path.join(dirName, fileName))
        # endfor
    # endfor

    for i in trange(chunkNum, desc="TwoHop"):
        path = f"{dataDir}/xa{chr(ord('a') + i)}"
        dataset = read_json(path)
        for j, host in enumerate(hosts):
            print(f"\nOneHops for {host}: {oneHopIps[j]}")
            twoHopDf, _ = slicePcap(oneHopIps[j], dataset, filterIps=[host])
            dirName = f"{host}"
            if not os.path.isdir(dirName):
                os.makedirs(dirName)
            fileName = f"TwoHop-{i}.json"
            if twoHopDf:
                to_json(twoHopDf, os.path.join(dirName, fileName))
        # endfor
    # endfor


if __name__ == "__main__":
    get2Hop()
