from app.ai.intent_detector import IntentDetector
from app.services.knowledge_service import KnowledgeService


class ChatService:

    FILE_MAPPING = {
        "leave": "leave.json",
        "payroll": "payroll.json",
        "jobs": "jobs.json",
        "workforce": "workforce.json",
    }

    @classmethod
    def process_message(cls, message: str):

        # Detect user intent
        intent = IntentDetector.detect(message)

        # Unknown question
        if intent == "unknown":
            return {
                "intent": "unknown",
                "answer": "Sorry, I can only answer HR related questions about Leave, Payroll, Jobs and Workforce."
            }

        # Load corresponding knowledge file
        data = KnowledgeService.load_json(cls.FILE_MAPPING[intent])

        return {
            "intent": intent,
            "answer": data
        }