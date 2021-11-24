from PIL import Image
import numpy as np
import doctest


def read(filename: str):
    """

    :param filename: название файла
    :return: np массив от фотографии с именем filename
    """
    img = Image.open(filename)
    return np.array(img)


def get_average(array: np.array, start_x: int, start_y: int, delta: int):
    """

    :param array: np массив
    :param start_x: координата x
    :param start_y: координата y
    :param delta: смещение по x и y
    :return: среднее значение в массиве в диапазоне start_x<=x<start_x+delta, start_y<=y<start_y+delta

    >>> get_average(np.array([[1, 1, 1], [1, 1, 1]]), 0, 0, 1)
    1.0
    >>> get_average(np.array([[1, 1, 1], [1, 1, 1]]), 0, 0, 3)
    1.0
    >>> get_average(np.array([[1, 2, 3], [1, 2, 3]]), 0, 0, 3)
    2.0
    """
    return np.mean(array[start_x:start_x + delta, start_y:start_y + delta])


def fill_array(array: np.array, start_x: int, start_y: int, delta: int, value: float):
    """
    :param array: np массив
    :param start_x: координата x
    :param start_y: координата y
    :param delta: смещение по x и y
    :param value: значение для array[x][y][0], array[x][y][1], array[x][y][2] диапазона start_x<=x<start_x+delta,
    start_y<=y<start_y+delta

    """
    array[start_x:start_x + delta, start_y:start_y + delta] = np.array(3 * [value])


def make_image_gray(array: np.array, puzzle_size: int, grayscale: float):
    """
    :param array: np массив
    :param puzzle_size: размер блока
    :param grayscale: градация серого

    """
    max_x = len(array)
    max_y = len(array[1])

    for x in range(0, max_x, puzzle_size):
        for y in range(0, max_y, puzzle_size):
            average = get_average(array, x, y, puzzle_size)
            fill_array(array, x, y, puzzle_size, int(average // grayscale) * grayscale)


def write(array: np.array, filename: str):
    """

    :param array: np массив
    :param filename: название файла, куда произойдет запись результата
    """
    res = Image.fromarray(array)
    res.save(filename)


if __name__ == "__main__":
    doctest.testmod()
    try:
        print("введите название картинки, которую нужно изменить:")
        read_name = input()
        print("введите название файла, куда сохранять картинку:")
        write_name = input()
        print("введите два числа через запятую в таком формате:\nразмер мозаики, градация серого")
        a, b = map(int, input().split(','))
        arr = read(read_name)
        make_image_gray(arr, a, b)
        write(arr, write_name)
        print(f"измененная картинка({read_name}) находится в {write_name}")
    except SyntaxError:
        print("нет картинки, которую нужно изменить, или нет такого файлика, куда нужно ее сохранять, или вы ввели "
              "числа не в том формате")
