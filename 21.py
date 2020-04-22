'''
Знайти добуток всіх елементів масиву дійсних чисел, менших заданого
числа. Розмірність масиву - 10. Заповнення масиву здійснити випадковими числами
від 50 до 100.
'''
import numpy as np

n = int(input('Enter yor number: '))
X = np.random.randint(50, 100, 10)
s = 1
for i in X:
    if i > n:
        s *= i
print(X)
print(s)
