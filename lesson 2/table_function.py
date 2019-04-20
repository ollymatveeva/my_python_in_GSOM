atomic_number=input('Введите атомный номер: ')
if atomic_number:
    atom_num=int(atomic_number)
    if atom_num==3:
        print ('Элемент Li\nЛитий')
    elif atom_num==25:
        print('Элемент Mn\nМарганец')
    elif atom_num==80:
        print('Элемент Hg\nРтуть')
    elif atom_num==17:
        print('Элемент Cl\nХлор')
else: print('Мой бот такого элемента не знает :(')