from app.services.knowledge_service import KnowledgeService


class WorkforceService:

    @staticmethod
    def get_workforce_management():
        data = KnowledgeService.load_json("workforce.json")
        return {
            "topic": "Workforce Management",
            "content": data["workforce_management"]
        }