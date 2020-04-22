'''
В масиві X (1: n) кожен елемент рівний 0, 1 або 5. Переставити елементи
масиву так, щоб спочатку розташовувалися всі нулі, потім все одиниці, а потім всі
п'ятірки. Додаткового масиву не заводити.
'''
import numpy as np
from random import choice

n = int(input('enter number: '))
l = [0, 1, 5]
A = np.array([choice(l) for i in range(n)])
print(A)
A = np.sort(A)
print(A)
