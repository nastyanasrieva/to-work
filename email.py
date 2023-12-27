import openpyxl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

# Путь к файлу Excel
excel_file_path = 'C:/Users/Admin/Desktop/mail.xlsx'

# Загрузка данных из Excel
wb = openpyxl.load_workbook(excel_file_path)
sheet = wb.active

# Получение адресов электронной почты
email_column = 'Почта'
emails = [row[0] for row in sheet.iter_rows(min_row=2, max_col=1, values_only=True) if row[0]]

# Путь к открытке
image_path = 'C://Users...'

# SMTP настройки
smtp_server = 'smtp.mail.ru'
smtp_port = 587
smtp_username = '.....'
smtp_password = '......'

# Отправка открыток
for email in emails:
    try:
        # Создание сообщения
        message = MIMEMultipart()
        message['From'] = smtp_username
        message['To'] = email
        message['Subject'] = 'Название'

        # Добавление текста в сообщение
        text = MIMEText('Название')
        message.attach(text)

        # Добавление изображения в сообщение
        with open(image_path, 'rb') as image_file:
            image = MIMEImage(image_file.read(), name='Картинка.png')
            message.attach(image)

        # Отправка сообщения
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.sendmail(smtp_username, email, message.as_string())

        print(f'Письмо на адрес {email} успешно отправлено.')

    except smtplib.SMTPRecipientsRefused:
        print(f'Письмо на адрес {email} не отправлено. Некорректный адрес или ящик недоступен.')

    except Exception as e:
        print(f'Произошла ошибка при отправке письма на адрес {email}: {e}')

print('Отправка завершена.')
