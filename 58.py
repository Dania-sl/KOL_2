'''
Дан одновимірний масив цілих чисел. Знайдіть, скільки разів в ньому
повторюється найчастіше число.
'''
import numpy as np

A = np.random.randint(0, 10, 25)
A_2 = np.unique(A, return_counts=True)
print(A)
print(max(A_2[1]))
