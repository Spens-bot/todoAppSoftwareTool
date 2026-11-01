
def show_menu():
    print("\n===== TO-DO LIST MANAGER =====")
    print("1. Add a task")
    print("2. View all tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Exit")


def add_task(tasks):
    description = input("Enter a new task: ").strip()

    if not description:
        print("Task cannot be empty.")
        return

    tasks.append({"description": description, "completed": False})
    print("Task added successfully!")


def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
        return

    print("\nYour Tasks:")
    for index, task in enumerate(tasks, start=1):
        status = "Completed" if task["completed"] else "Pending"
        print(f"{index}. [{status}] {task['description']}")


def get_task_index(tasks):
    if not tasks:
        print("No tasks available.")
        return None

    view_tasks(tasks)

    try:
        number = int(input("Enter task number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        return None

    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return None

    return number - 1


def complete_task(tasks):
    index = get_task_index(tasks)

    if index is not None:
        tasks[index]["completed"] = True
        print("Task marked as completed!")


def delete_task(tasks):
    index = get_task_index(tasks)

    if index is not None:
        removed_task = tasks.pop(index)
        print(f"Task deleted: {removed_task['description']}")


def main():
    tasks = []

    while True:
        show_menu()
        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()
