# 5 В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.
import random

SIZE = 10
MIN_ITEM = -500
MAX_ITEM = 500

array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

array_neg = []

for i, val in enumerate(array):
    if array[i] < 0:
        array_neg.append((i, array[i]))

max_array_neg = array_neg[-1][-1]
max_neg_pos = -1

for i in array_neg:
    if i[1] > max_array_neg:
        max_array_neg = i[1]
        max_neg_pos = i[0]

print(f'Максимальный отрицательный элемент: {max_array_neg} на {max_neg_pos}-м месте ')
