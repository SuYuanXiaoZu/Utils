import gzip
import codecs
from bs4 import BeautifulSoup

count = 0
flag = ''
with open('./q4.txt', mode='r', encoding='utf-8') as f:
    for line in f.readlines():
        if "b'GET /index.php HTTP/1.1" == line[0:25]:
            count += 1
            continue
        elif count == 1:
            s = line[439:-2]
            s = codecs.escape_decode(s, "hex-escape")[0]
            uncompressed_data = gzip.decompress(s)
            # 将解压缩后的数据转换为字符串
            decoded_data = uncompressed_data.decode('utf-8')
            soup = BeautifulSoup(decoded_data, 'html.parser')
            # print(soup.prettify())
            res = soup.span.string
            if int(res) == 0:
                break
            res = chr(int(res))
            flag += res
            count = 0
print(flag)