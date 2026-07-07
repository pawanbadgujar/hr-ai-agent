class IntentDetector:
    """
    Detects the user's intent based on keywords.
    """

    INTENTS = {
        "leave": [
            "leave",
            "vacation",
            "holiday",
            "time off",
            "sick leave",
            "casual leave",
            "annual leave",
            "balance"
        ],
        "payroll": [
            "salary",
            "payroll",
            "payslip",
            "tax",
            "ctc",
            "bonus"
        ],
        "jobs": [
            "job",
            "opening",
            "vacancy",
            "career",
            "hiring",
            "position"
        ],
        "workforce": [
            "attendance",
            "shift",
            "employee",
            "workforce",
            "work from home",
            "wfh"
        ]
    }

    @classmethod
    def detect(cls, message: str) -> str:
        """
        Returns the detected intent.
        """

        message = message.lower()

        for intent, keywords in cls.INTENTS.items():
            for keyword in keywords:
                if keyword in message:
                    return intent

        return "unknown"