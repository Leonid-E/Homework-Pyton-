# Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону (т.е. не меньше 
# заданного минимума и не больше заданного максимума)

from random import randint
list_length = int(input('Задайте длину списка : '))
min_max_range = (input('Минимальное и максимальное значение диапазона : '))
new_min_max_range = "".join(min_max_range.split()) 
min = int (new_min_max_range [0])
max = int (new_min_max_range [1])
first_list = [randint(0,10) for i in range(list_length)]
print(f'Основной список : {first_list}')
print(f'Инлексы элементов заданного диапазона : ')
for i in range (len(first_list)):
    if first_list[i] >= min and first_list[i] <= max:
        print (f'{i}', end= " ")