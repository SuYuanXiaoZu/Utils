
import json
import binascii

import csv
Filter_command=["data","http.unknown_header","http.file_data"]
none=" "
def hex_a2b(string):#十六进制转ASCII接口
    str_out=string.replace(":","")

    #print(str_out)
    if len(str_out)%2!=0:
        str_out=str_out[:len(str_out)-1]

    text = binascii.a2b_hex(str_out)




    return text
def unicode(string):#UNICODE转ASCII接口
    str_out = string[0].decode('unicode_escape')  # .encode("EUC_KR")
    print(str_out)


if __name__ == '__main__':

    with open('/Users/krz/Downloads/99.999.9.23/TwoHop.json', 'r') as FJ:
        with open("/Users/krz/Downloads/99.999.9.23/test2.csv", "w", encoding="utf-8") as fw:
            writer = csv.writer(fw)
            writer.writerow([f'TIME', 'HTTP','TCP_DECODE','HTTP_DECODE'])
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
                            #print(hex_a2b(tcp_payload))
                            pass
                        tcp_flags_tree=tcp.get("tcp.flags_tree")
                        if(tcp_flags_tree):
                            tcp_flags_str=tcp_flags_tree.get("tcp.flags.str")

                            #print(tcp_flags_str)



                    http=layers.get("http")
                    if(http):
                        content=list(http.keys())
                        HTTP_chunked_response=http.get("HTTP chunked response")
                        #print(HTTP_chunked_response)

                        if content[0] not in Filter_command:
                            if(frame_time):
                                content_write = [frame_time[:21], content[0]]
                                if (tcp_payload):

                                    content_write.append(hex_a2b(tcp_payload))
                                else:
                                    content_write.append(none)

                                if(HTTP_chunked_response):

                                    for Data_chunk in HTTP_chunked_response:
                                        #print(Data_chunk)
                                        if(str("Data")in Data_chunk ):
                                            #print(Data_chunk)
                                            http_chunk_data=HTTP_chunked_response.get(Data_chunk)
                                            http_chunk_data=http_chunk_data.get("http.chunk_data")
                                            if(http_chunk_data):
                                                content_write.append(hex_a2b(http_chunk_data))






                                writer.writerow(content_write)


                                #print(frame_time[:21],content[0])










