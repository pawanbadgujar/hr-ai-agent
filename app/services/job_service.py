from app.services.knowledge_service import KnowledgeService


class JobService:

    @staticmethod
    def get_job_creation_process():
        data = KnowledgeService.load_json("jobs.json")
        return data["job_creation"]

    @staticmethod
    def get_job_requirements():
        data = KnowledgeService.load_json("jobs.json")
        return data["job_requirements"]