'''
У будинку, що складається з 30 квартир, переселити мешканців так, щоб
мешканці першої квартири переїхали в тридцяту, з тридцятого - в першу, з другої - в 29
і т.д., знайдіть кількість квартир, в яких проживає більше 5 осіб.
'''
import numpy as np
from random import randint


A = np.array([[i, randint(1, 8)] for i in range(1, 31)])
x = len(A) // 2
print(A)
for i in range(len(A)):
    if x > 0:
        A[i][1], A[len(A)-i-1][1] = A[len(A)-i-1][1], A[i][1]
        x -= 1
print(A)
