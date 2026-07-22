from pydantic_settings import BaseSettings


class Settings(BaseSettings):

    PROJECT_NAME: str = "HR AI Agent"

    VERSION: str = "1.0.0"

    OPENAI_API_KEY: str = ""
    OPENROUTER_API_KEY: str = ""
    GOOGLE_API_KEY: str = ""

    DATABASE_URL: str = ""

    class Config:
        env_file = ".env"


settings = Settings()