#! usr/bin/python
import math, random

fileOut = open('image.ppm', 'w')
out = 'P3\n500 500\n255\n'


#draw
for y in range(500):
    for x in range(500):
        color = {'r' : (x + 211) % 256  + 135 % 67, 'g': (x+150) % 256  + 12 % 192, 'b': (x + 145) % 256  + 189 % 51}
        out += '{r} {g} {b} '.format(**color)



#write file
fileOut.write(out)
fileOut.close()
