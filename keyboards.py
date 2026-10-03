"""Модуль для генерации клавиатур."""

from telebot import types
from telebot.types import (
    ReplyKeyboardMarkup, KeyboardButton,
)
from config import FLOWS

from database import DataBase

db = DataBase("data.json")


def generate_menu_keyboard() -> types.ReplyKeyboardMarkup:
    """"""
    markup = ReplyKeyboardMarkup()
    btn_articles = KeyboardButton("Популярное")
    btn_flows = KeyboardButton("Потоки")
    btn_complaint = KeyboardButton("Жалоба")
    markup.add(btn_articles, btn_flows, btn_complaint)
    return markup


def generate_flows_menu() -> types.InlineKeyboardMarkup:
    """"""
    markup = types.InlineKeyboardMarkup()
    for title, link_part in FLOWS.items():
        btn = types.InlineKeyboardButton(title, callback_data=f"flow|{link_part}")
        markup.add(btn)
    return markup
