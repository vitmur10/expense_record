import logging

import aiogram
from aiogram.contrib.fsm_storage.memory import MemoryStorage

cfg = {
    'token': '6610830289:AAFYd-_43M6vmF2vGhQuRzIO224P9JnmHco',
    'db_name': '',  # Замініть на ім'я вашої PostgreSQL бази даних
    'db_user': '',  # Замініть на користувача PostgreSQL бази даних
    'db_password': '',  # Замініть на пароль користувача PostgreSQL бази даних

    'welcome_message': f"""
Привітік! 😊

Вітаємо у світі бота-записника витрат! 🎉 Тепер ви зможете легко відстежувати свої витрати і керувати фінансами. Просто вводьте свої витрати, і ми все вам записуватимемо. Якщо щось потрібно, пишіть нам, ми завжди раді допомогти! 💰

З любов'ю,
Команда бота-записника 📝""",
    'error_message': 'Упс! Помилка! Не хвилюйтеся, помилку вже відправлено розробникам.',
}


# Змінено підключення до PostgreSQL
"""con = psycopg2.connect(
    dbname=cfg['db_name'],
    user=cfg['db_user'],
    password=cfg['db_password'],
    host='infotron_postgres',  # Залиште як є, оскільки це ім'я сервісу з Docker Compose
    port='5432'  # Залиште як є, порт за замовчуванням для PostgreSQL
)
cur = con.cursor()
order = {}"""
logging.basicConfig(level=logging.INFO)
bot = aiogram.Bot(token=cfg['token'])
storage = MemoryStorage()
dp = aiogram.Dispatcher(bot, storage=storage)
