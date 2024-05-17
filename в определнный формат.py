import re

# Часть кода для обработки исходного файла и создания new.txt
file = 'C:/Users/Admin/Desktop/test.txt'
with open(file, encoding='utf-8') as f:
    contents = f.read()
    
    # Удаляем цифры и буквы в начале строк вместе с их знаками
    contents = re.sub(r'^\s*[\d]+[.\)]\s*|^\s*[а-яА-ЯёЁ]\)\s*', '', contents, flags=re.MULTILINE)
    
    # Удаляем все точки и точки с запятой
    contents = re.sub(r'[.;]', '', contents)
    
    # Заменяем символ + на = во всех строках
    contents = re.sub(r'\+', '=', contents)
    
    # Удаляем начальные буквы и символы в подстроках после начального удаления цифр и точек
    contents = re.sub(r'\s*[а-яА-ЯёЁ]\)\s*', '', contents)

with open('new.txt', 'w', encoding='utf-8') as f2:
    f2.write(contents)

# Часть кода для открытия файла new.txt и перемещения = в начало строк
with open('new.txt', 'r', encoding='utf-8') as f:
    new_contents = f.readlines()
    
    # Находим все строки, где знак = находится в конце и перемещаем его в начало
    new_contents = [re.sub(r'([^=]*)(\s*=\s*)\n', r'\2\1\n', line) for line in new_contents]

with open('new.txt', 'w', encoding='utf-8') as f:
    f.write(''.join(new_contents))
