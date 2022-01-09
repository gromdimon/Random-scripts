import numpy as np


#Тензор первого порядка
#f = np.array([1, 2, 3])
#s = np.array([3, 3, 3])
#m = f * s
#print(m, np.dot(f, s))


#Тензор второго порядка
f = input('Первая строка (2 числа): ')
s = input('Вторая строка (2 числа): ')
sq = input('Строка второй мартрица (2 числа): ')

first = np.array( [[int(x) for x in f.split(' ')],
           [int(x) for x in s.split(' ')]] )
second = np.array( [int(x) for x in sq.split(' ')])
ssum = first + second
razn = first - second
multiplying = first * second
print('Операции с тензором 2-го порядка:\n')
print('Произведение:\n', multiplying, '\nСумма\n', ssum, '\nРазница\n', razn, '\nСвертывание:\n',np.dot(first, second))


print('\n\n\nВыполнение операций с тензорами 3-го порядка:\n')
# Тензор третьего порядка
first_tensor = np.arange(12).reshape(2, 2, 3)
second_tensor = np.arange(12).reshape(2, 3, 2)

# Выполнение умножения
multiplying_tensor = np.tensordot(first_tensor, second_tensor, axes=2)
print('Произведение: \n', multiplying_tensor)

# Выполнение свертки
convolution_tensor = np.dot(first_tensor, second_tensor)
print('Свертывание: \n', convolution_tensor)