'''
Обчислити суму парних елементів одновимірного масиву до першого
зустрінутого нульового елемента.
'''
import numpy as np
s = 0
A = np.random.randint(-5, 5, 10)
for i in range(len(A)):
    if A[i] == 0:
        break
    else:
        s += A[i]
print(A)
print(s)
