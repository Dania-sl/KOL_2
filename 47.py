'''
У лінійному масиві знайти максимальний елемент. Вставте порядковий
номер елемента за ним, пересунувши всі залишилися на одну позицію вправо.
'''
import numpy as np

A = np.random.randint(10, 50, 15)
print(A)
max = max(A)
for i in range(len(A)):
    if max == A[i]:
        ind = i
        A = np.insert(A, i + 1, ind)
        break
print(ind)
print(A)
