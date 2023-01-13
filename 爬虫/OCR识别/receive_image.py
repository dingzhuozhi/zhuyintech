import pytesseract
from PIL import Image
import socket
import base64
import io
from datetime import datetime
def picture2base(path):
    with open(path, 'rb') as img:
        # 使用base64进行编码
        b64encode = base64.b64encode(img.read())
        s = b64encode.decode()
        base64 = 'data:image/jpeg;base64,%s' % s
        # 返回base64编码字符串
        return base64

def base2picture(base64_data):
    # 分割字符串
    res = base64_data.split(',')[1]
    # 使用base64进行解码
    b64decode = base64.b64decode(res)
    image1 = io.BytesIO(b64decode)
    img = Image.open(image1)
    img.show()
    # 写到图片文件中
    file = open('demo.jpg', 'wb')
    file.write(b64decode)
    file.close()


def receive_udp(port):
    """
    :param port:
    :return: information
    """
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as udp_socket:
        local_addr = ("", port)
        udp_socket.bind(local_addr)

        base64_data= udp_socket.recvfrom(1024000)
        base2picture(base64_data)
        text=pytesseract.image_to_string(Image.open('demo.jpg',lang="eng"))
        #print(recv_data[0].decode("utf-8")) #接收 UDP 数据，与 recv() 类似，单返回值是（data,address）。其中 data 是包含接收数据的字符串，addrress 是发送数据的套接字
        print(text)
        #print("发送方的ip和端口",recv_data[1])
        return text

if __name__ == '__main__':
    print(f"开始执行receive模型, 当前时间为 {datetime.now()}")
    receive_udp(40001)