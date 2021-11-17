from PIL import Image
import numpy as np


def read(filename):
    img = Image.open(filename)
    return np.array(img)


def get_average(array, start_x, start_y, delta):
    average = 0
    for x in range(start_x, start_x + delta):
        for y in range(start_y, start_y + delta):
            r = array[x][y][0]
            g = array[x][y][1]
            b = array[x][y][2]
            average += (r // 3 + g // 3 + b // 3)
    return int(average // (delta * delta))


def fill_array(array, start_x, start_y, delta, value):
    for x in range(start_x, start_x + delta):
        for y in range(start_y, start_y + delta):
            array[x][y][0] = value
            array[x][y][1] = value
            array[x][y][2] = value


def write(array, filename):
    res = Image.fromarray(array)
    res.save(filename)


def make_image_gray(array, puzzle_size, grayscale):
    max_x = len(array)
    max_y = len(array[1])

    for x in range(0, max_x, puzzle_size):
        for y in range(0, max_y, puzzle_size):
            average = get_average(array, x, y, puzzle_size)
            fill_array(array, x, y, puzzle_size, int(average // grayscale) * grayscale)


if __name__ == "__main__":
    arr = read("632.jpg")
    make_image_gray(arr, 1, 5)
    write(arr, "res.jpg")
