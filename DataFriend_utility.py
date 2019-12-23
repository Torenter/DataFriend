import address
import disintegration
import get_vals
import update
import recode

def instruct():
    """Выводит на экран инструкцию"""
    print('''
    0- Выйти из программы
    1- создать новый vals файл
    2- обновить существующий vals файл
    3- перекодировать базу используя vals
    4- Разобрать xlsx файл на vars и vals
    ''')

ask = None
while ask!=0:
    instruct()
    ask=int(input('введите действие: '))
    if ask==1:
        c = address.address(ask)
        get_vals.get_vals(c)
    elif ask==2:
        c,k = address.address(ask)
        update.update_vals(c,k)
    elif ask==3:
        c,k = address.address(ask)
        recode.recod_base(c,k)
    elif ask==4:
        a = address.address(ask)
        disintegration.disintegration(a)
    elif ask==0:
        break
    else:
        print('введено некоректно')
        continue