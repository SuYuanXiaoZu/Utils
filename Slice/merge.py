import os
import json

hosts = ["99.999.9.10", "99.999.9.16", "99.999.9.19", "99.999.9.23", "99.999.9.27", "99.999.9.35"]


def merge():
    for host in hosts:
        oneHop = []
        twoHop = []
        for file in os.listdir(host):
            path = os.path.join(host, file)
            with open(path, "r", encoding="utf8") as f:
                df = json.load(f)
                if file.startswith("One"):
                    oneHop.extend(df)
                else:
                    twoHop.extend(df)

        onePath = f"{host}/OneHop.json"
        twoPath = f"{host}/TwoHop.json"
        with open(onePath, "w", encoding="utf8") as f:
            json.dump(oneHop, f, indent=4)
        with open(twoPath, "w", encoding="utf8") as f:
            json.dump(twoHop, f, indent=4)
        print(f"Done processing for {host}.")


if __name__ == "__main__":
    merge()
