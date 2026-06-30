from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health_endpoint() -> None:
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_chat_endpoint_uses_fake_model() -> None:
    response = client.post("/api/chat", json={"message": "你好"})

    assert response.status_code == 200
    assert "我已收到你的问题" in response.json()["answer"]


def test_agent_query_endpoint_returns_trace_and_evidence() -> None:
    response = client.post(
        "/api/agent/query",
        json={"query": "智能门锁多少钱，有库存吗，保修多久"},
    )

    payload = response.json()
    assert response.status_code == 200
    assert payload["route"] == "mixed"
    assert payload["trace"]
    assert payload["evidence"]
