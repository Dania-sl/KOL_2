'''
Створіть масив з 15 цілочисельних елементів і визначте серед них
мінімальне значення.
'''
import numpy as np

X = np.random.randint(0, 30, 15)
print(X)
print(min(X))
