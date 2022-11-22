import math
from random import randint

# Задача 1. Дано натуральное число N. Найдите значение выражения: N + NN + NNN
# N может быть любой длины.
# N (132) = 132 + 132132 + 132132132 = 132264396

def String_StringString(): 

    N=input("Введите число N: ")
    str_list = list()

    
    # Для варианта в соответствии с условием задачи.
    str_list = [N, N+N, N+N+N]

    # Сделанный изначально вариант в котором количество элементов равнялось бы N.
    # counter = int(N)
    # N_dlya_izmeneniy = str(N)
    # i = 0
    # while i != counter:
    #     N_dlya_vneseniya = N_dlya_izmeneniy
    #     str_list.append(N_dlya_vneseniya)
    #     N_dlya_izmeneniy = (N_dlya_izmeneniy+N)
    #     i = i+1


    print(f'Получаем список из {len(str_list)} элементов:  {str_list}')
    
    int_list = [int(el) for el in  str_list]
    print (f'Сумма всех элементов списка = {sum(int_list)}')
    print()

String_StringString()


# Задача 2. Задан массив из случайных цифр на 15 элементов. На вход подаётся трёхзначное натуральное число. 
# Напишите программу, которая определяет, есть в массиве последовательность из трёх элементов, совпадающая с введённым числом.
# [0, 5, 6, 2, 7, 7, 8, 1, 1, 9] - 277 -> да
# [4, 4, 3, 6, 7, 0, 8, 5, 1, 2] - 812 -> нет



arr = [randint(1,9) for n in range (15)]
print(f'Cформирован список {arr}')

while True:
    number = input("Введите трехзначное число: ")
    if not number.isdigit():
        print("Вы ввели не число. Попробуйте снова: ")
    elif not 100 <= int(number) <= 999:
        print("Ваше число не является трехзначным. Попробуйте снова")
    else:
        # print(f"Число {number} прошло проверку.")
        number = int(number)
        break

def sequence_search(arr, number):
    result = bool(0)
    for i in range(len(arr) - 2):
        if int("".join(str(x) for x in arr[i:i + 3])) == number:
            result = bool(1)
    return result

def print_result(result):
    print(f'Содержит ли список {arr} в себе число {number}? -> {result}')

print_result(sequence_search(arr, number))
print()

# Задача 3. Найдите все простые несократимые дроби, лежащие между 0 и 1, знаменатель которых не превышает 11.

def simple_fraction():

    list_of_fractions = []
    for i in range(2, 12):
        for j in range(1, i):
            if math.gcd(i, j) == 1:
                list_of_fractions.append(f"{j}/{i}")
                # print(f"{j}/{i}", end=", ")
    print(' Список простых несократимых дробей, лежащих между 0 и 1, знаменатель которых не превышает 11:')
    print(list_of_fractions)

simple_fraction()    