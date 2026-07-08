from rapidfuzz import fuzz

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

    @staticmethod
    def detect(query):

        text=query.lower()


        keywords={

            "leave":[
                "leave",
                "vacation",
                "holiday",
                "apply leave"
            ],

            "payroll":[
                "salary",
                "payroll",
                "payslip"
            ],

            "jobs":[
                "job",
                "hiring",
                "requirement"
            ],

            "workforce":[
                "employee",
                "workforce"
            ]

        }


        for module,words in keywords.items():

            for word in words:

                score=fuzz.partial_ratio(text,word)

                if score > 70:
                    return module


        return "unknown"