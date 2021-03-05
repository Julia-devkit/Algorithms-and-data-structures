# 6 В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 20

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_pos = len(array) - 1
min_pos = 0

array_min = array[0]
array_max = array[-1]

for i in range(len(array)):
    if array[i] > array_max:
        array_max = array[i]
        max_pos = i
    elif array[i] < array_min:
        array_min = array[i]
        min_pos = i

sum_ = 0

if min_pos < max_pos:
    for i in range(min_pos + 1, max_pos):
        sum_ += array[i]
else:
    for i in range(max_pos + 1, min_pos):
        sum_ += array[i]

print(
    f'Минимальный элемент {array_min} находится в {min_pos}ой ячейке,\nмаксимальный элемент {array_max} находится в  {max_pos}ой ячейке,\nсумма элементов между ними - {sum_}')
