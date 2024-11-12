#Написать программу, которая:
#- Создаёт с помощью генератора списков,
#список случайных целых чисел от **-50** до **50** размером **25** элементов.
#- Находит количество положительных, отрицательных и нулевых элементов в списке.
#- Выводит значения и их (*положительных, отрицательных и нулевых*) количество
#вместе с процентом от общего количества.
#- Выводит самое большое и самое маленькое значение
import random
list=[]
for _ in range(25):
    number = random.randrange(-50,50)
    list.append(number) 
print(list)
minus=0
plus=0
zero=0
for i in list:
    if i==0:
        zero+=1
    if i<0:
        minus+=1
    if i>0:
        plus+=1
# Вычисляем проценты
total = len(list)
minus_percent = (minus / total) * 100
plus_percent = (plus / total) * 100
zero_percent = (zero / total) * 100

# Выводим результаты
print(f"Количество отрицательных чисел в списке: {minus} ({minus_percent:.2f}%)")
print(f"Количество положительных чисел в списке: {plus} ({plus_percent:.2f}%)")
print(f"Количество нулей в списке: {zero} ({zero_percent:.2f}%)")
       
         
max_list=max(list)
min_list=min(list)
# Выводим результаты
print(f"Минимальное число в списке: {min_list}")
print(f"Максимальное число в списке: {max_list}")
