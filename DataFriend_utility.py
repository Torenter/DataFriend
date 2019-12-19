import pandas as pd

def adres(ask):
    global c
    global k
    global a
    """Получает путь до базы и валса для передачи функциям обработчикам"""
    if ask == 1:
        c = input('Введите путь до базы. \nНапример: C:\\User\\admin\\Desktop\\DateBase\n')#Принимаемый ввод подставляется как путь
        return c
    elif ask == 2 or ask == 3:
        c = input('Введите путь до базы. \nНапример: C:\\User\\admin\\Desktop\\DateBase\n')#Принимаемый ввод подставляется как путь
        k = input ('Введите путь до Vals файла. \nНапример: C:\\User\\admin\\Desktop\\Data_vals\n')#Принимаемый ввод подставляется как путь
        return c, k
    elif ask == 4:
        a = input("ВВедите полный путь с указанием имени xlsx файла.\n Например:C:\\User\\DataBase \n Так же вы можете передать в таком форме несколько файлов через запятую \nНапример: C:\\User\\DataBase_1,C:\\User\\DataBase,C:\\User\\DataBase_2,C:\\User\\DataBase_3\n ")
        a = a.split(',')
        return a

def get_vals(c):
    """Разбирает базу и создает Vals файл"""
    df = pd.read_csv ( '{}.csv'.format (c) , encoding = 'utf-8' , sep = ';', low_memory=False)#открываем файл в УТФ-8 используя разделитель ";", отключено ограничение на использование памяти для более точного определения типа столбца
    df = df.select_dtypes ( include = 'object' )#усечения файла до столбцов содержащих только строковые значения
    df = df.fillna ( 'Nin' )#замена пропущенных значений в таблице на Nin
    a = df.columns.tolist()#получение списка содержащего названия всех столбцов
    k = pd.DataFrame ( columns= [ 'variable' , 'index' , 'values' ] )#создание пустого датафрейма,из которого создается валс
    e = 1 # при первой итерации встает на первую строку, потому что нулевой строки в экселе нет
    for i in a:#берез значение из списка с именами переменных
        k.loc [ e ,'variable' ] = i # записывает это значение в ячейку валса
        d = df[i].unique().tolist()#получение всех уникальных значений их столбцов
        o = 1 # проставление индексов от 1 и до бесконечности
        for l in d: #берет зачение из списка для запили его в ячейку
            if l == 'Nin':#проверка на условие
                continue#удаление всех Nin из валса
            k.loc [ e , 'values' ] = l # записывает значение, переходя каждый раз на следующую строку
            k.loc [ e ,'index' ] = o
            e += 1
            o += 1
    k.to_csv( '{}_vals.csv'.format(c) , sep=';' , index=False )#записывает полученный валс в файл

