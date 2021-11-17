from PIL import Image
import numpy as np


def read(filename):
    img = Image.open(filename)
    return np.array(img)


def write(array, filename):
    res = Image.fromarray(array)
    res.save(filename)


def make_image_gray(array, puzzle_size, grayscale):
    rowsCount = len(array)
    colsCount = len(array[1])

    for i in range(0, rowsCount, puzzle_size):
        for j in range(0, colsCount, puzzle_size):
            average = 0
            for row in range(i, i + puzzle_size):
                for col in range(j, j + puzzle_size):
                    r = array[row][col][0]
                    g = array[row][col][1]
                    b = array[row][col][2]
                    average += (r + g + b) // 3
            average = int(average // (puzzle_size * puzzle_size))
            for row in range(i, i + puzzle_size):
                for col in range(j, j + puzzle_size):
                    array[row][col][0] = int(average // grayscale) * grayscale
                    array[row][col][1] = int(average // grayscale) * grayscale
                    array[row][col][2] = int(average // grayscale) * grayscale


if __name__ == "__main__":
    arr = read("img2.jpg")
    make_image_gray(arr, 10, 50)
    write(arr, "res.jpg")
