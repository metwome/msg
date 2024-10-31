import sqlite3
import time

def create_database():
    """Создает базу данных и таблицу для хранения сообщений."""
    connection = sqlite3.connect('msg.db')  # Создаем соединение с базой данных
    cursor = connection.cursor()  # Создаем курсор для выполнения операций

    # Создаем таблицу, если она еще не создана
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            text TEXT,
            unix_time REAL
        )
    ''')

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

def add_msg(username, text):
    """Добавляет новое сообщение в базу данных с текущим временем."""
    connection = sqlite3.connect('msg.db')
    cursor = connection.cursor()

    # Получаем текущее время в формате UNIX с плавающей точкой
    unix_time = time.time()

    # Вставляем данные о сообщении
    cursor.execute('INSERT INTO messages (username, text, unix_time) VALUES (?, ?, ?)', (username, text, unix_time))

    # Сохраняем изменения и закрываем соединение
    connection.commit()
    connection.close()

def get_all_msg_by_username(username):
    """Возвращает все сообщения от данного пользователя."""
    connection = sqlite3.connect('msg.db')
    cursor = connection.cursor()

    # Запрашиваем все сообщения от указанного пользователя
    cursor.execute('SELECT * FROM messages WHERE username = ?', (username,))
    messages = cursor.fetchall()  # Получаем все результаты

    # Закрываем соединение
    connection.close()
    return messages

def find_msg_by_id(msg_id):
    """Ищет сообщение по ID."""
    connection = sqlite3.connect('msg.db')
    cursor = connection.cursor()

    # Запрашиваем сообщение по его ID
    cursor.execute('SELECT * FROM messages WHERE id = ?', (msg_id,))
    message = cursor.fetchone()  # Получаем первое найденное сообщение

    # Закрываем соединение
    connection.close()
    return message

# Пример использования
create_database()  # Создаем базу данных и таблицу
