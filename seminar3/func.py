def read_last_row(name):
    data = open(name, encoding='utf-8')
    rows = data.readlines()
    data.close()
    # with open(name, encoding='utf-8') as data:
    #     rows = data.readlines()

    #<_io.TextIOWrapper name='text.txt' mode='r' encoding='utf-8'>

    # w r a   w+  r+  a+
    data = open('counts.txt', mode='r+', encoding='utf-8')
    number = int(data.readlines()[-1]) + 1
    number = f'{number}\n'
    data.writelines(number)
    data.close()
    print(rows[-1])


def print_hello_world():
    print("привет, мир!")