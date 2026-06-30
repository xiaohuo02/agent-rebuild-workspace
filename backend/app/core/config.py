from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings for the rebuild workspace."""

    app_name: str = "Agent Rebuild Workspace"
    api_prefix: str = "/api"
    cors_origins: list[str] = ["http://localhost:5173"]

    model_config = SettingsConfigDict(env_prefix="REBUILD_")


settings = Settings()
