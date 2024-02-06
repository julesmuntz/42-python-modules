from numpy import ndarray as array
from PIL import Image


def ft_load(path: str) -> array:
    try:
        image = Image.open(path)
    except FileNotFoundError:
        return "File not found"
    width, height = image.size
    ret = array(shape=(height, width, 3), dtype=int)
    for y in range(0, width):
        for x in range(0, height):
            ret[x, y] = image.getpixel((y, x))
    return (
        "The shape of image is: ("
        + str(height)
        + ", "
        + str(width)
        + ", 3)\n"
        + str(ret)
    )
