import pytesseract
from PIL import Image
import socket
import io
import base64


sock = socket.socket()
sock.setsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF, 393303)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF, 393303)
recv_buff = sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
send_buff = sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
print(f'修改后接收缓冲区大小：{recv_buff}。修改后发送缓冲区大小：{send_buff}')

def picture2base(path):
    with open(path, 'rb') as img:
        # 使用base64进行编码
        import base64
        b64encode_data = base64.b64encode(img.read())
        s = b64encode_data.decode()
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


def send_udp(host,port,imagepath):
    """
    :param host:
    :param port:
    :param message:
    :return:
    爬虫发送至指定端口，一般发到 127.0.0.1
    """
    picture_data= picture2base(imagepath) #转成base64编码字符串
    print(len(picture_data))
    picture_data=picture_data[:60536]
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as s:
        s.sendto(picture_data.encode(),(host,port))



def receive_udp(port):
    """
    :param port:
    :return: information
    """
    with socket.socket(socket.AF_INET,socket.SOCK_DGRAM) as udp_socket:
        local_addr = ("", port)
        udp_socket.bind(local_addr)

        base64_data= udp_socket.recvfrom(393303)
        base2picture(base64_data)
        text=pytesseract.image_to_string(Image.open('demo.jpg',lang="eng"))
        #print(recv_data[0].decode("utf-8")) #接收 UDP 数据，与 recv() 类似，单返回值是（data,address）。其中 data 是包含接收数据的字符串，addrress 是发送数据的套接字
        print(text)
        #print("发送方的ip和端口",recv_data[1])
        return text


if __name__ == '__main__':
    #text=pytesseract.image_to_string(Image.open(r"D:\pachong\OCR识别\img.png"),lang="eng")
    #print(text)
    send_udp(host="192.168.7.70",port=40001,imagepath="img.png")



