from load_image import ft_load
from numpy import ndarray as array, swapaxes
from PIL import Image
from matplotlib import pyplot as plt


def rotate(path: str, height: int, width: int) -> array:
    try:
        image = Image.open(path)
    except FileNotFoundError:
        return "File not found"
    ret = array(shape=(height, width), dtype=int)
    for y in range(0, width):
        for x in range(0, height):
            ret[x, y] = image.getpixel((y, x))[0]
    plt.imshow(swapaxes(ret, 0, 1), cmap="gray")
    plt.show()
    return (
        "New shape after transpose: ("
        + str(height)
        + ", "
        + str(width)
        + ")\n"
        + str(ret)
    )


def main():
    print(ft_load("animal.jpeg", 400, 400, 1))
    print(rotate("animal.jpeg", 400, 400))
    return


if __name__ == "__main__":
    main()
