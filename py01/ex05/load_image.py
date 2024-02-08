from numpy import array
from PIL import Image


def ft_load(path: str) -> array:
    try:
        image = Image.open(path)
    except FileNotFoundError:
        return "File not found"
    ret = array(image)
    print(f"The shape of image is: {ret.shape}")
    print(ret)
    return ret
