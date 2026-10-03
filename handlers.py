"""Модуль с обработчиками команд."""

import telebot

from database import DataBase
from telebot.types import Message
from parser import article_parser
from keyboards import generate_menu_keyboard, generate_flows_menu
from config import MAIN_URL

db = DataBase("data.json")


def register_handlers(bot: telebot.TeleBot) -> None:
    """Регистрирует все обработчики команд."""

    @bot.message_handler(commands=["start"])
    def handler_start(message: Message) -> None:
        """Обработчик команды /start."""
        bot.send_message(
            message.chat.id,
            "Привет!",
            reply_markup=generate_menu_keyboard()
        )

    @bot.message_handler(commands=["help"])
    def handler_help(message: Message) -> None:
        """Обработчик команды /help."""
        bot.send_message(
            message.chat.id,
            """
            /start - Запустить бота
            /help - Вызвать эту справку
            /articles - Показать первые 5 статей
            /complaints - Оставить жалобу
            /flows - Показать первые 5 статей, выбранного потока
            """
        )

    @bot.message_handler(commands=["articles"])
    def handler_articles(message: Message) -> None:
        """Обработчик команды /articles."""
        articles = article_parser(MAIN_URL)
        for text, link in articles.items():
            bot.send_message(message.chat.id, f'{text}\n{link}')

    @bot.message_handler(commands=["complaints"])
    def handler_complaints(message: Message) -> None:
        """Обработчик команды /complaints."""
        bot.send_message(
            message.chat.id,
            "Пожалуйста, напишите причину жалобы одним сообщением. Опишите ситуацию как можно подробнее."
        )
        bot.register_next_step_handler(message, get_report)

    def get_report(message: Message) -> None:
        report_msg = message.text
        db.save_report(message.chat.id, report_msg)
        bot.send_message(
            message.chat.id,
            "Спасибо! Ваша жалоба отправлена администрации. Мы постараемся разобраться в ближайшее время."
        )

    @bot.message_handler(commands=["flows"])
    def handler_flows(message: Message) -> None:
        """Обработчик команды /flows."""
        bot.send_message(message.chat.id, "Потоки:", reply_markup=generate_flows_menu())

    @bot.message_handler(content_types=["text"])
    def handle_text(message: Message) -> None:
        """Обработчик текстовых сообщений."""
        if message.text == "Популярное":
            handler_articles(message)
        elif message.text == "Потоки":
            bot.send_message(message.chat.id, "Потоки:", reply_markup=generate_flows_menu())
        elif message.text == "Жалоба":
            bot.send_message(
                message.chat.id,
                "Пожалуйста, напишите причину жалобы одним сообщением. Опишите ситуацию как можно подробнее."
            )
            bot.register_next_step_handler(message, get_report)
        else:
            bot.send_message(message.chat.id, "Я вас не понимаю")

    @bot.callback_query_handler(func=lambda call: True)
    def query_handler(call):
        """Обработчик колбэков"""
        if call.data.startswith("flow|"):
            _, name_flow = call.data.split("|")
            flows = article_parser(f'https://habr.com/ru/flows/{name_flow}/articles/')
            for text, link in flows.items():
                bot.send_message(call.message.chat.id, f'{text}\n{link}')
