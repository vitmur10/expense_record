import aiogram
import logging

from aiogram.fsm.storage.memory import MemoryStorage

cfg = {
    'token': '',
    'db_name': '',  # Замініть на ім'я вашої PostgreSQL бази даних
    'db_user': '',  # Замініть на користувача PostgreSQL бази даних
    'db_password': '',  # Замініть на пароль користувача PostgreSQL бази даних

    'welcome_message': "",
    'error_message': 'Упс! Помилка! Не хвилюйтеся, помилку вже відправлено розробникам.',
}

bot = aiogram.Bot(token=cfg['token'])

# Змінено підключення до PostgreSQL
"""con = psycopg2.connect(
    dbname=cfg['db_name'],
    user=cfg['db_user'],
    password=cfg['db_password'],
    host='infotron_postgres',  # Залиште як є, оскільки це ім'я сервісу з Docker Compose
    port='5432'  # Залиште як є, порт за замовчуванням для PostgreSQL
)
cur = con.cursor()
order = {}
logging.basicConfig(level=logging.INFO)"""
storage = MemoryStorage()
dp = aiogram.Dispatcher(bot, storage=storage)
