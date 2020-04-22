'''
Задано два натуральних числа a і b. Змінній w привласнити значення
істина, якщо в одновимірному цілочисельному масиві є хоча б один елемент, кратний а
і не кратний b.
'''
import numpy as np

w = False
a = int(input('Enter number 1: '))
b = int(input('Enter number 2: '))
A = np.random.randint(1, 20, 15)
for i in A:
    if A % a == 0 and A % b != 0:
        w = True
print(A)
print(w)
