import json
import os
from pathlib import Path

import pytest
from requests import Response

from api.todo_client import TodoClient


BASE_DIR = Path(__file__).resolve().parent


def load_test_data(file_name: str) -> dict:
    with (BASE_DIR / "test_data" / file_name).open(encoding="utf-8") as file:
        return json.load(file)


def make_response(status_code: int, payload: dict | list | None = None) -> Response:
    response = Response()
    response.status_code = status_code
    response._content = json.dumps(payload if payload is not None else {}).encode("utf-8")
    response.headers["Content-Type"] = "application/json"
    return response


@pytest.fixture(scope="session")
def base_url() -> str:
    return os.getenv("TODO_API_BASE_URL", "https://jsonplaceholder.typicode.com")


@pytest.fixture(scope="session")
def todo_client(base_url: str) -> TodoClient:
    return TodoClient(base_url=base_url)


@pytest.fixture
def create_todo_payload() -> dict:
    return load_test_data("create_todo.json")


@pytest.fixture
def update_todo_payload() -> dict:
    return load_test_data("update_todo.json")
