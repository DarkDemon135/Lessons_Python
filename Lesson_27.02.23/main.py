while True:
    x = int(input("Введите первое число: "))
    print("Выберите: ")
    print("Сложение +")
    print("Вычитание -")
    print("Умножение *")
    print("Деление /")
    print("Деление без остатка //")
    print("Нахождение остатка %")
    a = input()
    y = int(input("Введите второе число: "))
    if a == '+':
        print ("Ответ: ", x + y)
    if a == '-':
        print ("Ответ: ", x - y)
    if a == '*':
        print ("Ответ: ", x * y)
    if a == '/':
        if y == 0:
            print ("Ошибка")
        else:
            print ("Ответ: ", x / y)
    if a == '//':
        if y == 0:
            print ("Ошибка")
        else:
            print ("Ответ: ", x // y)
    if a == '%':
        if y == 0:
            print ("Ошибка")
        else:
            print ("Ответ: ", x % y)
    break