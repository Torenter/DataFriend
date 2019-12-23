import pandas as pd
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
    if __name__ == "__main__":
        print("Модуль должен быть импортирован")