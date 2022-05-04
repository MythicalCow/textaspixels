#Text As Image
#Storing text as pixels in an image

# imports Pil module
from PIL import Image
import random

text = open("dna.txt").read()
print(text)
print(len(text))
data_buffer = []
for i in text:
    data_buffer.append(i)
print(data_buffer)
    

# Code to create image of size 500x500 each with random pixel value
xsize = 50
ysize = 20
im = Image.new(mode = "RGB", size = (xsize, ysize))
for j in range(ysize):
    for i in range(xsize):
        im.putpixel([i,j],(ord(data_buffer.pop(0)),ord(data_buffer.pop(0)),ord(data_buffer.pop(0))))


# # this will show image in any image viewer
im.show()