def update_vals(c,k):
    """Используется для обновления валс файл если появилась новая база с новыми столбцами и/или значениями"""
    df_vals=pd.read_csv('{}.csv'.format(k), encoding='utf-8',sep=';')
    df=pd.read_csv('{}.csv'.format (c) , encoding = 'utf-8' , sep = ';', low_memory=False)
    df = df.select_dtypes ( include = 'object' ) # Берет из базы только столбцы со строками
    df = df.fillna ( 'Nin' )#Забивает пустые ячейки словом
    a = df.columns.tolist()#получает список из названий столбов базы
    x={}#словарь на который разбирается база
    for i in a:#берет название столба
        x[i]=df[i].unique().tolist()# Добавляет название как ключь и подсовывает под него все уникальные значения из столбца
    df_vals = df_vals.fillna ( 'Nin' ) #Забивает пустые ячейки словом
    q={}# Словарь на который разбирается валс файл
    schotchik=0# Хз, куда его еще присунуть, но он должен быть инициализирован до итерации.
    s=[df_vals.loc[df_vals['variable']==elements].index[0] for elements in df_vals['variable'] if elements!='Nin']#Генератор, запускает цикл в котором сложенно условие, после выполнения которого используется извлечение индекса строки df_vals.loc[df_vals['variable']==elements].index[0]
    d=[i-1 for i in s]#использован генератор вместо обычного цикла
    d.append(len(df_vals.index))#добавление последнего индекса для последнего среза
    for elements in df_vals['variable']:# В цикле реализуется срез значений по индексу
        e=''# надо
        if elements!='Nin':#Проверка на условие
            e=df_vals['values'].loc[s[schotchik]:d[schotchik+1]].tolist()#получение среза по индексам
            q[elements]=e#Создание ключа со значениями
            schotchik+=1#реализует переход на следующий срез
        else:
            continue
    for i in x:# Взять ключь из словаря для базы
        if i in q:#Проверка наличия такого же ключа в словаре из валс файла
            for e in x[i]:#Итерация по значениям ключей словаря для базы, если этого значения нет под ключем из словаря для валса,то добавляет его 
                if e=="Nin":#
                    continue
                else:
                    if e in q[i]:#
                        continue
                    else:
                        q[i].append(e)#добавление нехватающего значения.
        else:
            q[i]=x[i]#Если ключь не был найдет, то он добавляется в словарь для валса со всеми значениями
    w = pd.DataFrame ( columns= [ 'variable' , 'index' , 'values' ] )#создание пустого датафрейма,из которого создается валс
    e = 1 # поставить курсор на первую строчку
    for key in q: # взять ключь из словаря
        w.loc [ e ,'variable' ] = key #записать ключ
        o=1 
        for l in q[key]: # взять значение по ключу получаемого на прошлом шаге
            w.loc [ e , 'values' ] = l #записать значение в ячейку
            w.loc [ e , 'index' ] = o #записать индекс для этого значения
            e += 1 #переставить курсов на строчку ниже
            o += 1 #нарастить индекс
    w.to_csv( '{}_update.csv' .format(k), sep=';' , index=False )

def recod_base(c,k):
    """Использует существующий валс файл и перекодирует базу, используя столбец index"""
    df=pd.read_csv('{}.csv'.format (c) , encoding = 'utf-8' , sep = ';',dtype = str )
    df_vals=pd.read_csv('{}.csv'.format(k), encoding='utf-8',sep=';')
    #Заполним пустые строки значениями переменной свыше. Вдруг пригодиццо
    df_vals['variable']=df_vals['variable'].ffill()#Берет и забивает пустые ячейки в первом столбце значением которое встретил, и забивает до следующего,как только встречает другое, то используе его
    # А давайте сгруппируем
    recode=df_vals.groupby('variable').agg(lambda row: list(row))#группирует всё так,что напротив названия столбца получается список с индексами и список со значениями
    # рекодим
    for col in recode.index:#смотрим в название столбца,он является индексом
        keys=recode.loc[col]['values']#Берем значение как ключ
        values=recode.loc[col]['index']#Берем инлекс как значение для ключа
        mapRecode = dict(zip(keys, values))#Запаковываем всё в словарь

        df[col].replace(mapRecode,inplace=True)#БЕрем столбец,название которого записанно в cоl и меняем его значения используя словарь. Ключ - это то,что нужно заменить, а значение под ключем - на что заменить 
    df.to_csv( '{}_encod.csv'.format(c) , sep=';' , index=False )#записывает полученный валс в файл

def disintegration(*arg):
    """Берет листы Values и Variables из существующего лейаута и записывает их в отдельные файлы с нужной кодировкой и разделителем"""
    for i in a: 
        df_vals = pd.read_excel("{}.xlsx".format(i),sheet_name='VALUES')
        df_vars = pd.read_excel("{}.xlsx".format(i),sheet_name='VARIABLES')
        df_vals.to_csv( "{}_vals.csv".format(i), sep=';' , encoding='utf-8', index=False )
        df_vars.to_csv( "{}_vars.csv".format(i), sep=';' , encoding='utf-8', index=False )

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
    c=None
    k=None
    a=None
    ask=int(input('введите действие: '))
    if ask==1:
        adres(ask)
        get_vals(c)
    elif ask==2:
        adres(ask)
        update_vals(c,k)
    elif ask==3:
        adres(ask)
        recod_base(c,k)
    elif ask==4:
        adres(ask)
        disintegration(a)
    elif ask==0:
        break        
    else:
        print('введено некоректно')
        continue