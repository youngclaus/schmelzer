import json
import os

DATA_FILE = "data/saved_sheets.json"


class StorageManager:
    @staticmethod
    def load_players(file_path):
        if not os.path.exists(file_path):
            return []

        with open(file_path, "r") as file:
            data = json.load(file)
            return data.get("players", [])

    @staticmethod
    def save_players(players):
        with open(DATA_FILE, "w") as file:
            json.dump({"players": players}, file, indent=4)
