'''
Змінній t привласнити значення істина, якщо в одновимірному масиві є
хоча б одне від’ємне і парне число.
'''
import numpy as np

A = np.random.randint(-8, 20, 15)
for i in A:
    if i < 0 and i % 2 == 0:
        t = True
print(A)
print(t)
