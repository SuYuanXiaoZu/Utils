from tqdm import trange
dataDir = "../.."
encoding='ISO-8859-1'
if __name__ == "__main__":
    chunkNum = 20
    reserved = []
    for i in trange(chunkNum):
        name = f"{dataDir}/xa{chr(ord('a')+i)}"
        with open(name, "r", encoding=encoding) as f:
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
        with open(name, "w", encoding=encoding) as f:
            f.writelines(cleanedLines)
