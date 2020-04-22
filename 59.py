'''
Дан одновимірний масив з 10 цілих чисел. Підрахуйте кількість різних
чисел в ньому.
'''
import numpy as np

A = np.random.randint(0, 10, 10)
A_2 = np.unique(A, return_counts=True)
print(A)
print(len(A_2[0]))
