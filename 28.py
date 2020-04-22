'''
Знайти кількість парних елементів одновимірного масиву.
'''
import numpy as np

A = np.random.randint(10, 200, 15)
c = 0
for i in A:
    if i % 2 == 0:
        c += 1
print(A)
print(c)
