# Задача 18: Требуется найти в массиве A[1..n] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число n – количество элементов в массиве. 
# В последующих  строках записаны n целых чисел Ai. Последняя строка содержит число X

# *Пример:*
# 5
#     1 2 3 4 5
#     6
#     -> 5


n = int(input("Введите количество элементов массива "))
A = []
print(f'Введите {n} чисел массива ')
for i in range(n):
    A.append(int(input()))
print(A)

X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
min = abs(X - A[0])
index = 0
for i in range(1, n):
    count = abs(X - A[i])
    if count < min:
        min = count
        index = i
print(f'Число {A[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A[index])}')