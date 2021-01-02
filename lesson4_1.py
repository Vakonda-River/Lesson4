import less4myfunc

name = input('Укажите имя и фамилию сотрудника: ')
hour = float(input('Введите выработку в часах: '))
rate = float(input('Введите размер почасовой ставки: '))
prize = float(input('Если предусмотрено, введите размер премии: '))

w = round(less4myfunc.wage(hour,rate),2)
w_p = w + prize
print(name,', основная заработная плата, начислено:',w,'руб. Премия:',prize,'руб. Итого к выплате:', w_p,'руб. ')