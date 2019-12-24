from pandas import read_csv
def recod_base(c,k):
    """Использует существующий валс файл и перекодирует базу, используя столбец index"""
    df=read_csv('{}.csv'.format (c) , encoding = 'utf-8' , sep = ';',dtype = str )
    df_vals=read_csv('{}.csv'.format(k), encoding='utf-8',sep=';')
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
    df.to_csv( '{}_encode.csv'.format(c) , sep=';' , index=False )#записывает полученный валс в файл
    if __name__ == "__main__":
        print("Модуль должен быть импортирован")