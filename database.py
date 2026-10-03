"""Модуль для работы с базой данных бота."""

import json

from typing import Dict


class DataBase:
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name

    def _load_json(self) -> Dict:
        """Загружает данные из json-файла."""
        try:
            with open(self.file_name, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            return {"complaints": []}

    def _save_json(self, data: Dict) -> None:
        """Сохраняет данные в json-файл."""
        with open(self.file_name, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

    def save_report(self, client_id: int, complaint: str) -> None:
        """Сохраняет жалобу в json-файл."""
        data = self._load_json()
        data["complaints"].append({
            "client_id": client_id,
            "text": complaint
        })
        self._save_json(data)
