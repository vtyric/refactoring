#Батуев Макар АТ-28

## Время работы:

### Время работы filter.py (26433 ms):

![filter.py](refactoring-tasks-images/new-filter.PNG)

### Время работы old-filter.py.py (1170 ms):

![old-filter.py](refactoring-tasks-images/old-filter.PNG)

### Время работы filter_with_filename.py (81 ms):

![filter_with_filename.py](refactoring-tasks-images/filter_with_filename.PNG)

### Объяснение результатов:

Самое большое время исполнения у первого фильтра, так там мы вводим данные с консоли. old-filter.py выполняет свою
задачу гораздо медленнее filter_with_filename.py. В исправленном фильтре я избавился от ручных циклов, переделал их в
матричные преобразования, что позволило повысить скорость выполнения кода.

## Тесты и документация:

### Пример теста:

![average-test](refactoring-tasks-images/average-test.PNG)

### Пример запуска правильного теста:

![complete-test](refactoring-tasks-images/complete-test.PNG)

### Пример неправильного теста:

![failed-test](refactoring-tasks-images/failed-test.PNG)

## Отладчик:

### Введенные данные:

![input-data](refactoring-tasks-images/input.PNG)

### Свойства и тип изображения:

![image-prop](refactoring-tasks-images/image-prop.PNG)

### Значения ширины блока и градации серого:

![grayscale-puzzle_size](refactoring-tasks-images/grayscale-puzzle_size.PNG)
