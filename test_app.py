import pytest
from app import create_app


def test_home_route():
    app = create_app()
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert b"Hello" in resp.data
