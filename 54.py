'''
Введіть масив з 20 елементів і визначте, чи є в ньому елементи з
однаковими значеннями.
'''
import numpy as np

t = False
A = np.random.randint(0, 20, 20)
A_2 = np.unique(A, return_counts=True)
for i in A_2[1]:
    if i > 1:
        t = True
print(A)
print(t)
