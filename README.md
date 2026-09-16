# mock-qa-competition-1

Simple pytest-based API QA infrastructure for todo endpoints.

## Project structure

```text
mock-qa-competition-1/
├── api/
│   └── todo_client.py
├── test_data/
│   ├── create_todo.json
│   └── update_todo.json
├── tests/
│   ├── test_create_todo.py
│   ├── test_delete_todo.py
│   ├── test_get_todos.py
│   └── test_update_todo.py
├── conftest.py
├── pytest.ini
├── requirements.txt
└── test_plan.md
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Run tests

The `TodoClient` defaults to `https://jsonplaceholder.typicode.com`, and you can
override the API host with `TODO_API_BASE_URL`. The included pytest suite is a
mocked client test suite, so it validates request construction and response
handling without requiring live network access in CI.

```bash
pytest
```

## Allure reports

Generate Allure result files while running tests:

```bash
pytest --alluredir=allure-results
```

Serve the report locally:

```bash
allure serve allure-results
```

> `allure serve` requires the Allure command-line tool to be installed separately
> from the Python dependencies.