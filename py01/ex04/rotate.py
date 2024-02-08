from load_image import ft_load
from numpy import array, swapaxes
from matplotlib import pyplot as plt


def rotate(image: array) -> array:
    ret = array(image, dtype=int)
    ret = ret.reshape(ret.shape[0], ret.shape[1])
    print(f"New shape after Transpose: ({ret.shape[0]}, {ret.shape[1]})")
    return ret


def main():
    image = ft_load("animal.jpeg", 400, 400, 1)
    print(image)
    image = rotate(image)
    print(image)
    plt.imshow(swapaxes(image, 0, 1), cmap="gray")
    plt.show()
    return


if __name__ == "__main__":
    main()
