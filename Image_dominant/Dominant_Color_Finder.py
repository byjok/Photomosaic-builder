__author__ = 'apopov'
import math
from PIL import Image, ImageDraw
import os

def Image_Dominant_Finder(name):

    f = open('database.txt', 'a')
    sumR = 0
    sumG = 0
    sumB = 0
    image = Image.open(name)  #Открываем изображение.
    width = image.size[0]  #Определяем ширину.
    height = image.size[1]  #Определяем высоту.
    pix = image.load()  #Выгружаем значения пикселей.

    for i in range(width):
        for j in range(height):
            sumR += pix[i, j][0]
            sumG += pix[i, j][1]
            sumB += pix[i, j][2]

    f.write(name + ' ' + str(math.ceil(sumR/(width*height))) + ' ' + str(math.ceil(sumG/(width*height))) + ' ' + str(math.ceil(sumB/(width*height))) + '\n')
    f.close()

files = os.listdir()
images = filter(lambda x: x.endswith('.jpg'), files)
for i in images:
    Image_Dominant_Finder(i)
