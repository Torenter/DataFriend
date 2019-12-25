import pandas as pd
def update_vals(c,k):
    """Используется для обновления валса на основании новой базы в которой есть новые столбцы/строки"""
    df_vals = pd.read_csv('{}.csv'.format(k), encoding='utf-8',sep=';')
    df = pd.read_csv('{}.csv'.format (c) , encoding = 'utf-8' , sep = ';', low_memory=False)
    df = df.select_dtypes ( include = 'object' ) # Берет из базы только столбцы со строками
    df = df.fillna ( 'Nin' )#Забивает пустые ячейки словом
    a = df.columns.tolist()#получает список из названий столбов базы
    x={}#словарь на который разбирается база
    for i in a:#берет название столба
        x[i]=df[i].unique().tolist()# Добавляет название как ключь и подсовывает под него все уникальные значения из столбца
    df_vals['variable']=df_vals['variable'].ffill()
    recode=df_vals.groupby('variable').agg(lambda row: list(row))
    recode.reset_index(level=0, inplace=True)
    q={}# Словарь на который разбирается валс файл
    for col in recode.index:#смотрим в название столбца,он является индексом
            variable=recode.loc[col]['variable']
            values=recode.loc[col]['values']
            Df_expr=recode.loc[col]['Df_expr']
            Df_metr=recode.loc[col]['Df_metr']
            restrict_W=recode.loc[col]['restrict_W']
            q[variable]=[values,Df_expr,Df_metr,restrict_W]
    for i in x:# Взять ключь из словаря для базы
        if i in q:#Проверка наличия такого же ключа в словаре из валс файла
            for e in x[i]:#Итерация по значениям ключей словаря для базы, если этого значения нет под ключем из словаря для валса,то добавляет его 
                if e=="Nin":#
                    continue
                else:
                    if e in q[i][0]:#
                        continue
                    else:
                        q[i][0].append(e)#добавление нехватающего значения.
        else:
            q[i]=[x[i]]#Если ключь не был найдет, то он добавляется в словарь для валса со всеми значениями
    final_frame = pd.DataFrame({'variables': [], 'index': [], 'valuess': [], 'Df_expr': [], 'Df_metr': [], 'rectrict_W': []})

    row = 0
    for cus_key, columns in q.items():
        final_frame.loc[row, 'variables'] = cus_key
        for enum, data_row in enumerate(columns[0]):
            final_frame.loc[row, final_frame.columns[2]] = data_row
            for inner_enum, column in enumerate(columns[1:]):
                if len(column) >= (enum+1):
                    final_frame.loc[row, final_frame.columns[inner_enum + 3]] = column[enum]
            final_frame.loc[row, final_frame.columns[1]] = int(enum + 1)
            row += 1

    final_frame.dropna(inplace=True, how='all')
    final_frame.astype({'index': 'int32'})
    final_frame.to_csv( '{}_update.csv' .format(k), sep=';' , index=False )
if __name__ == "__main__":
    print("Модуль должен быть импортирован")