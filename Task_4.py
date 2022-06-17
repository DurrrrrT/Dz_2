# Написать программу преобразования десятичного числа в двоичное
number = int(input())
final = ''
 
while number > 0:
    final = str(number % 2) + final
    number = number // 2
print(final)