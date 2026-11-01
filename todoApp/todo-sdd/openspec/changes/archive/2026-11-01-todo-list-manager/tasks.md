# Tasks: Terminal Todo List Manager

## Implementation plan
- [x] Create the single Python entry file and define the main menu loop.
- [x] Initialize an in-memory list for tasks and establish a simple task data structure.
- [x] Implement the add-task flow, including input capture and validation for empty or whitespace-only descriptions.
- [x] Implement the view-all-tasks flow so each task is displayed with a readable status marker and number.
- [x] Implement the complete-task flow by validating the selected task number before updating the completion state.
- [x] Implement the delete-task flow and confirm the task is removed from memory.
- [x] Add robust input validation for invalid menu selections, task numbers, and nonnumeric input without crashing the app.
- [x] Add user-friendly messages for success, warnings, and empty-list states.
- [x] Run a manual smoke test covering add, list, complete, delete, invalid numeric input, invalid menu values, and exit.

## Suggested execution order
- [x] Setup the program shell and loop.
- [x] Add the data structure.
- [x] Implement add/list operations.
- [x] Implement complete/delete operations.
- [x] Add validation and error handling.
- [x] Finish with smoke testing and polish.

## Definition of done
The change is ready when the application supports all required menu actions, handles invalid user input without crashing, keeps tasks in memory only, and remains in a single Python file using only the standard library.
