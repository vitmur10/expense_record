import json
import seaborn as sns
import matplotlib.pyplot as plt
import io

from Const import *


def send_stats():
    # Отримуємо дані з бд
    cur.execute(f"""SELECT * FROM records""")
    data = cur.fetchall()

    # Розбиваємо по категоріям та сумуємо їх значення
    datas = {}

    for p_info in data:
        category = p_info[1][2:]
        try:
            datas[category] = datas.get(category, 0) + int(p_info[4])
        except:
            pass

    # Формуємо діаграму
    colors = sns.color_palette('pastel')[0:5]

    # Виведення конретного значення для конкретного ключа, щоб в діаграмі відображалось витрати а не відсоток
    def format_func(pct):
        total = sum(datas.values())
        val = int(pct / 100. * total + 1)
        return f'{val}'

    plt.pie(datas.values(), labels=datas.keys(), colors=colors, autopct=format_func)

    # Створюємо картинку в буфер
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Після надсилання картинки, очищаємо діаграму, щоб пізніше не було конфліктів
    plt.clf()

    return buf


def send_costs(category):
    # Отримання з бд всіх значень по конкретній категорії
    try:
        cur.execute(f"""SELECT * FROM records WHERE category == '{category}'""")
        data = cur.fetchall()
        return data
    except Exception as ex:

        print(ex)