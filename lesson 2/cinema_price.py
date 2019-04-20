movie=str(input('Выберете фильм: "Пятница", "Чемпионы", "Пернатая банда"\n'))
date=input('Выберете дату: сегодня или завтра\n')
if movie=="Пятница":
    print('Выберете время (12, 16, 20):')
elif movie=='Чемпионы':
    print('Выберете время (10, 13, 16):')
elif movie=='Пернатая банда':
    print('Выберете время (10, 14, 18):')
time=int(input())
print('Сколько билетов вы хотите купить?')
tiсket=int(input())
if movie=='Пятница':
    if time==12:
        price=250
    elif time==16:
        price=350
    elif time==20:
        price=450
elif movie=='Чемпионы':
    if time==10:
        price=250
    elif time==13:
        price=350
    elif time==16:
        price=350
elif movie=='Пернатая банда':
    if time==10:
        price=350
    elif time==14:
        price=450
    elif time==18:
        price=450
else: print('Ошибка')
allprice=tiсket*price
if date=='завтра':
    allprice=allprice*0.95
if tiсket>19:
    allprice=allprice*0.8
print('Итоговая сумма:',allprice)