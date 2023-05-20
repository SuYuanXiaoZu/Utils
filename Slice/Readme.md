## Slice
首先运行（非windows命令，可能需要在wsl或者虚拟机切一下）
```
    split -n 20 dataset.json
```
然后运行clean.py来拼接一下分片json为正确的格式
```
    python clean.py
```
接着运行分片程序
```
    python slice.py
```
最后将切片的json拼到一起
```
    python merge.py
```
因为切片是2g，所以估计4g内存就可以运行。运行时间本机测试20min左右即可全部运行完毕。

已切好的数据链接 https://cloud.tsinghua.edu.cn/d/56748a9b89a849d4920d/