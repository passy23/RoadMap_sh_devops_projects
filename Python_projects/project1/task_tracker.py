import json
import sys
from datetime import datetime

TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from JSON file or return empty list."""
    try:
        with open(TASKS_FILE, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    """Save tasks to JSON file."""
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    task_id = len(tasks) + 1
    task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added (ID: {task_id})")

def update_task(task_id, description):
    """Update a task's description."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['description'] = description
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated")
            return
    print(f"Task {task_id} not found")

def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task['id'] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted")

def mark_task(task_id, status):
    """Mark a task as in-progress or done."""
    tasks = load_tasks()
    for task in tasks:
        if task['id'] == task_id:
            task['status'] = status
            task['updatedAt'] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as {status}")
            return
    print(f"Task {task_id} not found")

def list_tasks(status=None):
    """List tasks, optionally by status."""
    tasks = load_tasks()
    tasks = [t for t in tasks if status is None or t['status'] == status]
    if not tasks:
        print("No tasks found")
        return
    for task in tasks:
        print(f"ID: {task['id']}, {task['description']}, Status: {task['status']}")

def main():
    """Handle CLI commands."""
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [args]")
        sys.exit(1)

    cmd = sys.argv[1]
    if cmd == "add" and len(sys.argv) > 2:
        add_task(" ".join(sys.argv[2:]))
    elif cmd == "update" and len(sys.argv) > 3:
        update_task(int(sys.argv[2]), " ".join(sys.argv[3:]))
    elif cmd == "delete" and len(sys.argv) == 3:
        delete_task(int(sys.argv[2]))
    elif cmd in ["mark-in-progress", "mark-done"] and len(sys.argv) == 3:
        mark_task(int(sys.argv[2]), cmd.replace("mark-", ""))
    elif cmd == "list" and len(sys.argv) <= 3:
        list_tasks(sys.argv[2] if len(sys.argv) == 3 else None)
    else:
        print("Invalid command or arguments")
        sys.exit(1)

if __name__ == "__main__":
    main()
