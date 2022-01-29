#encoding:utf8
import random
import six

from PIL import Image, ImageDraw, ImageFont
from io import BytesIO as StringIO

DISTANCE_FROM_TOP = 10
FONT_SIZE = 15
FONT_PATH = '../font/SIMYOU.TTF'
IMAGE_SIZE = (100,30)
BACKGROUND_COLOR = '#ffe'
FOREGROUND_COLOR = '#000'
# ASCII_CHAR = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
ASCII_CHAR = list("@#-")
# ASCII_CHAR = list("星星星星火。")


def captcha_image(text=''):
    length = len(text)
    image_size = (length*FONT_SIZE,FONT_SIZE)
    image = Image.new('RGB', image_size, BACKGROUND_COLOR)
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)
    draw.text((0, 0), text, FOREGROUND_COLOR, font=font)
    # image.show()
    return image, image_size

# 将256灰度映射到70个字符上，也就是RGB值转字符的函数：
def get_char(r, g, b, alpha=256):  # alpha透明度
   if alpha == 0:
       return ' '
   length = len(ASCII_CHAR)
   gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)  # 计算灰度
   unit = (256.0 + 1) / length
   return ASCII_CHAR[int(gray / unit)]  # 不同的灰度对应着不同的字符


def to_ascii(image, image_size):
    image = image.resize(image_size, Image.NEAREST)
    txt = ""
    for i in range(image_size[1]):
        for j in range(image_size[0]):
            txt += get_char(*image.getpixel((j, i))) # 获得相应的字符
        txt += '\n'
    print(txt)
    with open("./output.txt", 'w', encoding='utf8') as f:
       f.write(txt)

def draw_image(imgpath, times=1):
    image = Image.open(imgpath)
    image_size = (int(image.width*times), int(image.height*times))
    # print(image_size)
    to_ascii(image, image_size)

def draw_text(text=''):
    to_ascii(*captcha_image(text))

if __name__ == '__main__':
    print('''
------------------------------------------------------------
----------------------------------------------------#-------
------------------#---#-------------------------#---@----#--
------------------#---#-------------------------#---@----#--
-----------------#####@#####--------------------#---@----#--
-----------------@----@-----------------------##@###@######-
----------------##----#------------------------#@---@---##--
-#############--@-----#--------#############----#---@----#--
----------------------#-------------------------#---@----#--
-----------------@@@@@@@@@@@--------------------#---@----#--
----------------------#-------------------------#---@---##--
----------------------#-------------------------#----####---
----------------------#-------------------------#-----------
----------------------#-------------------------#-----------
----------------@@@@@@@@@@@@@-------------------@@@@@@@@@@#-
''')
    print("生成中....")
    draw_text("一生一世")
    print("已输出到output.txt，请查看")
    # draw_image("./1.jfif", times=0.08)