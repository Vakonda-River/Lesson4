from itertools import count
from math import factorial

def gen_f():
    for i in count(1):
        yield factorial(i)

generat = gen_f()

n = int(input('Введите число для расчета факториала:'))
x = 0
for k in generat:
    if x < n:
        print('Факториал от "',x+1,'" =',k)
        x += 1
    else:
        break











