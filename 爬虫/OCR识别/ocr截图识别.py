import pytesseract
import time
from PIL import ImageGrab

if __name__ == "__main__":
    start = time.time()
    image = ImageGrab.grab((50, 50, 1450, 1400)) #左上，右下
    text = pytesseract.image_to_string(image, lang='eng')
    print(text)
    print(time.time() - start)

#实现截图识别文字，耗时约1.1s