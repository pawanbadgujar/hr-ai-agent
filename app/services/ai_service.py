import json
import google.generativeai as genai

from app.ai.prompts import SYSTEM_PROMPT
from app.ai.router import detect_module
from app.core.config import settings
from app.services.knowledge_service import KnowledgeService
from app.ai.guard import Guard

# Configure Gemini
genai.configure(api_key=settings.GOOGLE_API_KEY)

# Load Model
model = genai.GenerativeModel("gemini-2.5-flash")


class AIService:

    @staticmethod
    def ask(query: str):

        guard = Guard.check(query)


        if guard["type"] != "continue":

            return guard["response"]

        module = detect_module(query)

        knowledge = {}

        if module == "leave":
            knowledge = KnowledgeService.load_json("leave.json")

        elif module == "jobs":
            knowledge = KnowledgeService.load_json("jobs.json")

        elif module == "payroll":
            knowledge = KnowledgeService.load_json("payroll.json")

        elif module == "workforce":
            knowledge = KnowledgeService.load_json("workforce.json")

        # Build Prompt
        prompt = f"""
{SYSTEM_PROMPT}

HR Knowledge Base:

{json.dumps(knowledge, indent=2)}

User Question:

{query}

Answer using ONLY the HR Knowledge Base provided above.
If the answer is not available in the knowledge base,
reply politely that the information is unavailable.
"""

        # Ask Gemini
        response = model.generate_content(prompt)

        return response.text