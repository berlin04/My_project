import os

print("Добро пожаловать в 'Файловый менеджер'")
print()

while True:
    print("Список доступных команд")
    print("/create-----создать новый файл")
    print("/delete-----удалить файл")
    print("/change-----внести изменения в файл")
    print("/rename-----переименовать файл")
    print("/exit-------выход")
    print()
    cmd=input("Введите команду:")
    if cmd=="/create":             ###########создать
        file_name=input("Введите название файла:")
        file_format=input("Введите формат файла:")
        
        if file_name=='' or file_format=='':
            print("Мы не сможем создать файл с пустым названием или форматом!\n")
        else:
            try:
                file=open(f"{file_name}.{file_format}","x")
                print(f"Файл '{file_name}.{file_format}' успешно создан!\n")
            except:
                print(f"Файл '{file_name}.{file_format}' уже существует!\n")
            file.close()



    elif cmd=="/delete":          ############удалить
        file_del=input("Введите полное название файла вместе с форматом:")
      
        try:
            os.remove(file_del)
            print(f"Файл '{file_del}' успешно удален!\n")
        except:
            print(f"Файл '{file_del}' не существует!\n")
    


    elif cmd=="/change":           ###########изменить
        file_change=input("Введите полное название файла вместе с форматом:")        
        
        try:
            file_read=open(f"{file_change}",'r')
            print()
            print("1)Перезаписать файл")
            print("2)Дозаписать файл")
            print("3)Очистить файл\n")
            num=int(input("Выберите пункт:"))
            if num==1:
                text=input("Введите текст которую вы хотите записать:")
                file_p=open(f"{file_change}",'w')
                file_p.write(f"\n{text}")
                print(f"Ваш текст успешно записан в файл '{file_change}'\n")
                file_p.close()
            elif num==2:
                text2=input("Введите текст которую вы хотите записать:")
                file_d=open(f"{file_change}",'a')
                file_d.write(f"\n{text2}")
                print(f"Ваш текст успешно записан в файл '{file_change}'\n")
                file_d.close()
            elif num==3:
                file_o=open(f"{file_change}",'w')
                file_o.write('')
                print(f"Файл '{file_change}' успешно очищен!")
                file_o.close()
            else:
                print("Ошибка, только от 1 до 3!\n")
        except:
            print(f"Файл '{file_change}' не существует!\n")
        file_read.close()
        
        
    
    elif cmd=="/rename":                   ##########переименовать
        old_file_name=input("Введите старое название файла:")
        new_file_name=input("Введите новое название файла:")
        if old_file_name=='' or new_file_name=='':
            print("Мы не сможем переименовать файл с пустым названием и форматом!\n")
        else:
            try:
                os.rename(old_file_name,new_file_name)
                print(f"Файл '{old_file_name}' успешно переименован на '{new_file_name}'!\n")
            except:
                print(f"Файл '{old_file_name}' не найден!\n")
           
            
    
    elif cmd=="/exit":        #############################выход
        print("GOODBYE!")
        break
    
    else:
        print("У нас нет такой команды!\n")



    
