'''
Розсортуйте заданий лінійний масив по зростанню.
'''
import numpy as np

A = np.random.randint(-5, 15, 20)
print(A)
l = len(A)
for i in range(l - 1):
    min = i
    for j in range(i + 1, l):
        if A[j] < A[min]:
            min = j
    A[i], A[min] = A[min], A[i]
print(A)
