from app.core.config import Settings


def test_settings_read_mimo_and_ollama_embedding_env(monkeypatch) -> None:
    monkeypatch.setenv("REBUILD_LLM_PROVIDER", "mimo")
    monkeypatch.setenv("REBUILD_MIMO_API_KEY", "mimo-secret")
    monkeypatch.setenv("REBUILD_MIMO_BASE_URL", "https://api.xiaomimimo.com/v1")
    monkeypatch.setenv("REBUILD_MIMO_MODEL", "mimo-v2.5-pro")
    monkeypatch.setenv("REBUILD_OLLAMA_EMBEDDING_MODEL", "quentinz/bge-large-zh-v1.5:f16")

    settings = Settings()

    assert settings.llm_provider == "mimo"
    assert settings.mimo_api_key == "mimo-secret"
    assert settings.mimo_base_url == "https://api.xiaomimimo.com/v1"
    assert settings.mimo_model == "mimo-v2.5-pro"
    assert settings.ollama_embedding_model == "quentinz/bge-large-zh-v1.5:f16"
