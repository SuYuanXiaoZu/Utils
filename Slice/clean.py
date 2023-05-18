from tqdm import trange
dataDir = "dataset"

if __name__ == "__main__":
    chunkNum = 20
    reserved = []
    for i in trange(chunkNum):
        name = f"{dataDir}/xa{chr(ord('a')+i)}"
        with open(name, "r", encoding="utf8") as f:
            lines = f.readlines()
            if i != chunkNum - 1:
                for j in range(len(lines)-1, -1, -1):
                    line = lines[j]
                    if line.startswith("  },"):
                        cleanedLines = reserved + lines[:j] + ["}]"]
                        reserved = ["["] + lines[j+1:]
                        break
                    # endif
                # endfor
            else:
                cleanedLines = reserved + lines
        # endwith
        with open(name, "w", encoding="utf8") as f:
            f.writelines(cleanedLines)
