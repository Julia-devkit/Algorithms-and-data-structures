# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
SIZE_N = 5
SIZE_M = 4

print(f'Заполните матрицу целыми числами, количество значений в строке: {SIZE_M - 1}.')
matrix = [[int(i) for i in input('Введите значения для текущей строки через пробел: ').split()] for _ in range(SIZE_N)]

for line in matrix:
    sum_line = 0
    for j in line:
        sum_line += j
    line.append(sum_line)

for line in matrix:
    for val in line:
        print(f'{val:<5}', end='')
    print()
