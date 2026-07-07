from app.services.knowledge_service import KnowledgeService


class JobService:

    @staticmethod
    def get_job_creation_process():
        data = KnowledgeService.load_json("jobs.json")
        return {
            "topic": "Job Creation",
            "content": data["job_creation_process"]
        }

    @staticmethod
    def get_job_requirements():
        data = KnowledgeService.load_json("jobs.json")
        return {
            "topic": "Job Requirements",
            "content": data["requirements"]
        }