import re

while True:
    email = input("Введите Вашу почту: ")
    login = input("Введите Ваш логин: ")
    if re.match(r'^[a-zA-Z0-9_\.\-]+@\w+\.\w+$', email) and re.match(r'^[a-zA-Z0-9_\.\-\@]+$', login):
        users_list = open('users_list.txt', 'a', encoding='utf-8')
        users_list.write(email + ', ' + login + '\n')
        users_list.close()
        exit()
    elif re.match(r'^[a-zA-Z0-9_\.\-]+@\w+\.\w+$', email) is None:
        print("Вы ввели не почту, введите данные заново")
    else:
        print("Вы ввели недопустимый логин, введите данные заново")