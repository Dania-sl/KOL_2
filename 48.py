'''
Наведено список прізвищ брокерів товарної біржі з N чоловік. Поміняйте
місцями прізвища брокерів: першого і останнього, другого і передостаннього, третього
з початку і третього від кінця і т.д.
'''
n = int(input('enter number:'))
A =[]
for i in range(n):
    A.append(input('enter second name:'))
print(A)
x = n // 2
for i in range(n):
    if n % 2 == 0 and x > 0:
        A[i], A[len(A)-i-1] = A[len(A)-i-1], A[i]
        x -= 1
    elif n % 2 == 1 and x-1 >= 0:
            A[i], A[len(A)-i-1] = A[len(A)-i-1], A[i]
            x -= 1
print(A)

