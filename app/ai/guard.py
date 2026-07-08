import re


class Guard:

    GREETINGS = [
        "hello",
        "hi",
        "hey",
        "hii",
        "good morning",
        "good afternoon",
        "good evening"
    ]


    @staticmethod
    def check(message: str):

        text = message.lower().strip()


        # greeting check

        for word in Guard.GREETINGS:

            if word in text:

                return {
                    "type":"greeting",
                    "response":
                    "Hello 👋 I am HR AI Assistant. I can help you with Leave, Payroll, Jobs and Workforce related queries."
                }


        # very short input

        if len(text) < 3:

            return {
                "type":"invalid",
                "response":
                "Please enter a valid HR question."
            }


        return {
            "type":"continue"
        }