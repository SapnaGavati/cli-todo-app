# CLI To-Do App

A simple command-line to-do app written in Python. Tasks are saved in a local JSON file.

## Features
- Add, list, complete and delete tasks
- Tasks are saved between runs
- Input validation and error handling
- Unit tests with pytest

## Usage
```
python todo.py add "Buy milk"
python todo.py list
python todo.py done 1
python todo.py delete 1
```

## Run the tests
```
pip install pytest
pytest
```

## Project structure
- `todo.py`: command-line interface and task logic
- `storage.py`: reading and writing tasks.json
- `test_todo.py`: tests