'''
Дані про температуру повітря за декаду грудня зберігаються в масиві.
Визначити, скільки раз температура була вище середньої за цю декаду.
'''
import numpy as np

X = np.random.randint(-17, 2, 31)
c = 0
n = 0
print(X)
for i in X:
    n += i
mid = n//len(X)
for i in range(len(X)):
    if X[i] > mid:
        c += 1
print(c)
