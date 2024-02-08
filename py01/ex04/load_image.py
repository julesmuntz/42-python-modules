from numpy import array
from PIL import Image


def ft_load(path: str, height: int, width: int, channels: int) -> array:
    try:
        image = Image.open(path)
    except FileNotFoundError:
        return "File not found"
    ret = array(image)
    ret = ret[:height, :width, :channels]
    print(f"The shape of image is: {ret.shape} or \
({ret.shape[0]}, {ret.shape[1]})")
    return ret
