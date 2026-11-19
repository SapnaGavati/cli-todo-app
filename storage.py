import json
from pathlib import Path

FILE = Path("tasks.json")

def load_tasks():
    if not FILE.exists():
        return []
    with open(FILE) as f:
        return json.load(f)

def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=2)