# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.

a = int(input('Введите день недели: '))

if 1 <= a <= 5:
   print("Рабочий")

else:
   print("Выходной")
