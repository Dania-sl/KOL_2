'''
Дані про направлення вітру (північний, південний, східний, західний) і
силі вітру за декаду листопада зберігаються в масиві. Визначити, скільки днів дув
південний вітер з силою, що перевищує 8 м / с.
'''
import numpy as np
from random import choice
from random import randint

l = ["Північний ", "Південний", "Східний", "Західний"]
s = 0
A = np.array([[choice(l), randint(0, 40)] for i in range(10)])
for i in A:
    if int(i[1]) > 8:
        s += 1
print(A)
print(s)
