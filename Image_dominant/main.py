__author__ = 'apopov'
from Dominant_Color_Finder import Image_solver
import os

r = Image_solver
files = os.listdir()
images = filter(lambda x: x.endswith('.jpg'), files)

for i in images:
    r.Write_to_database(i)
