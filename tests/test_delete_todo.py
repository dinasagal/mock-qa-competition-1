import allure

from conftest import make_response


@allure.title("Delete todo succeeds")
@allure.tag("api", "delete")
def test_delete_todo_returns_success(todo_client, monkeypatch):
    def fake_delete(url, timeout):
        assert url == f"{todo_client.base_url}/todos/1"
        assert timeout == todo_client.timeout
        return make_response(200)

    monkeypatch.setattr(todo_client.session, "delete", fake_delete)
    response = todo_client.delete_todo(todo_id=1)

    assert response.status_code == 200


@allure.title("Delete todo propagates not found response")
@allure.tag("api", "delete")
def test_delete_todo_propagates_failure_status(todo_client, monkeypatch):
    def fake_delete(url, timeout):
        assert url == f"{todo_client.base_url}/todos/999"
        assert timeout == todo_client.timeout
        return make_response(404, {"error": "todo not found"})

    monkeypatch.setattr(todo_client.session, "delete", fake_delete)

    response = todo_client.delete_todo(todo_id=999)

    assert response.status_code == 404
    assert response.json()["error"] == "todo not found"
