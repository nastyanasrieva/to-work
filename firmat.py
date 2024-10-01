import pandas as pd
import random

# Читаем файл Excel
file_path = 'list.xlsx'
df = pd.read_excel(file_path)

# Создаем словарь для хранения вопросов и соответствующих уникальных ответов
questions_dict = {}

# Проходим по строкам DataFrame
for index, row in df.iterrows():
    question = row['question']
    answer = row['answer']
    class_value = row['class']

    # Проверяем, есть ли вопрос в словаре, если нет, создаем новый список
    if question not in questions_dict:
        questions_dict[question] = set()  # Используем множество для уникальности

    # Определяем, какой маркер использовать для ответа
    if 'correct_answer' in class_value:
        marker = '='
    else:
        marker = '~'

    # Добавляем ответ с соответствующим маркером
    questions_dict[question].add(f"{marker}{answer}")

# Формируем выходной формат
output_lines = []
for question, answers in questions_dict.items():
    output_lines.append(f"{question} {{")
    
    # Превращаем множество в список и перемешиваем
    shuffled_answers = list(answers)
    random.shuffle(shuffled_answers)
    
    output_lines.extend(shuffled_answers)
    output_lines.append("}")
    output_lines.append("")  # Добавляем пустую строку после каждой группы

# Записываем результат в файл
output_file_path = 'formatted_questions.txt'
with open(output_file_path, 'w', encoding='utf-8') as f:
    f.write('\n'.join(output_lines))

print(f"Форматированный вывод сохранен в {output_file_path}.")
