import allure

from conftest import make_response


@allure.title("Get todos returns a populated collection")
@allure.tag("api", "get")
def test_get_todos_returns_list(todo_client, monkeypatch):
    def fake_get(url, timeout):
        assert url == f"{todo_client.base_url}/todos"
        assert timeout == todo_client.timeout
        return make_response(
            200,
            [
                {
                    "id": 1,
                    "userId": 1,
                    "title": "Write API smoke test",
                    "completed": False,
                }
            ],
        )

    monkeypatch.setattr(todo_client.session, "get", fake_get)
    response = todo_client.get_todos()

    assert response.status_code == 200
    todos = response.json()
    assert isinstance(todos, list)
    assert todos
    first_todo = todos[0]
    assert {"id", "userId", "title", "completed"} <= set(first_todo)


@allure.title("Get todos can return an empty collection")
@allure.tag("api", "get")
def test_get_todos_returns_empty_list(todo_client, monkeypatch):
    def fake_get(url, timeout):
        assert url == f"{todo_client.base_url}/todos"
        assert timeout == todo_client.timeout
        return make_response(200, [])

    monkeypatch.setattr(todo_client.session, "get", fake_get)

    response = todo_client.get_todos()

    assert response.status_code == 200
    assert response.json() == []
