import threading
import streamlit as st
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Функция для работы бота
def run_bot():
    # Токен бота
    updater = Updater("7930470705:AAHbOa2VpXknxhnkdV5sCE9R3W50yjTbVwg", use_context=True)
    dp = updater.dispatcher

    # Ответ на любое сообщение
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, 
                                  lambda update, context: update.message.reply_text("Я получил твоё сообщение!")))

    # Запуск бота
    updater.start_polling()
    updater.idle()

# Запуск бота в отдельном потоке
threading.Thread(target=run_bot, daemon=True).start()

# Код для Streamlit UI
st.title("Streamlit + Telegram Bot")
st.write("Бот работает в фоне и будет отвечать на сообщения.")
