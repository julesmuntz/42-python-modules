from numpy import array, copy
from matplotlib import pyplot as plt


def ft_invert(array) -> array:
    """Inverts the color of the image received."""
    ret = copy(array)
    ret[:, :, 0] = 255 - ret[:, :, 0]
    plt.imshow(255 - array)
    plt.show()
    return ret


def ft_red(array) -> array:
    """Sets to red the color of the image received."""
    ret = copy(array)
    ret[:, :, 1:] = 0
    plt.imshow(ret)
    plt.show()
    return ret


def ft_green(array) -> array:
    """Sets to green the color of the image received."""
    ret = copy(array)
    ret[:, :, [0, 2]] = 0
    plt.imshow(ret)
    plt.show()
    return ret


def ft_blue(array) -> array:
    """Sets to blue the color of the image received."""
    ret = copy(array)
    ret[:, :, :2] = 0
    plt.imshow(ret)
    plt.show()
    return ret


def ft_grey(array) -> array:
    """Sets to grey the color of the image received."""
    ret = copy(array)
    ret[:, :, 0] = ret[:, :, 1] = ret[:, :, 2] = ret.mean(axis=2, dtype=int)
    plt.imshow(ret)
    plt.show()
    return ret
