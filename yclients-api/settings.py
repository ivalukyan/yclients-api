from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    MODE: str = "PROD"
    LOGGER: str = "INFO"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
