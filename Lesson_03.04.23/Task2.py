from random import randint
n = int(input("Введите размер массива: "))
mas = [int(randint(-100, 100)) for i in range(n)]
chetnie = [int(i) for i in mas if i % 2 == 0]
nechetnie = [int(i) for i in mas if i % 2 != 0]
negative = [int(i) for i in mas if i  < 0]
positive = [int(i) for i in mas if i  > 0] 
print("Массив: ", mas)
print("Четные числа: ", chetnie)
print("Нечетные числа: ", nechetnie)
print("Отрицательные числа: ", negative)
print("Положительные числа: ", positive)