import os
from pydantic import BaseSettings


class Settings(BaseSettings):
    # Database URL
    DATABASE_URL: str = os.getenv(
        "DATABASE_URL", "postgresql://user:password@localhost/dbname"
    )

    # JWT settings
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key")
    ALGORITHM: str = "HS256"  # The algorithm used to sign JWT tokens
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30  # Token expiration time in minutes

    # Add other settings here as needed (e.g., logging, S3 credentials, etc.)

    class Config:
        # Automatically read variables from the environment
        env_file = ".env"  # Read environment variables from a .env file (optional)
        env_file_encoding = "utf-8"


# Instantiate the settings object
settings = Settings()
