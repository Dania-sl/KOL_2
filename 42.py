'''
Підрахувати кількість елементів одновимірного масиву, для яких
виконується нерівність i*i<ai<i!
'''
import numpy as np
import math

s = 0
A = np.random.randint(1, 20, 15)
for i in range(len(A)):
    if i * i < A[i] < math.factorial(i):
        s += 1
print(A)
print(s)
