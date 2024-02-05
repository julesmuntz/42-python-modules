from numpy import ndarray as array
from PIL import Image
from matplotlib import pyplot as plt


def ft_load(path: str) -> array:
    image = Image.open(path)
    width, height = image.size
    ret = array(shape=(height, width, 3), dtype=int)
    for y in range(0, width):
        for x in range(0, height):
            ret[x, y] = image.getpixel((y, x))
    plt.imshow(ret)
    plt.show()
    return ret
