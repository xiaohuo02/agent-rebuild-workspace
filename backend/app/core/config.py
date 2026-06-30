from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Runtime settings for the rebuild workspace."""

    app_name: str = "Agent Rebuild Workspace"
    api_prefix: str = "/api"
    cors_origins: list[str] = ["http://localhost:5173"]
    llm_provider: str = "fake"

    deepseek_api_key: str = ""
    deepseek_base_url: str = "https://api.deepseek.com/v1"
    deepseek_model: str = "deepseek-chat"

    mimo_api_key: str = ""
    mimo_base_url: str = "https://api.xiaomimimo.com/v1"
    mimo_model: str = "mimo-v2.5-pro"

    ollama_base_url: str = "http://127.0.0.1:11434"
    ollama_model: str = "qwen3:4b"
    ollama_embedding_model: str = "quentinz/bge-large-zh-v1.5:f16"

    mysql_dsn: str = ""
    redis_url: str = "redis://127.0.0.1:6380/0"
    neo4j_uri: str = "bolt://127.0.0.1:7687"
    neo4j_username: str = "neo4j"
    neo4j_password: str = ""
    neo4j_database: str = "neo4j"
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_prefix="REBUILD_")


settings = Settings()
