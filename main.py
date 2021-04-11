import math


def square_dist(dx, dy):
    if dx > 500:
        dx = 1000 - dx
    if dy > 500:
        dy = 1000 - dy
    return dy * dy + dx * dx  # Возвращает квадрат перемещения оси.


# Вычисление ближайшего перемещения координатной оси.
def final_distance(dx, dy):
    if dx > 500:
        dx = 1000 - dx
    if dy > 500:
        dy = 1000 - dy
    dy /= 1000
    dx /= 1000
    return math.sqrt(dy * dy + dx * dx)


count_of_targets = int(input())  # Количество целей задаваемое пользователем.
delta_table = []  # Таблица приращений до ближайшего целого.
# Создание нулевой матрицы.
for i in range(1000):
    column = [0] * 1000
    delta_table.append(column)

max_element = 0  # Максимальное количество попаданий, идёт в output.
current_min_dist = 0  # Держит квадрат значения текущей максимальной
# дистанции перемещения оси.
max_y = 0  # Конечные дельты перемещения нуля координат по осям.
max_x = 0

for i in range(count_of_targets):
    x, y = input().split()
    x_coord_of_targets = x.split('.')  # Разделение координаты на две строки
    # без плавающей точки.
    y_coord_of_targets = y.split('.')

    delta_x = int(x_coord_of_targets[1])  # Берётся именно дробная часть,
    # с которой и будем работать.
    delta_y = int(y_coord_of_targets[1])

    if x[0] == '-':  # Проверка на отрицательное число, точнее начинается ли
        # строка с целой частью с 0.
        delta_x = 1000 - delta_x  # Так из-за того что отрицательное число
        # по модулю не равно отрицательному без модуля.
        if delta_x == 1000:
            delta_x = 0

    if y[0] == '-':
        delta_y = 1000 - delta_y
        if delta_y == 1000:
            delta_y = 0
            
    delta_table[delta_y][delta_x] += 1  # Количество совпадений,
    # записывается в таблицу дельт по координатам этих дельт.

    if delta_table[delta_y][delta_x] > max_element:  # Т.е из-за отличия в
        # построении таблицы и оси.
        max_element = delta_table[delta_y][delta_x] # Новый максимальный элемент
        current_min_dist = square_dist(delta_y, delta_x)
        max_x = delta_x
        max_y = delta_y
    elif delta_table[delta_y][delta_x] == max_element:
        now_range = square_dist(delta_y, delta_x)
        if now_range < current_min_dist:
            current_min_dist = now_range
            max_y = delta_y
            max_x = delta_x

print(max_element, round(final_distance(max_x, max_y), 5))
