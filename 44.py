'''
Підрахуйте кількість елементів одновимірного масиву, які збігаються зі
своїм номером і при цьому кратні 3.
'''
import numpy as np

s = 0
A = np.random.randint(1, 20, 15)
for i in range(len(A)):
    if i == A[i] and A[i] % 3 == 0:
        s += 1
print(A)
print(s)
