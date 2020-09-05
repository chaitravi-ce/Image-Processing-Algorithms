import matplotlib.pyplot as plt
import math
import numpy as np

A = plt.imread('edge-detection.png')
height, width, channel = A.shape
rgb_weights = [0.2989, 0.5870, 0.1140]
B = np.dot(A[..., :3], rgb_weights)

C = B.copy()

for i in range(1, height - 2):
    for j in range(1, width - 2):
        Gx = ((2 * C[i + 2][j + 1] + C[i + 2][j] + C[i + 2][j + 2]) - (2 * C[i][j + 1] + C[i][j] + C[i][j + 2]))
        Gy = ((2 * C[i + 1][j + 2] + C[i][j + 2] + C[i + 2][j + 2]) - (2 * C[i + 1][j] + C[i][j] + C[i + 2][j]))
        B[i][j] = math.sqrt(Gx * Gx + Gy * Gy)
plt.show(B)
