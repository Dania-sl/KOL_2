'''
Відомість на зарплату представлена як дві таблиці. Одна містить
прізвища працівників цеху, а друга - їх зарплату за поточний місяць. Знайдіть прізвище
працівника, зарплата якого найменш відхиляється від середньої зарплати всіх
працівників за поточний місяць. Знайдіть прізвища двох працівників з найбільшою
заробітною платою. Видаліть з відомості на зарплату відомості про працівника,
зарплата якого мінімальна.
'''
import copy

l_n = ['Слободянюк', 'Васильченко', 'Опонасюк', 'Юрчук', 'Коврижних', 'Рощенюк', 'Cорокопуд', 'Редич']
l_p = [12000, 15000, 13300, 9800, 9300, 13100, 8400, 11000]
print(l_p)
s = max(l_p) + 1  # введемо значення найбільше за максимальну зарплату
for i in l_p:  # цикл для підрахунку суми всіх заробітніх плат для визначення середньої
    s += i
m = s / 8
for i in range(len(l_p)):
    x = m - l_p[i]  # різниці між середньою заробітньою платою і заробітньою платою працівника
    if x < 0:  # перевірка на відємність одержаного числа
        x = x * -1  # якщо при віднімані від середньої зарплати, зарплату робітника ми одережемо відємне число
        # то ця стрічка перетворить його в натуральне
        if s > x:  # перевірка чи більша різниці між середньою зарплатою і зарплатою робіника
            s = x  # після проходження перевірки записується найменша різниця між середньою зарплатою і зарплатою робітника
    elif x > 0:
        if s > x:  # перевірка чи більша різниці між середньою зарплатою і зарплатою робіника
            s = x  # після проходження перевірки записується найменша різниця між середньою зарплатою і зарплатою робітник
    else:  # умова для перевірки, якщо середня зарплата співпаде з зарплатою робітника
        if s > x:  # перевірка чи більша різниці між середньою зарплатою і зарплатою робіника
            s = x  # після проходження перевірки записується найменша різниця між середньою зарплатою і зарплатою робітник
ind = l_p.index(m - s)  # знаходимо індекс робітника заробітня плата якого найменше відхиляється від середньої
# віднімаємо від середньої найменшу різниую між зарплатами

l_p2 = copy.deepcopy(l_p)  # робимо копію списку
max_1 = max(l_p2)  # знаходимо максимальне значеня перше
l_p2.remove(max_1)  # видаляєио перше максимальне значення
max_2 = max(l_p2)  # знаходимо друге максимальне значення

min = min(l_p)  # знаходимо мінімальне значення
l_p.remove(min)

print(l_n[ind])
print(l_n[l_p.index(max_1)])  # знаходимо індекс першої максимальної зарпалти і використовуємо для знаходження фамілії
print(l_n[l_p.index(max_2)])  # знаходимо індекс другої максимальної зарпалти і використовуємо для знаходження фамілії
print(l_p)