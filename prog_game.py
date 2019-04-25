n=int(input('Введите число от 1 до 4: '))
import random
random_num=random.randint(1,4)
if n==random_num:
    print('Победа')
else: print('Попрробуйте ещё раз!')