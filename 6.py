'''
Створіть масив А [1..8] за допомогою генератора випадкових чисел з
елементами від -10 до 10 і виведіть його на екран. Підрахуйте кількість від’ємних
елементів масиву.
'''
import numpy as np

X = np.random.randint(-10, 10, 8)
print(X)
c = 0
for i in X:
    if i < 0:
        c += 1
print(c)
