def address(ask):
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
if __name__ == "__main__":
    print("Модуль должен быть импортирован")