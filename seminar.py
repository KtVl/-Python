from random import randint as ri

def power(number):
    return number * number

def zadacha0():
    #Напишите программу, которая на вход принимает число и выдаёт его квадрат (число умноженное на само себя).
    number = int(input('Введите число: '))
    print(f'{number} * {number} = {power(number)}')


def zadacha1():
    # 1. Напишите программу, которая на вход принимает два числа и проверяет, является ли одно число квадратом другого.
    number_first = input('Введите первое число: ')
    if number_first.isdigit():
        #number_first = int(number_first)
        try:
            number_first = int(number_first)
        except ValueError:
            number_first = float(number_first)


    number_second = int(input('Введите второе число: '))

    if number_first == power(number_second) or number_second == power(number_first):
        print('одно число является квадратом другого')
    else:
        print('ни одно число не является квадратом другого')

def zadacha2():
    #2. Организуйте последовательный ввод чисел до тех
    # пор, пока не будет введён 0. Подсчитайте среди введённых чисел те, которые кратны трём.

    number = None
    count = 0
    while number !=0:
        try:
            number = int(input('Введите число: '))
            if number % 3 == 0:
                count+=1
        except ValueError:
            print('неверный ввод')
    print(f'пользователь ввёл {count - 1} чисел, кратных трём')

def zadacha3():
    #3. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
    number = ri(5, 10)
    print(f'выпало число {number}')

    for i in range(-number, number+1):
        print(i, end=' ')

def zadacha4():
    # 4. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
    #number = float(input())
    number = 234.99678
    #   int/int = int
    print(int(number % 1 * 10))
    print(int(number * 10) % 10)
    number = round(number, 3)
    print(number)

#5. Напишите программу, которая находит наибольшее и наименьшее число из списка значений

numbers = [5, 2, 8, 1, -1, 0, 4, 3]
max_n = numbers[0]
min_n = numbers[0]

for el in numbers:
    if el > max_n:
        max_n = el
    elif el < min_n:
        min_n = el

print(f'максимальное значение {max_n}')
print(f'минимальное значение {min_n}')
print(f'максимальное значение {max(numbers)}')
print(f'минимальное значение {min(numbers)}')

max_n = numbers[0]
min_n = numbers[0]
index_max = 0
index_min = 0
print(range(len(numbers)))
for i in range(len(numbers)):
    if numbers[i] > max_n:
        max_n = numbers[i]
        index_max = i
    elif numbers[i] < min_n:
        min_n = numbers[i]
        index_min = i
print(f'максимальное значение {max_n} находится на позиции {index_max+1}')
print(f'минимальное значение {min_n} находится на позиции {index_min+1}')