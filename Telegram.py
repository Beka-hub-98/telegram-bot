import schedule
import time
from telegram import Bot

# Токен бота
TOKEN = "7240887720:AAFSUYhAA8I7Nx317tfcQmACtrFiWwY_Skk"
# ID Telegram-группы
CHAT_ID = -1002761648162

# Инициализация бота
bot = Bot(token=TOKEN)

# Функции отправки сообщений
def send_morning():
    bot.send_message(chat_id=CHAT_ID, text="Доброе утро мужики, готовимся работать!")

def send_evening():
    bot.send_message(chat_id=CHAT_ID, text="Мощно поработали")

# Расписание
schedule.every().day.at("07:00").do(send_morning)
schedule.every().day.at("18:00").do(send_evening)

print("Бот запущен и ждёт времени...")

# Основной цикл
while True:
    schedule.run_pending()
    time.sleep(60)  # проверяет каждую минуту