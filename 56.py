'''
Якщо в одновимірному масиві є три поспіль однакових елемента, то
змінній r привласнити значення істина.
'''
import numpy as np

A = np.random.randint(0, 5, 20)
c = 0
r = False
for i in A:
    for j in range(2, len(A)):
        if i == A[j]:
            c += 1
            if c >= 3:
                r = True
        else:
            c = 0
print(A)
print(r)
