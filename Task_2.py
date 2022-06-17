# Найти произведение пар чисел в списке. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.


my_list = [2, 3, 5, 6, ]
new_list = []
mid_element = len(my_list)//2 + len(my_list) % 2
for i in range(mid_element):
    mult = my_list[i] * my_list[len(my_list)-1-i]
    new_list.append(mult)
print(new_list)
