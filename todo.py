import argparse
from storage import load_tasks, save_tasks

def add_task(title):
    tasks = load_tasks()
    new_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append({"id": new_id, "title": title, "done": False})
    save_tasks(tasks)
    print(f"Added task {new_id}: {title}")

def main():
    parser = argparse.ArgumentParser(description="Simple CLI To-Do App")
    sub = parser.add_subparsers(dest="command")
    p_add = sub.add_parser("add", help="add a task")
    p_add.add_argument("title")
    args = parser.parse_args()
    if args.command == "add":
        add_task(args.title)

if __name__ == "__main__":
    main()