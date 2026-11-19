import storage
import todo

def test_add_and_complete(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "FILE", tmp_path / "tasks.json")
    todo.add_task("Buy milk")
    assert storage.load_tasks()[0]["title"] == "Buy milk"
    todo.complete_task(1)
    assert storage.load_tasks()[0]["done"] is True

def test_delete(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "FILE", tmp_path / "tasks.json")
    todo.add_task("A")
    todo.delete_task(1)
    assert storage.load_tasks() == []

def test_empty_title_rejected(tmp_path, monkeypatch):
    monkeypatch.setattr(storage, "FILE", tmp_path / "tasks.json")
    todo.add_task("   ")
    assert storage.load_tasks() == []