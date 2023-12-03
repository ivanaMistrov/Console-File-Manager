import os
import sys
from viktori import get_person, get_person_and_question
from my_balans import menu, User
def create_folder():
    name =input("Введите название папки :")
    os.mkdir(name)
    print(f"Папка {name} успешно создана.")
def delete_file_folder():
    name = input("Введите название папки :")
    if os.path.isfile(name):
        os.remove(name)
        print(f"Файл {name} успешно удален.")
    elif os.path.isdir(name):
        os.rmdir(name)
        print(f"Папка {name} успешно удален.")
    else:
        print(" нет таких ")
def copy_file_folder():
    name_folder = input("Введите название папки/файла :")
    new_name = input('укажи новое имя ')
    if  os.path.isfile(name_folder):
        with open(name_folder, 'rb') as f:
            content = f.read()
        with open(new_name, 'wb') as f:
            f.write(content)
        print(f"Файл {name_folder} успешно скопирован с именем {new_name}.")
    elif os.path.isdir(name_folder):
        os.mkdir(new_name)
        print(f"Папка {name_folder} успешно скопирована с именем {new_name}.")
    else:
        print("Данного файла или папки не существует.")
def working_direct():
    contents = os.listdir()
    for item in contents:
        print(item)


def folder ():
    n = os.listdir()
    for item in n:
        if os.path.isdir(item):
            print(item)
def file():
    n = os.listdir()
    for item in n:
        if os.path.isfile(item):
            print(item)

def change_working_dir():
    new_directory = input("Введите новую рабочую директорию: ")
    os.chdir(new_directory)
    print(f"Рабочая директория изменена на {new_directory}.")
def play_game():
    rounds = int(input('Сколько раз вы хотите играть?'))
    for i in range(rounds):
        get_person_and_question()
    print('Пока!')

def save_directory_contents():
    dir_path = os.getcwd()
    with open("listdir.txt", "w") as file:
        files = []
        folders = []
        for item in os.listdir(dir_path):
            if os.path.isfile(os.path.join(dir_path, item)):
                files.append(item)
            else:
                folders.append(item)


        file.write("Файлы:\n")
        for file_name in files:
            file.write(file_name + "\n")
        file.write("nПапки:\n")
        for folder_name in folders:
            file.write(folder_name + "\n")

    print("Содержимое рабочей директории сохранено в файл listdir.txt")




def games():
    while True:
        print("Меню:")
        print("1. Создать папку")
        print("2. Удалить (файл/папку)")
        print("3. Копировать (файл/папку)")
        print("4. Просмотр содержимого рабочей директории")
        print("5. Посмотреть только папки")
        print("6. Посмотреть только файлы")
        print("7. Просмотр информации об операционной системе")
        print("8. Создатель программы")
        print("9. Играть в викторину")
        print("10. Мой банковский счет")
        print("11. Смена рабочей директории")
        print("12. Выход")
        print("13.сохранить содержимое рабочей директории в файл")

        choice = input("Выберите пункт меню: ")

        if choice == "1":
            create_folder()
        elif choice == "2":
            delete_file_folder()
        elif choice == "3":
            copy_file_folder()
        elif choice == "4":
            working_direct()
        elif choice == "5":
            folder ()
        elif choice == "6":
            file()
        elif choice == "7":
            print('My OS is', sys.platform, '(', os.name, ')' ,os.getcwd())
        elif choice == "8":
            print('* ' *10 ,'VVM' ,'* ' *10)
        elif choice == "9":
            play_game()
        elif choice == "10":
            menu()
        elif choice == "11":
            change_working_dir()
        elif choice == "12":
            print("До свидания!")
            break
        elif choice == "13":
            save_directory_contents()
        else:
            print("Неверный пункт меню. Попробуйте снова.")
games()