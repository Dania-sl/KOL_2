'''
Дан лінійний масив цілих чисел. Перевірте, чи є він упорядкованим по
спаданню.
'''
import numpy as np

A = np.zeros(10)
for i in range(len(A)):
    A[i] = int(input('Enter element: '))
c = True
l = len(A)
for i in range(l - 1):
    min = i
    for j in range(i + 1, l):
        if A[j] < A[min]:
            min = j
            c = False
print(A)
print(c)
