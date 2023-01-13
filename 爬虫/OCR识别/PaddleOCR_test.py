from paddleocr import PaddleOCR, draw_ocr
import os
import time
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

start=time.time()
# 模型路径下必须含有model和params文件
ocr = PaddleOCR(use_angle_cls=True,
                use_gpu=False,lang="en"
                )  # det_model_dir='{your_det_model_dir}', rec_model_dir='{your_rec_model_dir}', rec_char_dict_path='{your_rec_char_dict_path}', cls_model_dir='{your_cls_model_dir}', use_angle_cls=True
img_path = r'img_1.png'
result = ocr.ocr(img_path, cls=True)
for line in result:
    print(line)
print(time.time()-start)
# # 显示结果
# from PIL import Image
#
# image = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
# txts = [line[1][0] for line in result]
# scores = [line[1][1] for line in result]
# im_show = draw_ocr(image, boxes, txts, scores, font_path='D:/paddle_pp/PaddleOCR/doc/simfang.ttf')
# im_show = Image.fromarray(im_show)
# im_show.save('result.jpg')  # 结果图片保存在代码同级文件夹中。