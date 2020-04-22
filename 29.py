'''
Знайти кількість парних елементів одновимірного масиву до першого
зустрінутого числа рівного наперед заданому числу а.
'''
import numpy as np

a = int(input('Enter your number: '))
A = np.random.randint(1, 10, 15)
c = 0
for i in A:
    while i != a:
        if i % 2 == 0:
            c += 1
        break
    else:
        break
print(A)
print(c)
