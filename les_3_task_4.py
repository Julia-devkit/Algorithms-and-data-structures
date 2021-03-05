# В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
my_list = []

for i in range(2, 10):
    my_list.append([i, 0])

for item in my_list:
    cnt = 0
    for num in range(2, 100):
        if num % item[0] == 0:
            cnt += 1
    item[1] = cnt
    print(f'В диапазоне от 2 до 99 числу {item[0]} кратно {cnt} чис.')
