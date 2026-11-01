# Proposal: Terminal Todo List Manager

## Summary
Create a small Python command-line application that helps a user manage a short list of tasks. The app will run in the terminal, keep tasks in memory while the program is active, and provide a simple, repeatable menu-driven interface for everyday task operations.

## Why
The project is a good fit for a beginner-friendly Python exercise because it combines core programming concepts such as loops, conditionals, user input validation, data modeling, and clean console output. It is also easy to use, easy to test manually, and does not require any external packages or database setup.

## What Changes
The change adds a menu-driven terminal application for managing tasks in memory. It includes adding tasks, viewing the current list, marking tasks complete, deleting tasks, repeating the menu until exit, and validating invalid input without crashing the program. The implementation stays in a single Python file and uses only the Python standard library.

## Scope
In scope:
- Add new tasks with text descriptions.
- Display all tasks with their completion status.
- Mark tasks as completed by selecting their number.
- Delete tasks by number.
- Repeat the menu until the user exits.
- Validate invalid menu choices, invalid task numbers, and nonnumeric input without crashing.
- Use only the Python standard library and keep the program in a single Python file.

Out of scope:
- Persistent storage across program restarts.
- A graphical user interface or web interface.
- External libraries or database integration.
- Multi-user or networked task management.
