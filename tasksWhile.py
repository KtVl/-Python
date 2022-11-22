# вывод чисел от 0 до 100

number = 0

while number <= 100:
    print(number)
    # number = number+1
    number += 1


# вывод чисел от 0 до n

number = 0
n = int(input('введите число n: '))

while number <= n:
    print(number)
    number += 1

# вывод четных чисел от 0 до n

number = 0
n = int(input('введите число n: '))

while number <= n:
    if number % 2 ==0: # если делится на 2 без остатка. для неч !=
        print(number)
    number += 1