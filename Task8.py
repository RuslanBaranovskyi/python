# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
#     1 2 3 4 5
#     3
#     -> 1


n = int(input("Введите количество элементов массива "))
list_n = []
print(f'Введите {n} чисел массива ')
for i in range(n):
    list_n.append(input())
print(list_n)
x = (input('Введите число х: '))
count = 0
for i in range(n):
    if list_n[i] == x:
        count += 1
print(f'Число {x} встречается в списке А {count} раз.')