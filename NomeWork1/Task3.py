#3. Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).
#- x=34; y=-30 -> 4
#- x=2; y=4-> 1
#- x=-34; y=-30 -> 3

x = int(input('Введите координату X: '))
y = int(input('Введите координату Y: '))
if (x > 0 and y > 0):
    print('Координаты точки лежат в первой четверти плоскости')
elif (x > 0 and y < 0):
    print('Координаты точки лежат в четвертой четверти плоскости')
elif (x < 0 and y > 0):
    print('Координаты лежат во второй четверти плоскости')
elif (x < 0 and y < 0):
    print('Координаты точки лежат в третьей четверти плоскости')
else:
    print('Точка лежит на оси')