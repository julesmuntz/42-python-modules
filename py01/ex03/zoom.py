from load_image import ft_load
from numpy import ndarray as array
from PIL import Image
from matplotlib import pyplot as plt


def zoom(path: str, height: int, width: int, channels: int) -> array:
    try:
        image = Image.open(path)
    except FileNotFoundError:
        return "File not found"
    ret = array(shape=(height, width, channels), dtype=int)
    for y in range(0, width):
        for x in range(0, height):
            ret[x, y] = image.getpixel((y, x))[:channels]
    plt.imshow(ret, cmap='gray')
    plt.show()
    return (
        "New shape after slicing: ("
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


def main():
    print(ft_load("animal.jpeg"))
    print(zoom("animal.jpeg", 400, 400, 1))
    return


if __name__ == "__main__":
    main()
