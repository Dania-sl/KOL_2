'''
Знайти суму всіх елементів масиву дійсних чисел, більших за задане
число. Розмірність масиву - 20. Заповнення масиву здійснити випадковими числами
від 50 до 100.
'''
import numpy as np

n = int(input('Enter yor number: '))
X = np.random.randint(50, 100, 20)
s = 0
for i in X:
    if i > n:
        s += i
print(X)
print(s)
