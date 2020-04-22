'''Дано два лінійних масиву однакової розмірності. Скласти третій масив з
добутку елементів перших двох масивів, що стоять на місцях з однаковим індексом.'''
import numpy as np

A = np.random.randint(-5, 15, 20)
A_2 = np.random.randint(0, 20, 20)
B = np.array([])
for i in range(len(A)):
    B = np.append(B, A[i]*A_2[i])
print(A)
print(A_2)
print(B)
