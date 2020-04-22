'''
У лотереї розігрувалося 100 квитків. Таблиця містить 10 номерів
виграшних квитків. Перевірте, чи є квиток з номером N виграшним.
'''
import numpy as np

t = False
n = int(input('enter number: '))
A = np.random.randint(0, 100, 100)
A_2 = np.random.randint(0, 100, 10)
if n in A and n in A_2:
    t = True
print(A)
print(A_2)
print(t)
