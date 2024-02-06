from numpy import ndarray as array
from PIL import Image


def ft_load(path: str, height: int, width: int, channels: int) -> array:
    try:
        image = Image.open(path)
    except FileNotFoundError:
        return "File not found"
    ret = array(shape=(height, width, channels), dtype=int)
    for y in range(0, width):
        for x in range(0, height):
            ret[x, y] = image.getpixel((y, x))[:channels]
    return (
        "The shape of image is: ("
        + str(height)
        + ", "
        + str(width)
        + ", "
        + str(channels)
        + ") or ("
        + str(height)
        + ", "
        + str(width)
        + ")\n"
        + str(ret)
    )
