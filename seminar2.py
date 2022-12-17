# Задача 0. Дано число N. Найти все его делители. Для каждого делителя укажите чётный он или нечётный.

def even_or_odd(number):
    # if number % 2 == 0:
    #     return 'чётное число'
    # else:
    #     return 'нечётное число'
    return 'чётное число' if not number % 2 else 'нечётное число'

def zadacha0():
    number = 60
    for divider in range(1, number//2 + 1):
        if number % divider == 0:
            print(f'{divider} - {even_or_odd(divider)}')

        
    print(f'{number} - {even_or_odd(number)}')


# Форматирование строк при выводе со всякими фишками, вроде типов данных, выделенного места под строку и вот этим вот всем
# Срезы строк и шаг срезов
# Тип генератор и как с ним бороться
# Многочлены и операции с ними
# list1 = [float(input()) for _ in range(int(input()))]
# list1 = [input() for _ in range(int(input()))]
# вот этот код можно подробно объяснить)что за чем тут следует
# Что такое бот? Как его создать и "наделить" интеллектом?


#Задача 1. Выведите таблицу истинности для выражения ¬ X ∨ Y.

#  не X или Y
#  X |  Y  | не X  |не X или Y
#  0 |  0  |  1    |   1
#  0 |  1  |  1    |   1
#  1 |  0  |  0    |   0
#  1 |  1  |  0    |   1

def zadacha1():
    print(f'X   |\tY   |\t¬X ∨ Y')
    for x in range(0, 2):
        for y in range(0, 2):
            print(f'{x}   |\t{y}   |\t {int(not x or y)}')



#Задача 2. Напишите программу, в которой пользователь будет задавать две строки,
# а программа - определять количество вхождений одной строки в другую.

def zadacha2():
    phrase = 'Банкиров ребрендили-ребрендили-ребрендили, да не выребрендировали'
    substring = 'ребренд'
    length = len(substring)
    count = 0

    result = ''
    for index in range(len(phrase)-length+1):
        # for i in range(index, index+length):
        #     result += phrase[i]
        # if substring == result:
        #     count += 1
        # result = ''
        if substring == phrase[index : index+length]:
            count += 1

    print(phrase)
    print(f'подстрока "{substring}" встречается {count} раз(-а)')
    print(phrase)
    print(f'подстрока "{substring}" встречается {phrase.count(substring)} раз(-а)')


hello = 'привет'
result = []
step = 3
for ind in range(0, len(hello)-1, step):
    result.append(hello[ind:ind+step])

print(result)