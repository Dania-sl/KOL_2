'''
Обчислити середнє арифметичне значення тих елементів одновимірного
масиву, які розташовані за першим по порядку мінімальним елементом.
'''
import numpy as np

A = np.random.randint(10, 50, 15)
min = min(A)
for i in range(len(A)):
    if min == A[i]:
        ind = i
        break
print(ind)
print(A)
print(f'{np.mean(A[ind: len(A)]):.2f}')
