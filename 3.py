'''
Створіть масив з п'яти прізвищ і виведіть їх на екран стовпчиком,
починаючи з останнього.
'''
import numpy as np

X = np.array(['Слободянюк', 'Васильченко', 'Опанасюк', 'Юрчук', 'Рощенюк'])  # створкння списку з 5 елементів
for i in np.flip(X):
    print(i)