import math
import os
from PIL import Image
import numpy as np

# LABEL = 'car'
# LABEL = 'bike'
LABEL = 'test'
dir_name = os.path.join('dataset', 'train', LABEL)
data = os.scandir(dir_name)

IMAGE_SIZE = 224
KERNEL_SIZE = 14
STRIDE = 3

kernels = 0.02 * np.random.random((KERNEL_SIZE, KERNEL_SIZE, 3)) - 0.01
kernel_out_size = int((IMAGE_SIZE - KERNEL_SIZE) / STRIDE + 1)

for file in data:
    image = Image.open(file.path).resize((IMAGE_SIZE, IMAGE_SIZE))
    # матрица пикселей картинки
    layer_0 = np.array(list(image.getdata())).reshape(IMAGE_SIZE, IMAGE_SIZE, 3)
    # результат работы сверточного слоя
    kernel_output = np.zeros((kernel_out_size, kernel_out_size, 3))
    for i in range(kernel_out_size):
        for j in range(kernel_out_size):
            sect = layer_0[j * STRIDE:KERNEL_SIZE + j * STRIDE, i * STRIDE:KERNEL_SIZE + i * STRIDE]
            res = (sect * kernels).sum(1).sum(0)
            kernel_output[i, j] = res

    img = Image.new(mode="RGB", size=(kernel_out_size, kernel_out_size))
    for i in range(kernel_out_size):
        for j in range(kernel_out_size):
            out = [0, 0, 0]
            for k in range(3):
                out[k] = abs(int(math.sin(kernel_output[i, j, k]) * 255))
            img.putpixel((i, j), tuple(out))
    img.show()
