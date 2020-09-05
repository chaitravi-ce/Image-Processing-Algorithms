import numpy as np
import math as m
import matplotlib.pyplot as plt

img = plt.imread('rotate.png')
height, width, num_channels = img.shape

angle = int(input("Enter an Angle : "))
radian = m.radians(angle)

maxLength = int(m.sqrt(height ** 2 + width ** 2))

opImg = np.zeros((maxLength, maxLength, num_channels))

rotH, rotW, _ = opImg.shape

midR = int((rotH + 1) / 2)
midC = int((rotW + 1) / 2)

for r in range(rotH):
    for c in range(rotW):
        y = (r - midC) * m.cos(radian) + (c - midR) * m.sin(radian)
        x = -(r - midC) * m.sin(radian) + (c - midR) * m.cos(radian)
        y += midC
        x += midR
        y = int(y)
        x = int(x)
        if 0 <= x < width and 0 <= y < height:
            opImg[r][c][:] = img[y][x][:]

plt.imshow(opImg)
plt.show()
