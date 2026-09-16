from __future__ import annotations

from typing import Any

import requests


class TodoClient:
    def __init__(self, base_url: str, timeout: int = 10) -> None:
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def get_todos(self) -> requests.Response:
        return self.session.get(f"{self.base_url}/todos", timeout=self.timeout)

    def create_todo(self, payload: dict[str, Any]) -> requests.Response:
        return self.session.post(f"{self.base_url}/todos", json=payload, timeout=self.timeout)

    def update_todo(self, todo_id: int, payload: dict[str, Any]) -> requests.Response:
        return self.session.put(f"{self.base_url}/todos/{todo_id}", json=payload, timeout=self.timeout)

    def delete_todo(self, todo_id: int) -> requests.Response:
        return self.session.delete(f"{self.base_url}/todos/{todo_id}", timeout=self.timeout)
