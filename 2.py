'''
Введіть з клавіатури п'ять цілочисельних елементів масиву X. Виведіть на
екран значення коріння і квадратів кожного з елементів масиву.
'''
import numpy as np

while True:
    X = np.zeros(5, dtype=int)  # створкння списку з 5 елементів
    while True:
        try:
            for i in range(len(X)):
                n = int(input(f'Enter {i} number: '))
                X[i] = n  # ініціалізація елементів списку
            break
        except ValueError:
            print('Enter correct value')

    for i in range(len(X)):  # послідовний переьір всіх елементів
        sq_1 = X[i] ** 0.5  # знаходження корення
        sq_2 = X[i] ** 2  # знаходження квадрата
        print(f' roof number {X[i]} = {sq_1: .2f}, square = {sq_2: .2f}')
    if input('If you want continue press Enter') != '':
        break
