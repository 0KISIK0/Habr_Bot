"""Главный модуль бота."""

import telebot

from dotenv import load_dotenv
import os
from handlers import register_handlers


load_dotenv()


def main() -> None:
    """Запускает бота."""
    bot = telebot.TeleBot(os.getenv("TOKEN"))
    register_handlers(bot)
    print("Бот запущен...")
    bot.polling(none_stop=True)


if __name__ == "__main__":
    main()
