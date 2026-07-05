from app.services.knowledge_service import KnowledgeService


class LeaveService:

    @staticmethod
    def get_leave_process():

        data = KnowledgeService.load_json("leave.json")

        return data["leave_process"]["steps"]

    @staticmethod
    def get_leave_policy():

        data = KnowledgeService.load_json("leave.json")

        return data["policy"]