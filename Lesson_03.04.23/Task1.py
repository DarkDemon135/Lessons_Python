import random
n = int(input("Введите размер массива: "))
mas = []
s = 1
sum2 = 0
sum1 = 0
sumneg = 0
sumelem = 0
mas = [random.randint(-100,100) for i in range(n)]
print(mas)
for i in mas: 
    if (i%2) == 0:
        sum2 += i
    else:
        sum1 += i
for i in mas: 
    if i < 0:
        sumneg += i
print("Сумма четных: ",sum2)
print("Сумма нечетных: ", sum1)
print("Сумма отрицательных: ", sumneg)
print("Максимальное значение в массиве: ", max(mas))
print("Минимальное значение в массиве: ", min(mas))
print("Сумму элементов, находящихся между первым и по-следним положительными элементами: ", sum(mas[min(a := [i for i in range(len(mas)) if mas[i] > 0], default=0):max(a, default=-1) + 1]))