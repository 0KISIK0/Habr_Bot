"""Модуль парсинга."""

import requests
from bs4 import BeautifulSoup
from typing import Dict


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}


def article_parser(url: str) -> Dict:
    """Возвращает первые 5 статей habr'а с переданной ссылки."""
    try:
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        all_articles = soup.find_all('h2', class_="tm-title tm-title_h2")
        res = {}
        for article in all_articles[:5]:
            text = article.text
            link = "https://habr.com" + article.find('a', class_='tm-title__link')['href']
            res[text] = link
        return res
    except Exception as e:
        print(f"При парсинге произошла ошибка {e}")
        return {
            "При парсинге произошла ошибка": "Попробуйте позже"
        }
