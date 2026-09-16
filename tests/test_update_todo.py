import allure

from conftest import make_response


@allure.title("Update todo returns updated entity")
@allure.tag("api", "update")
def test_update_todo_returns_updated_payload(todo_client, update_todo_payload, monkeypatch):
    def fake_put(url, json, timeout):
        assert url == f"{todo_client.base_url}/todos/1"
        assert json == update_todo_payload
        assert timeout == todo_client.timeout
        return make_response(200, {"id": 1, **update_todo_payload})

    monkeypatch.setattr(todo_client.session, "put", fake_put)
    response = todo_client.update_todo(todo_id=1, payload=update_todo_payload)

    assert response.status_code == 200
    todo = response.json()
    assert todo["id"] == 1
    assert todo["title"] == update_todo_payload["title"]
    assert todo["completed"] == update_todo_payload["completed"]
    assert todo["userId"] == update_todo_payload["userId"]


@allure.title("Update todo propagates not found response")
@allure.tag("api", "update")
def test_update_todo_propagates_failure_status(todo_client, update_todo_payload, monkeypatch):
    def fake_put(url, json, timeout):
        assert url == f"{todo_client.base_url}/todos/999"
        assert json == update_todo_payload
        assert timeout == todo_client.timeout
        return make_response(404, {"error": "todo not found"})

    monkeypatch.setattr(todo_client.session, "put", fake_put)

    response = todo_client.update_todo(todo_id=999, payload=update_todo_payload)

    assert response.status_code == 404
    assert response.json()["error"] == "todo not found"
