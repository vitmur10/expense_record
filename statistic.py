import json
import seaborn as sns
import matplotlib.pyplot as plt
import io

from Const import bot


def send_stats(chat_id):
    # Отримуємо дані з json файлу
    with open("data.json", "r", encoding="utf-8") as file:
        data = json.load(file)

    # Розбиваємо по категоріям та сумуємо їх значення
    datas = {}
    for p_id, p_info in data.items():
        for key in p_info:
            datas[p_id] = datas.get(p_id, 0) + p_info[key]

    # Формуємо діаграму
    colors = sns.color_palette('pastel')[0:5]
    plt.pie(datas.values(), labels=datas.keys(), colors=colors, autopct='%.0f%%')

    # Створюємо картинку в буфер
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)

    # Відправляємо картинку користувачу за допомогою Telegram API
    bot.send_photo(chat_id=chat_id, photo=buf)

    # Закриваємо об'єкт графіка)
    plt.close()


def send_costs(category):
    def get_value_from_key(key_to_find):
        def hook(dct):
            if key_to_find in dct:
                return dct[key_to_find]
            return dct

        return hook

    # Відкриття файлу JSON та завантаження вмісту, використовуючи object_hook
    with open("data.json", 'r', encoding='utf-8') as file:
        data = json.load(file, object_hook=get_value_from_key(category))

    print(data)


send_costs("Одяг")