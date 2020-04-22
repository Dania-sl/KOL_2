'''
Дані про температуру повітря і кількості опадів за декаду квітня
зберігаються в масивах. Визначити кількість опадів, що випали у вигляді дощу і у
вигляді снігу за цю декаду.
'''
import numpy as np
from random import randint

s = 0
r = 0
A = np.array([[randint(0, 20), randint(-3, 18)] for i in range(30)])
for i in A:
    if i[0] > 0 and i[1] > 0:
        r += 1
    elif i[0] > 0 and i[1] <= 0:
        s += 1
print(A)
print(s)
print(r)
