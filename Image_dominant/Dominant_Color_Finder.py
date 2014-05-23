__author__ = 'apopov'
import math
from PIL import Image


class Image_solver:
    def image_dominant_finder(name):

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

        return math.ceil(sumR/(width*height)), math.ceil(sumG/(width*height)),math.ceil(sumB/(width*height))

    def Write_to_database(name):
        f = open('database.txt', 'a')
        f.write(name + ' ' +str(Image_solver.image_dominant_finder(name))+ '\n')
        f.close()