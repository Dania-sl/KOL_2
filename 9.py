'''
З 8 до 20 години температура повітря вимірювалася щогодини. Відомо,
що протягом цього часу температура знижувалася. Визначте, о котрій годині було
вперше зафіксовано від'ємну температуру.
'''
import numpy as np

X = np.random.randint(-5, 8, 12)
X = np.sort(X)
X = np.flip(X)
for i in range(len(X)):
    if X[i] < 0:
        ind = i
print(X)
print(f'at {i} o`clock')
