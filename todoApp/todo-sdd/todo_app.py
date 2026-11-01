from dataclasses import dataclass


@dataclass
class TodoTask:
    description: str
    completed: bool = False


def print_menu() -> None:
    print("\n=== Todo List Manager ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark task as completed")
    print("4. Delete task")
    print("5. Exit")


def get_number(prompt: str):
    while True:
        raw_value = input(prompt)
        if raw_value.strip() == "":
            print("Please enter a number.")
            continue
        try:
            return int(raw_value)
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def add_task(tasks):
    description = input("Enter task description: ").strip()
    if not description:
        print("Task description cannot be empty.")
        return

    tasks.append(TodoTask(description=description, completed=False))
    print(f"Added task: '{description}'")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nCurrent tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "[x]" if task.completed else "[ ]"
        print(f"{index}. {status} {task.description}")


def select_task(tasks, action_name: str):
    if not tasks:
        print("No tasks available to update.")
        return None

    while True:
        task_number = get_number(f"Enter the task number to {action_name}: ")
        if task_number < 1 or task_number > len(tasks):
            print(f"Invalid task number. Please choose a number from 1 to {len(tasks)}.")
            continue
        return task_number - 1


def mark_task_complete(tasks):
    task_index = select_task(tasks, "complete")
    if task_index is None:
        return

    tasks[task_index].completed = True
    print(f"Task marked as complete: '{tasks[task_index].description}'")


def delete_task(tasks):
    task_index = select_task(tasks, "delete")
    if task_index is None:
        return

    removed_task = tasks.pop(task_index)
    print(f"Deleted task: '{removed_task.description}'")


def main():
    tasks = []

    while True:
        try:
            print_menu()
            choice = get_number("Select an option (1-5): ")

            if choice == 1:
                add_task(tasks)
            elif choice == 2:
                view_tasks(tasks)
            elif choice == 3:
                mark_task_complete(tasks)
            elif choice == 4:
                delete_task(tasks)
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid menu choice. Please select a number from 1 to 5.")
        except KeyboardInterrupt:
            print("\nExiting the program.")
            break


if __name__ == "__main__":
    main()
