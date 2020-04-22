'''
Змінній t привласнити значення істина, якщо максимальний елемент
одновимірного масиву єдиний і не перевищує наперед заданого числа а.
'''
import numpy as np

a = int(input('Enter number:'))
s = 0
A = np.random.randint(-5, 5, 10)
m = max(A)
t = False
for i in A:
    if i == m:
        s += 1
    else:
        if m < a and s == 1:
            t = True
print(A)
print(t)
