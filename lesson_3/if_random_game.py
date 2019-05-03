import random
x=random.randint(1,4)
y=int(input('Введите целое число от 1 до 4\n'))
if x==y:
    print('Победа!')
elif y>x:
    print('Загаданное число меньше')
else: print('Загаданное число больше')