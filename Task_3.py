# В заданном списке вещественных чисел найдите разницу между максимальным
# и минимальным значением дробной части элементов.


import math


def difference(numbers):
    min = max = round(math.modf(numbers[0])[0], 2)
    for number in numbers:
        num = round(math.modf(number)[0], 2)
        if max < num:
            max = num
        if num != 0 and min > num:
            min = num
    return max - min


list = [1.1, 1.2, 3.1, 5, 10.01]
print(f"Разница между максимальным и минимальным = {difference(list)}")
