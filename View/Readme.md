## count_all_kv
统计所有99网段的IP的OneHop数据中的全部key，并为每个key列举一个value作为内容示例。
## decode_all
解码全部编码字段。
## restore_pic
从binary字符串中恢复图片。
## view
提取时间戳、IP、POST参数、tcp payload 和http payload等字段并解码至csv中以便查看。
## unzipgzip
解压gzip压缩的HTTP响应
## sliceTime

截取自定义时间段[a, b]中所有不含http、仅含有tcp的包并生成相应的csv文件。适用于第六题定位了攻击命令后分析对应执行反弹shell命令。

## decodeFlagOfTask4

解析第四题flag的代码。
