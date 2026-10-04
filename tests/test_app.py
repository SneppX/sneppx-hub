def test_health():
    from fastapi.testclient import TestClient
    from sneppx_hub.app import app
    assert TestClient(app).get("/healthz").json()["status"] == "ok"
