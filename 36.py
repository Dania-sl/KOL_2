'''
Знайти суму додатніх елементів лінійного масиву цілих чисел.
Розмірність масиву - 10. Заповнення масиву здійснити з клавіатури.
'''
import numpy as np

A = np.zeros(10)
s = 0
for i in range(len(A)):
    A[i] = int(input('Enter element: '))
for i in A:
    if i > 0:
        s += i
print(A)
print(s)
