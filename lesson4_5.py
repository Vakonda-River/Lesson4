from functools import reduce

my_list = [el for el in range(100,1001) if el % 2 == 0]
print('Генерируем список чётных чисел от 100 до 1000.')
print(my_list)

fool_num = reduce(lambda x, y: x * y, my_list)
print('Получаем сумашедшее число путем произведения всех чисел списка.')
print(fool_num)
