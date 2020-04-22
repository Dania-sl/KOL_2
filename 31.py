'''
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які потрапляють в інтервал від -2 до 10.
'''
import numpy as np

A = np.random.randint(-8, 20, 15)
A_2 = np.array([])
for i in A:
    if -2 < i < 10:
        A_2 = np.append(A-2, i)
print(A)
print(f'{np.mean(A_2):.2f}')
