# Надо много лямбд. когда в них есть смысл?
# Многочлены и операции с ними
# list1 = [float(input()) for _ in range(int(input()))]
# list1 = [input() for _ in range(int(input()))]
# вот этот код можно подробно объяснить)что за чем тут следует
# Как отрабатывать лямбды, когда они принимаются в функцию в качестве аргумента, а вторым аргументом список или  список списков например? как должно прописываться действие внутри списка
# Можно бы ещё про однострочники, ну всё эти мапы, фильтры и тд, т. е. по третьей лекции, а то там всё в куче, не усваивается с таким подходом

# def ink(number):
#     number += 5
#     return number

# f = lambda number: number + 5

# numbers = [4, -1, 3, 0]
# for i in range(len(numbers)):
#     numbers[i] = ink(numbers[i])
# print(numbers)

# result = map(lambda x: x + 5 if x % 2 == 0 else x, numbers)
# result = list(result)
# print(result)

# str_list = [['абв', 'авг'], ['абд'], ['авг']]

# result = filter(lambda x, i: 'аб' in str(x[i]), str_list)
# result = list(result)
# print(result)





list1 = [i+5 for i in range(10)]
print(list1)

list1 = (i for i in range(10))
print(list1)