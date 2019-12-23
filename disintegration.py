import pandas as pd
def disintegration(a):
    """Берет листы Values и Variables из существующего лейаута и записывает их в отдельные файлы с нужной кодировкой и разделителем"""
    for i in a: 
        df_vals = pd.read_excel("{}.xlsx".format(i),sheet_name='VALUES')
        df_vars = pd.read_excel("{}.xlsx".format(i),sheet_name='VARIABLES')
        df_vals.to_csv( "{}_vals.csv".format(i), sep=';' , encoding='utf-8', index=False )
        df_vars.to_csv( "{}_vars.csv".format(i), sep=';' , encoding='utf-8', index=False )
if __name__ == "__main__":
    print("Модуль должен быть импортирован")