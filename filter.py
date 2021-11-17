from PIL import Image
import numpy as np


def read(filename):
    img = Image.open(filename)
    return np.array(img)


def get_average(array, start_x, start_y, delta):
    return np.mean(array[start_x:start_x + delta, start_y:start_y + delta])


def fill_array(array, start_x, start_y, delta, value):
    array[start_x:start_x + delta, start_y:start_y + delta] = np.array(3 * [value])


def make_image_gray(array, puzzle_size, grayscale):
    max_x = len(array)
    max_y = len(array[1])

    for x in range(0, max_x, puzzle_size):
        for y in range(0, max_y, puzzle_size):
            average = get_average(array, x, y, puzzle_size)
            fill_array(array, x, y, puzzle_size, int(average // grayscale) * grayscale)


def write(array, filename):
    res = Image.fromarray(array)
    res.save(filename)


if __name__ == "__main__":
    try:
        print("введите название картинки, которую нужно изменить:")
        read_name = input()
        print("введите название файла, куда созранять картинку:")
        write_name = input()
        print("введите два числа через запятую в таком формате:\nразмер мозайки, градация серого")
        a, b = map(int, input().split(','))
        arr = read(read_name)
        make_image_gray(arr, a, b)
        write(arr, write_name)
        print(f"измененая картинка({read_name}) находится в {write_name}")
    except:
        print("нет картинки, которую нужно изменить, или нет такого файлика, куда нужно ее сохранять, или вы ввели "
              "числа не в том формате")
