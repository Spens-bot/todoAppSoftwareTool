# Design: Terminal Todo List Manager

## Overview
The application will be a small, single-file Python program built around a simple menu loop. It will manage an in-memory list of tasks, validate user input at each step, and re-render the menu after each action.

## Architecture
- One Python file at the project root, such as `todo_app.py`.
- A task model that stores at least:
  - a task description
  - a completion flag
  - a display position or index in the in-memory list
- A `main()` function that drives the interactive loop.
- Small helper functions for each operation:
  - `show_menu()`
  - `add_task()`
  - `view_tasks()`
  - `mark_task_complete()`
  - `delete_task()`
  - `get_valid_menu_choice()`
  - `get_valid_task_number()`

## Data model
Use a simple list of dictionaries or a lightweight dataclass representing each task. A dictionary-based model is enough for a small app, but a dataclass improves clarity and reduces mistakes when expanding functionality later.

Example structure:
- `tasks`: list of task records
- each task record: `{"description": "Task name", "completed": False}`

## Menu flow
1. Print the menu.
2. Read user input.
3. Validate the selection.
4. Dispatch to the matching command.
5. Print a confirmation or result message.
6. Repeat until the user selects exit.

## Validation strategy
- Convert menu choices to integers only when the input is numeric.
- Reject nonnumeric input and invalid integer values with a clear message.
- For task operations, verify that the selected number exists in the current task list before modifying or deleting it.
- Catch errors at the input boundary so the application remains running instead of crashing.

## User experience
- Keep terminal output simple and readable.
- Use numbered tasks when listing them.
- Show status values such as `[ ]` for incomplete and `[x]` for complete.
- Tell the user when the list is empty.
- Return to the main menu after each valid operation.

## Constraints
- No database persistence.
- No external packages.
- No GUI or web interface.
- All behavior must remain in a single Python file.
