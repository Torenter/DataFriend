import savReaderWriter as sav
import pandas as pd
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
    final_frame = pd.DataFrame({'variable': [], 'index': [], 'values': [], 'Df_expr': [], 'Df_metr': [], 'restrict_W': []})

    row = 0
    for cus_key, columns in q.items():
        final_frame.loc[row, 'variable'] = cus_key
        for enum, data_row in enumerate(columns[0]):
            final_frame.loc[row, final_frame.columns[1]] = data_row
            for inner_enum, column in enumerate(columns[1:]):
                if len(column) >= (enum+1):
                    final_frame.loc[row, final_frame.columns[inner_enum + 2]] = column[enum]
            row += 1
    final_frame.dropna(inplace=True, how='all')
    final_frame.astype({'index': 'int64'})
    final_frame.to_csv( '{}_vals.csv' .format(l), sep=';' , index=False )
    if __name__ == "__main__":
        print("Модуль должен быть импортирован")