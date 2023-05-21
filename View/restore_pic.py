from PIL import Image
import io

# image_bytes字节字符串表示图像数据
image_bytes = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00H\x00\x00\x00!\x08\x04\x00\x00\x00\xd0\x1f%^\x00\x00\x00\tpHYs\x00\x00\r\xd7\x00\x00\r\xd7\x01B(\x9bx\x00\x00\x03\x18iCCPPhotoshop ICC profile\x00\x00x\xdac``\x9e\xe0\xe8\xe2\xe4\xca$\xc0\xc0PPTR\xe4\x1e\xe4\x18\x19\x11\x19\xa5\xc0~\x9e\x81\x8d\x81\x99\x81\x81\x81\x81\x81!1\xb9\xb8\xc01 \xc0\x87\x81\x81\x81!/?/\x95\x01\x15020|\xbb\xc6\xc0\xc8\xc0\xc0\xc0pY\xd7\xd1\xc5\xc9\x95\x814\xc0\x9a\\PT\xc2\xc0\xc0p\x80\x81\x81\xc1(%\xb58\x99\x81\x81\xe1\x0b\x03\x03CzyIA\t\x03\x03c\x0c\x03\x03\x83HRvA\t\x03\x03c\x01\x03\x03\x83HvH\x903\x03\x03c\x0b\x03\x03\x13OIjE\t\x03\x03\x03\x83s~AeQfzF\x89\x82\xa1\xa5\xa5\xa5\x82cJ~R\xaaBpeqIjn\xb1\x82g^r~QA~QbIj\n\x03\x03\x03\xd4\x0e\x06\x06\x06\x06^\x97\xfc\x12\x05\xf7\xc4\xcc<\x05#\x03U\x06*\x83\x88\xc8(\x05\x08\x0b\x11>\x081\x04H.-*\x83\x07%\x03\x83\x00\x83\x02\x83\x01\x83\x03C\x00C"C=\xc3\x02\x86\xa3\x0co\x18\xc5\x19]\x18K\x19W0\xdec\x12c\nb\x9a\xc0t\x81Y\x989\x92y!\xf3\x1b\x16K\x96\x0e\x96[\xacz\xac\xad\xac\xf7\xd8,\xd9\xa6\xb1}c\x0fg\xdf\xcd\xa1\xc4\xd1\xc5\xf1\x853\x91\xf3\x02\x97#\xd7\x16nM\xee\x05<R<Sy\x85x\'\xf1\t\xf3M\xe3\x97\xe1_,\xa0#\xb0C\xd0U\xf0\x8aP\xaa\xd0\x0f\xe1^\x11\x15\x91\xbd\xa2\xe1\xa2_\xc4&\x89\x1b\x89_\x91\xa8\x90\x94\x93<&\x95/--}B\xa6LV]\xf6\x96\\\x9f\xbc\x8b\xfc\x1f\x85\xad\x8a\x85JzJo\x95\xd7\xaa\x14\xa8\x9a\xa8\xfeT;\xa8\xde\xa5\x11\xaa\xa9\xa4\xf9A\xeb\x80\xf6$\x9dT]+=A\xbdW\xfaG\x0c\x16\x18\xd6\x1a\xc5\x18\xdb\x9a\xc8\x9b2\x9b\xbe4\xbb`\xbe\xd3b\x89\xe5\x04\xab:\xeb\\\x9b8\xdb@;W{k\x07cG\x1d\'5g%\x17\x05Wy7\x05we\x0fuO]/\x13o\x1b\x1fw\xdf`\xbf\x04\xff\xfc\x80\xfa\xc0\x89AK\x83w\x85\\\x0c}\x19\xce\x14!\x17i\x15\x15\x11]\x1133vO\xdc\x83\x04\xb6D\xdd\xa4\xb0\xe4\x86\x945\xa97\xd392,23\xb3\xe6f_\xcce\xcf\xb3\xcf\xaf(\xd8T\xf8\xaeX\xbb$\xabtU\xd9\x9b\n\xfd\xca\x92\xaa]5\x8c\xb5^uS\xeb\x1f6\xea5\xd54\x9fm\x95k+l?\xda)\xddU\xd4}\xbaW\xb5\xaf\xb1\xff\xeeD\x9bI\xb3\'\xff\x9d\x1a?\xed\xf0\x0c\x8d\x99\xfd\xb3\xbe\xcfI\x98{z\xbe\xf9\x82\xa5\x8bD\x16\xb7.\xf9\xb6,s\xf9\xbd\x95!\xabN\xafqY\xbbo\xbd\xe5\x86m\x9bL6o\xd9j\xb2m\xfb\x0e\xab\x9d\xfbw\xbb\xee9\xbb/l\xff\x83\x839\x87~\x1ei?&~|\xc5I\xebS\xe7\xce$\x9f\xfdu~\xd2E\xedKG\xaf$^\xfdw}\xceM\x9b[w\xef\xd4\xdfS\xbe\x7f\xe2a\xdec\xb1\'\xfb\x9fe\xbe\x10yy\xf0u\xfe[\xf9w\x17>4}2\xfd\xfc\xea\xeb\x82\xef\xe1?\x05~\x9d\xfa\xd3\xfa\xcf\xf1\xff\x7f\x00\r\x00\x0f4\xfa\x96\xf1]\x00\x00\x00 cHRM\x00\x00z%\x00\x00\x80\x83\x00\x00\xf9\xff\x00\x00\x80\xe9\x00\x00u0\x00\x00\xea`\x00\x00:\x98\x00\x00\x17o\x92_\xc5F\x00\x00\x00\xdaIDATx\xda\xcc\xd6\xbb\r\xc20\x14\x85\xe1?!b\x00\x06`\x96\x0c\xc2v\x84\x96\t(2K`\x00Z(0\x85Ay\xd9\x8e"\x81\xcf\xbd\xbd\xa5O\xf7\xe9\xc2\x91\x8c\x9a\x1a\xb8q\xe4A\x96(mq\xd2 \x01\x07\xaa\x05\xce\x95&\'\'\x9e!\x11\'\x06\x92q\xc2 !\'\x04\x92r\xe6 1g\n\x92s\xc6c\xef9\x1d\'\x1dg\x98!\x13\x9c>C_N\xc3\x13i\x94\xb68>C\x9es\xe7\xc2n\xc5\xcb\r/\xdc\xefA\x85\xf3\x1c3Qb,*Z\xf8\x94\xec\xbc\xaa\x83\xfeV2cM\xedK\xd6\xd2\x02{\x0el\xad\xf4\x90\x19R\xdf\xd4FH\xc3)3A\x1a\x8f\xbd\x01\xd2t\x0f\xc9I\xf3\xc5(&\x856\xb5\x94\x14>\x1dBR\xec\x96\xc9H\xf1\xe3*"\xa5\xae\xbd\x84\x94\xfe~\x08HK\xff\xa1\xec\xa4\xf7\x00\xab\x0cV\x9da\xb46\x9c\x00\x00\x00\x00IEND\xaeB`\x82'
# 创建一个BytesIO对象并将字节字符串写入其中
image_io = io.BytesIO(image_bytes)

# 打开图像文件
# image = Image.open(image_io)
#
# # 保存图像文件
# image.save("restored_image.jpg")  # 以JPEG格式保存，可以根据需要修改文件名和保存格式
with open("test.jpg", "wb") as f:
    f.write(image_bytes)