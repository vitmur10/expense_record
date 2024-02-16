import json
import seaborn as sns
import matplotlib.pyplot as plt
import io

from Const import *


def send_stats(chat_id):
    # Отримуємо дані з бд
    cur.execute(f"""SELECT * FROM records""")
    data = cur.fetchall()

    # Розбиваємо по категоріям та сумуємо їх значення
    datas = {}

    for p_info in data:
        category = p_info[1][2:]
        datas[category] = datas.get(category, 0) + int(p_info[4])

    # Формуємо діаграму
    colors = sns.color_palette('pastel')[0:5]

    # Виведення конретного значення для конкретного ключа, щоб в діаграмі відображалось витрати а не відсоток
    def format_func(pct):
        total = sum(datas.values())
        val = int(pct / 100. * total)
        return f'{val}'

    plt.pie(datas.values(), labels=datas.keys(), colors=colors, autopct=format_func)

    # Створюємо картинку в буфер
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Відправляємо картинку користувачу за допомогою Telegram API
    bot.send_photo(chat_id=chat_id, photo=buf)

    # Закриваємо об'єкт графіка)
    plt.close()


def send_costs(category):
    # Отримання з бд всіх значень по конкретній категорії
    try:
        cur.execute(f"""SELECT * FROM records WHERE category == '{category}'""")
        data = cur.fetchall()
        return data
    except Exception as ex:

        print(ex)
