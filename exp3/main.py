"""
Simple Task Manager application.
"""


class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task: str) -> str:
        """Add a new task."""
        task = task.strip()

        if not task:
            raise ValueError("Task cannot be empty")

        self.tasks.append(task)
        return f"Task added: {task}"

    def remove_task(self, task: str) -> str:
        """Remove an existing task."""
        if task not in self.tasks:
            raise ValueError("Task not found")

        self.tasks.remove(task)
        return f"Task removed: {task}"

    def get_tasks(self) -> list[str]:
        """Return all tasks."""
        return self.tasks.copy()

    def task_count(self) -> int:
        """Return the number of tasks."""
        return len(self.tasks)


def main() -> None:
    manager = TaskManager()

    print(manager.add_task("Write Python code"))
    print(manager.add_task("Run automated tests"))
    print(manager.add_task("Push code to GitHub"))

    print("\nCurrent tasks:")
    for number, task in enumerate(manager.get_tasks(), start=1):
        print(f"{number}. {task}")

    print(f"\nTotal tasks: {manager.task_count()}")


if __name__ == "__main__":
    main()
