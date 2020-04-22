'''
Введіть з клавіатури в масив п'ять цілочисельних значень. Виведіть їх в
один рядок через кому. Отримайте для масиву середнє арифметичне.
'''
import numpy as np

while True:
    A = np.zeros(5, dtype=int)  # створкння списку з 5 елементів
    while True:
        try:
            for i in range(len(A)):
                n = int(input(f'Enter {i} number: '))
                A[i] = n  # ініціалізація елементів списку
            break
        except ValueError:
            print('Enter correct value')
    s = 0  # зміна для суми всіх елементів списку
    for i in range(len(A)):  # послідовний переьір всіх елементів
        s += A[i]
    m = s / len(A)  # знаходження середнього значення
    print(A)
    print(m)
    if input('If you want continue press Enter') != '':
        break
