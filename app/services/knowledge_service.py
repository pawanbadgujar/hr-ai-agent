import json
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent
KNOWLEDGE_DIR = BASE_DIR / "knowledge"


class KnowledgeService:

    @staticmethod
    def load_json(filename: str):
        file_path = KNOWLEDGE_DIR / filename

        with open(file_path, "r", encoding="utf-8") as file:
            return json.load(file)