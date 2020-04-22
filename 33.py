'''
Заданий масив А (1:20). Знайти добуток всіх його ненульових елементів.
'''
import numpy as np

A = np.random.randint(-5, 5, 20)
t = 1
for i in A:
    if i != 0:
        t *= i
print(A)
print(t)
