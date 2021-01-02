import random

n = int(input('Генерируем целые случайные числа от 0 до (укажите):'))
m = int(input('Укажите количество элементов в генерируемом списке:'))
my_list = [random.randint(0,n) for i in range(m)]
print(my_list)
print('Удаляем повторяющиеся элементы и выводим список')

mnl = [my_list[el] for el in range(len(my_list)) if my_list.count(my_list[el])==1]

print(mnl)
