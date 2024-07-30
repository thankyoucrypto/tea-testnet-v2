import sqlite3
"""
Запустив данный скрипт вы получите список своих рефералок из valid_logins.txt
На эти рефералки можно загнать другие аккаунты
Реферальные ссылки сохранятся в файле valid_refs.txt
Для регистрации аккаунтов их указывать в config.py
"""


# Подключаемся к базе данных
conn = sqlite3.connect('accounts.db')
c = conn.cursor()

# Читаем логины из файла valid_logins.txt
with open('valid_logins.txt', 'r') as file:
    valid_logins = [line.strip() for line in file.readlines()]

# Создаем список для хранения refer_link
valid_refs = []

# Получаем refer_link для каждого логина из valid_logins
for login in valid_logins:
    c.execute('SELECT refer_link FROM accounts WHERE login=?', (login,))
    result = c.fetchone()
    if result:
        valid_refs.append(result[0])

# Записываем refer_link в файл valid_refs.txt
with open('valid_refs.txt', 'w') as file:
    for ref in valid_refs:
        if ref != None:
            file.write(ref + '\n')

# Закрываем соединение с базой данных
conn.close()
