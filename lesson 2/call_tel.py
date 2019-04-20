code=int(input('Введите код города '))
time=int(input('Ввведите длительность звонка (в минутах) '))
if code==343:
    print('Екатеринбург\n',time*15,'рублей')
elif code==381:
    print('Омск\n',time*18,'рублей')
elif code==473:
    print('Воронеж\n',time*13,'рублей')
elif code==485:
    print('Ярославль\n',time*11,'рублей')
else: print('Введите другой код')