import numpy as np


#Тензор первого порядка
#f = np.array([1, 2, 3])
#s = np.array([3, 3, 3])
#m = f * s
#print(m, np.dot(f, s))

#Тензор второго порядка
#first = ( [[0, 1],
#         [2, 3]] )
#second = ( [4, 5] )
#multiplying = first + second
#print(multiplying, np.dot(first, second))

# Тензор третьего порядка
first_tensor = np.arange(12).reshape(2, 2, 3)
second_tensor = np.arange(12).reshape(2, 3, 2)

# Выполнение умножения
multiplying_tensor = np.tensordot(first_tensor, second_tensor, axes=2)
print(multiplying_tensor)

# Выполнение свертки
convolution_tensor = np.dot(first_tensor, second_tensor)
print(convolution_tensor)