#1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
#- 6 -> да
#- 7 -> да
#- 1 -> нет

a = int(input('Введите число дня недели: '))
if (a == 6 or a == 7):
    print('Ура, сегодня выходной!')
elif (a < 1 or a > 7):
    print('Такого дня не существует')
else:
    print('Еще не выходной, работаем')