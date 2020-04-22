'''
Знайти найбільший елемент з елементів одновимірного масиву, що мають
парний номер. Визначити, чи є він єдиним.
'''
import numpy as np

A = np.random.randint(0, 20, 15)
A_2 = np.array([])
c = 0
t = True
for i in range(len(A)):
    if i % 2 == 0:
        A_2 = np.append(A_2, A[i])
for i in A_2:
    if i == max(A_2):
        c += 1
if c > 1:
    t = False

print(A)
print(A_2)
print(t)
