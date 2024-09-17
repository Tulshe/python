# Задача - 1
# Запросите у пользователя имя, фамилию, email. Теперь необходимо совершить проверки, имя и фамилия должны иметь
# заглавные первые буквы.
# email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре, допускается нижнее
# подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net),
# te_4_st@test.com - верно указан.


import re

while True:
    name = input('Enter your name. It must contain first capital letter: ')
    pattern = '[A-Z][a-z]*'
    if re.match(pattern, name):
        break
while True:
    surname = input('Enter your surname. It must contain first capital letter: ')
    pattern = '[A-Z][a-z]*'
    if re.match(pattern, surname):
        break
while True:
    email = input('Enter your email. It must contain small letters only, may include _ and numbers. Domens must be '
                  '.ru .com .org: ')
    pattern = '[a-z_0-9]+@[a-z]+\.(ru|org|com)'
    if re.match(pattern, email):
        break

print(name, surname, email)
