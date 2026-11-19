import argparse
from storage import load_tasks, save_tasks

def add_task(title):
    tasks = load_tasks()
    new_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append({"id": new_id, "title": title, "done": False})
    save_tasks(tasks)
    print(f"Added task {new_id}: {title}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        mark = "x" if t["done"] else " "
        print(f"[{mark}] {t['id']}. {t['title']}")

def main():
    parser = argparse.ArgumentParser(description="Simple CLI To-Do App")
    sub = parser.add_subparsers(dest="command")
    p_add = sub.add_parser("add", help="add a task")
    p_add.add_argument("title")
    sub.add_parser("list", help="show all tasks")
    args = parser.parse_args()
    if args.command == "add":
        add_task(args.title)
    elif args.command == "list":
        list_tasks()

if __name__ == "__main__":
    main()