import io
from PIL import Image
import pytesseract
import time
from PIL import ImageGrab



# with open('img.png', 'rb') as img:
#     # 使用base64进行编码
#     import base64
#
#     b64encode_data1 = base64.b64encode(img.read())
#     s = b64encode_data1.decode()
#     base64_data = 'data:image/jpeg;base64,%s' % s
#     # 返回base64编码字符串
#
# def base2picture(base64_data):
#     # 分割字符串
#     res = base64_data.split(',')[1]
#     # 使用base64进行解码
#     b64decode = base64.b64decode(res)
#    # image1 = io.BytesIO(b64decode)
#     file = open('demo.jpg', 'wb')
#     file.write(b64decode)
#     file.close()
#     text = pytesseract.image_to_string(Image.open(r'demo.jpg'), lang="eng")
#     print(text)

start=time.time()
# base2picture(base64_data)
# config = r'-c tessedit_char_blacklist=0123456789 --psm 6'
text = pytesseract.image_to_string(Image.open(r'img_1.png'), lang="eng")
text=text.strip()
#print(text)
#print("pytesseract识别耗时:",time.time()-start) #1.12秒

for index,letter in enumerate(text):
    if letter=="-":
        print(index)
        print(text[:index])

# from textblob import TextBlob
#
#
# # function to convert string to list
# def convert(lst):
#     return ([i for item in lst for i in item.split()])
#
#
# # add your string instead yor stng
# lst = [text]
# # here we convert string to list using the function
# lst = convert(lst)
# # initislising the mistakes variable
# mistakes = 0
# # printing the list to show if text is correct
# # print(lst)
# # here we take each item from list and correct it if it was not equal to original text that means that it has a mistake and if it is equal to old word then it does not have mistake
# error_words=[]
# for x in lst:
#     a = TextBlob(x)
#     if (a.correct() != x):
#         error_words.append(x)
#         mistakes = mistakes + 1
#
# for i in text.split(","):
#     for error_word in error_words:
#         if error_word in i:
#             print("错误句为:")
#             print(i)



# printing the number of mistakes
# import easyocr
# start=time.time()
# #设置识别中英文两种语言
# reader = easyocr.Reader(['ch_sim','en'], gpu = True) # need to run only once to load model into memory
# result = reader.readtext(r'img_1.png', detail = 0)
# print(result)
# print("easyocr识别耗时:",time.time()-start)


# from cnocr import CnOcr
# start=time.time()
# img_fp = r'img_1.png'
# ocr = CnOcr(det_model_name='en_PP-OCRv3_det', rec_model_name='en_PP-OCRv3') #英文识别
# out = ocr.ocr(img_fp)
# print(out)
# print("CnOcr识别耗时:",time.time()-start)