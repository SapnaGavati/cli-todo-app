import argparse
from storage import load_tasks, save_tasks

def add_task(title):
    if not title.strip():
        print("Title cannot be empty")
        return
    tasks = load_tasks()
    new_id = max((t["id"] for t in tasks), default=0) + 1
    tasks.append({"id": new_id, "title": title.strip(), "done": False})
    save_tasks(tasks)
    print(f"Added task {new_id}: {title.strip()}")

def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for t in tasks:
        mark = "x" if t["done"] else " "
        print(f"[{mark}] {t['id']}. {t['title']}")

def complete_task(task_id):
    tasks = load_tasks()
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = True
            save_tasks(tasks)
            print(f"Completed task {task_id}")
            return
    print(f"Task {task_id} not found")

def delete_task(task_id):
    tasks = load_tasks()
    remaining = [t for t in tasks if t["id"] != task_id]
    if len(remaining) == len(tasks):
        print(f"Task {task_id} not found")
        return
    save_tasks(remaining)
    print(f"Deleted task {task_id}")

def main():
    parser = argparse.ArgumentParser(description="Simple CLI To-Do App")
    sub = parser.add_subparsers(dest="command")
    p_add = sub.add_parser("add", help="add a task")
    p_add.add_argument("title")
    sub.add_parser("list", help="show all tasks")
    p_done = sub.add_parser("done", help="mark a task done")
    p_done.add_argument("task_id", type=int)
    p_del = sub.add_parser("delete", help="delete a task")
    p_del.add_argument("task_id", type=int)
    args = parser.parse_args()
    if args.command == "add":
        add_task(args.title)
    elif args.command == "list":
        list_tasks()
    elif args.command == "done":
        complete_task(args.task_id)
    elif args.command == "delete":
        delete_task(args.task_id)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()