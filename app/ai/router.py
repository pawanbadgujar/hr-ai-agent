def detect_module(question: str):

    question = question.lower()

    leave_keywords = [
        "leave",
        "casual",
        "sick",
        "vacation",
        "holiday"
    ]

    payroll_keywords = [
        "salary",
        "pay",
        "payroll",
        "tax",
        "deduction",
        "ctc"
    ]

    jobs_keywords = [
        "job",
        "vacancy",
        "recruitment",
        "opening",
        "hiring"
    ]

    workforce_keywords = [
        "employee",
        "department",
        "manager",
        "team",
        "workforce"
    ]

    if any(word in question for word in leave_keywords):
        return "leave"

    if any(word in question for word in payroll_keywords):
        return "payroll"

    if any(word in question for word in jobs_keywords):
        return "jobs"

    if any(word in question for word in workforce_keywords):
        return "workforce"

    return "general"