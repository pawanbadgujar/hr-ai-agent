from app.services.knowledge_service import KnowledgeService


class PayrollService:

    @staticmethod
    def get_payroll_basics():
        data = KnowledgeService.load_json("payroll.json")
        return data["payroll_basics"]