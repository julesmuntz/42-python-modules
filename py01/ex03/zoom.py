from load_image import ft_load
from numpy import array
from matplotlib import pyplot as plt


def zoom(image: array, height: int, width: int, channels: int) -> array:
    """Zooms into the image based on the provided dimensions and channel(s)"""
    ret = array(image, dtype=int)
    ret = ret[:height, :width, :channels]
    print(f"New shape after slicing: {ret.shape} or ({height}, {width})")
    return ret


def main():
    image = ft_load("animal.jpeg")
    print(image)
    image = zoom(image, 400, 400, 1)
    print(image)
    plt.imshow(image, cmap="gray")
    plt.show()
    return


if __name__ == "__main__":
    main()
