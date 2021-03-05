# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 1_000

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

max_pos = 0
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

array[min_pos], array[max_pos] = array[max_pos], array[min_pos]

print(array)
print(f'Элементы поменялись местами на {min_pos}ой и {max_pos}ой позициях')
