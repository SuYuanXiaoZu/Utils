# 这是一个示例 Python 脚本。

# 按 ⌃R 执行或将其替换为您的代码。
# 按 双击 ⇧ 在所有地方搜索类、文件、工具窗口、操作和设置。
import json
import binascii

import struct
import csv
from scipy.spatial.distance import cdist
def hex_b2a(string):#十六进制转ASCII接口
    str_out=string.replace(":","")
    print(str_out)
    text = binascii.a2b_hex(str_out)


    return text
def unicode(string):#UNICODE转ASCII接口
    str_out = string[0].decode('unicode_escape')  # .encode("EUC_KR")
    print(str_out)


if __name__ == '__main__':
    #print_hi('PyCharm')
    with open('/Users/krz/Downloads/99.999.9.23/OneHop.json', 'r') as FJ:
        frame = json.load(FJ)
        # 读取json文件内容
        for data in frame:  #
            #print(d1)
            source = data.get("_source")
            if(source):
                #print(source)
                layers=source.get("layers")
                #print(layers)
            if(layers):
                frame=layers.get("frame")
                if(frame):
                    frame_time=frame.get("frame.time")
                eth=layers.get("eth")
                if(eth):
                    eth_dst=eth.get("eth.dst")
                    #print(eth_dst)


                ip=layers.get("ip")

                tcp=layers.get("tcp")
                if(tcp):
                    tcp_payload=tcp.get("tcp.payload")
                    if(tcp_payload):
                        #print(hex_b2a(tcp_payload))
                        pass
                    tcp_flags_tree=tcp.get("tcp.flags_tree")
                    if(tcp_flags_tree):
                        tcp_flags_str=tcp_flags_tree.get("tcp.flags.str")
                        #print(tcp_flags_str)



                http=layers.get("http")
                if(http):
                    content=list(http.keys())
                    if content[0]!=str("data") and content[0]!=str("http.unknown_header") and content[0]!=str("http.file_data")  :
                        if(frame_time):

                            print(frame_time[:21],content[0])






