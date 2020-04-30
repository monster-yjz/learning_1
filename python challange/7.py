# 　http://www.pythonchallenge.com/pc/def/oxygen.html

from PIL import Image

im = Image.open('oxygen.png')

print(''.
    join(
    [chr(i[0]) for i in
     [im.getpixel(
         (j, im.size[1] / 2))
         for j in range(0, im.size[0], 7)
     ]
     ]
)
)

key = [105, 110, 116, 101, 103, 114, 105, 116, 121]
print(''.join(chr(i) for i in key))
