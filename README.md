# habr_bot 🤖

Бот для поиска статей на habr.

## 🚀 Функционал
- /start - Запустить бота
- /help - Вызвать эту справку
- /articles - Показать первые 5 статей
- /complaints - Оставить жалобу
- /flows - Показать первые 5 статей, выбранного потока

## 🛠 Технологии
- Python 3.13
- pyTelegramBotAPI (telebot)
- Json

## 📦 Установка и запуск
1. Клонируйте репозиторий:
   ```bash
   git clone git@github.com:0KISIK0/Habr_Bot.git
   cd Habr_Bot
   ```

2. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```

3. Создайте файл `.env` в корневой папке и добавьте токен:
   ```
   BOT_TOKEN=ваш_токен_от_BotFather
   ```

4. Запустите бота:
   ```bash
   python bot.py
   ```

## 👨‍💻 Автор
Roman Chekasin — [https://github.com/0KISIK0]