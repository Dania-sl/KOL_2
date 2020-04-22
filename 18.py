'''
Знайти добуток всіх елементів масиву цілих чисел, менших 0. Розмірність
масиву - 10. Заповнення масиву здійснити за допомогою клавіатури.
'''
import numpy as np

X = np.zeros(10, dtype=int)
for i in range(len(X)):
    X[i] = int(input(f'enter {i+1} element: '))
s = 1
for i in X:
    if i < 0:
        s *= i
print(X)
print(s)
