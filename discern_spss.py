import savReaderWriter as sav
import pandas as pd
from numpy import nan
def spss_to_vals(c):
    l=c[:-4]
    with sav.SavHeaderReader(c, ioUtf8=True) as header:
        metadata = header.all()
        labels = metadata.valueLabels#получает в итоге словарь в словаре
    q={}#
    for k,v in labels.items():#итерируемся по словарю, где k-первый клуюч, v-вложенный словарь
        q[k]=[list(labels[k].keys())]#копируем первый ключ как ключ, а все ключи вложенных словарей засовываем в список и добавляем под ключ
        cus_list=[]#список в который будут собпаны все значения из под вложенных словарей на данном шаге итерации
        for cus_keys in labels[k]:#берем значение из вложенного словаря
            cus_list.append(labels[k][cus_keys])#добавляем в список
        q[k].append(cus_list)#добавляем список тем самым сохраням последовательность где список - это столбец в vals
    df= pd.DataFrame(q)
    df=df.T.reset_index()
    df.columns = ['variable', 'index', 'values']
    df=df.apply(pd.Series.explode)
    ffinv = lambda s: s.mask(s == s.shift())
    df=df.assign(variable=ffinv(df['variable']))
    df['Df_metr']=nan
    df['restrict_W']=nan
    df['total div']=nan
    df.to_csv( '{}_vals.csv' .format(l), sep=';' , index=False )
    if __name__ == "__main__":
        print("Модуль должен быть импортирован")