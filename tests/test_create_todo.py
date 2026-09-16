import allure

from conftest import make_response


@allure.title("Create todo returns created entity")
@allure.tag("api", "create")
def test_create_todo_returns_created_payload(todo_client, create_todo_payload, monkeypatch):
    def fake_post(url, json, timeout):
        assert url == f"{todo_client.base_url}/todos"
        assert json == create_todo_payload
        assert timeout == todo_client.timeout
        return make_response(201, {"id": 201, **create_todo_payload})

    monkeypatch.setattr(todo_client.session, "post", fake_post)
    response = todo_client.create_todo(create_todo_payload)

    assert response.status_code == 201
    todo = response.json()
    assert todo["title"] == create_todo_payload["title"]
    assert todo["completed"] == create_todo_payload["completed"]
    assert todo["userId"] == create_todo_payload["userId"]
    assert todo["id"] == 201


@allure.title("Create todo propagates API validation failure")
@allure.tag("api", "create")
def test_create_todo_propagates_failure_status(todo_client, create_todo_payload, monkeypatch):
    def fake_post(url, json, timeout):
        assert url == f"{todo_client.base_url}/todos"
        assert json == create_todo_payload
        assert timeout == todo_client.timeout
        return make_response(400, {"error": "invalid todo payload"})

    monkeypatch.setattr(todo_client.session, "post", fake_post)

    response = todo_client.create_todo(create_todo_payload)

    assert response.status_code == 400
    assert response.json()["error"] == "invalid todo payload"
