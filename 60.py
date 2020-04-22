'''
Дан одновимірний масив з 10 цілих чисел. Підрахуйте найбільше число
однакових чисел, що йдуть підряд в ньому.
'''
import numpy as np

A = np.random.randint(0, 5, 10)
c = 1
t = 0
x = 0
for i in A:
    for j in range(1, len(A)):
        if i == A[j]:
            c += 1
            if c > t:
                t = c
                x = t
        else:
            c = 0
            x = 0
print(A)
print(t)
