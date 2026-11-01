# Todo List Manager Specification

## Purpose
The system is a single-file Python terminal application for managing a list of tasks in memory. It provides a repeated menu-driven workflow that lets a user add, view, complete, and delete tasks while keeping the application lightweight, readable, and resilient to invalid input.

## Requirements

### Requirement: Maintain tasks in memory
The application SHALL maintain a list of tasks in memory while it is running.

#### Scenario: Task list remains available throughout the session
- **WHEN** the user adds, views, completes, or deletes tasks
- **THEN** the tasks remain available in memory until the program exits

### Requirement: Include task position and completion state
Each task SHALL have a visible position in the list and a completion state that can be either complete or incomplete.

#### Scenario: Position and completion status are visible to the user
- **WHEN** the user views the task list
- **THEN** each task displays a numbered position and a completion indicator

### Requirement: Display a numbered menu
The app SHALL display a numbered menu with options to add a task, view all tasks, mark a task complete, delete a task, and exit.

#### Scenario: Main menu appears at each iteration
- **WHEN** the application waits for the next action
- **THEN** the menu is shown again after each operation

### Requirement: Add a task description
Selecting the add option SHALL prompt the user for a task description and append it to the task list.

#### Scenario: Valid task is added
- **WHEN** the user selects add and enters a non-empty description
- **THEN** the task is appended to the list

#### Scenario: Empty or blank task descriptions are rejected
- **WHEN** the user enters a blank or whitespace-only description
- **THEN** the system rejects the input and does not add a task

### Requirement: View all tasks in readable format
Selecting the view option SHALL display all tasks in a readable format, including a status indicator for each task.

#### Scenario: User can inspect current tasks
- **WHEN** the user chooses to view tasks
- **THEN** the system displays every task with its number and completion marker

### Requirement: Complete a selected task
Selecting the complete option SHALL prompt the user for a task number and update the selected task to a completed state.

#### Scenario: Task completion is applied
- **WHEN** the user selects a valid task number to complete
- **THEN** the selected task is marked as complete

### Requirement: Delete a selected task
Selecting the delete option SHALL prompt the user for a task number and remove the selected task from the list.

#### Scenario: Task is deleted from memory
- **WHEN** the user selects a valid task number to delete
- **THEN** the chosen task is removed from the list

### Requirement: Keep the menu loop active until exit
The menu loop SHALL repeat until the user explicitly chooses to exit.

#### Scenario: Program continues after valid actions
- **WHEN** the user performs an action other than exit
- **THEN** the menu reappears and continues the workflow

### Requirement: Reject invalid menu selections gracefully
Invalid menu selections SHALL be rejected gracefully with a clear error message and without terminating the program.

#### Scenario: Unsupported menu values are handled safely
- **WHEN** the user enters an invalid menu option
- **THEN** the system prints a clear message and returns to the menu

### Requirement: Reject invalid task numbers gracefully
Invalid task numbers SHALL be handled gracefully with a clear error message and without terminating the program.

#### Scenario: Out-of-range task numbers are rejected
- **WHEN** the user selects a task number outside the current list range
- **THEN** the system shows a user-friendly error and keeps the menu running

### Requirement: Reject non-numeric input safely
Non-numeric input for menu choices and task selections SHALL be handled gracefully with a clear error message and without terminating the program.

#### Scenario: Alphabetic or blank input is rejected without crash
- **WHEN** the user enters alphabetic characters or an empty response
- **THEN** the application prints an error and waits for a valid input

### Requirement: Use only the standard library
The application SHALL use only the Python standard library.

#### Scenario: No external dependency is required
- **WHEN** the program runs
- **THEN** it does not depend on a database or external package

### Requirement: Keep the implementation in a single Python file
The application SHALL keep all logic within one Python file and shall not rely on a database or any external package.

#### Scenario: Single-file implementation is preserved
- **WHEN** the project is reviewed
- **THEN** all program logic remains in one Python file at the project root

### Requirement: Support immediate task visibility after add
A user SHALL be able to add tasks and see them listed immediately.

#### Scenario: Immediate view after add
- **WHEN** the user adds a task and then views the list
- **THEN** the new task appears without restarting the application

### Requirement: Show completion status after marking a task complete
A user SHALL be able to complete a task and see the updated status in the task list.

#### Scenario: Completed tasks display updated state
- **WHEN** the user marks a task complete
- **THEN** the task list reflects the updated status

### Requirement: Confirm deletion from the list
A user SHALL be able to delete a task and confirm it is removed.

#### Scenario: Deleted task is no longer visible
- **WHEN** the user deletes a task
- **THEN** the task no longer appears in later list views

### Requirement: Prevent premature exit
The application SHALL exit only when the user selects the exit option.

#### Scenario: Exit is explicit
- **WHEN** the user is performing normal actions in the app
- **THEN** the program continues running until the user intentionally exits

### Requirement: Task list state persists while the app is running
The system SHALL maintain a list of tasks in memory while it is running.

#### Scenario: In-memory task list remains available during the session
- **WHEN** the user adds, views, completes, or deletes tasks
- **THEN** the task list remains available in memory until the user exits the program

### Requirement: Each task includes a visible position and completion state
Each task SHALL have a visible position in the list and a completion state that can be either complete or incomplete.

#### Scenario: Task status is visible in the list
- **WHEN** the user views the task list
- **THEN** each task shows a numbered position and an indicator for complete or incomplete status

### Requirement: Menu options are displayed for the todo list workflow
The app SHALL display a numbered menu with options to add a task, view all tasks, mark a task complete, delete a task, and exit.

#### Scenario: Menu is shown on each loop iteration
- **WHEN** the application is waiting for the next user action
- **THEN** the numbered menu is displayed again after each action and before the next choice

### Requirement: Add task flow accepts user input and stores it
Selecting the add option SHALL prompt the user for a task description and append it to the task list.

#### Scenario: User adds a new task successfully
- **WHEN** the user selects add and enters a non-empty description
- **THEN** the task is appended to the list and shown as a valid item

#### Scenario: Empty task descriptions are rejected
- **WHEN** the user enters a blank or whitespace-only description
- **THEN** the app rejects the input with a clear message and does not add a task

### Requirement: View task flow presents readable task data
Selecting the view option SHALL display all tasks in a readable format, including a status indicator for each task.

#### Scenario: User sees an updated list with completion markers
- **WHEN** the user chooses to view the tasks
- **THEN** the application prints each task with its number and a readable status marker

### Requirement: Completion flow updates the selected task
Selecting the complete option SHALL prompt the user for a task number and update the selected task to a completed state.

#### Scenario: User marks a task as complete
- **WHEN** the user selects complete and enters a valid task number
- **THEN** the chosen task changes to completed and the updated status is displayed

### Requirement: Delete flow removes the selected task from memory
Selecting the delete option SHALL prompt the user for a task number and remove the selected task from the list.

#### Scenario: User removes an existing task
- **WHEN** the user selects delete and chooses a valid task number
- **THEN** the matching task is removed from the in-memory list

### Requirement: Menu loop continues until explicit exit
The menu loop SHALL repeat until the user explicitly chooses to exit.

#### Scenario: Repeated command loop
- **WHEN** the user completes a valid action and does not choose exit
- **THEN** the menu reappears and processing continues

### Requirement: Invalid menu selections are rejected gracefully
Invalid menu selections SHALL be rejected gracefully with a clear error message and without terminating the program.

#### Scenario: Invalid menu values do not crash the app
- **WHEN** the user enters a number outside the valid range or an unsupported option
- **THEN** the app prints a clear error message and returns to the menu

### Requirement: Invalid task numbers are handled gracefully
Invalid task numbers SHALL be handled gracefully with a clear error message and without terminating the program.

#### Scenario: Out-of-range task selection is rejected
- **WHEN** the user selects a task number that is not in the current list
- **THEN** the app prints a clear message and waits for another valid choice

### Requirement: Non-numeric input is rejected without crashing
Non-numeric input for menu choices and task selections SHALL be handled gracefully with a clear error message and without terminating the program.

#### Scenario: Alphabetic or blank input is rejected
- **WHEN** the user types letters, empty strings, or invalid numeric values
- **THEN** the program shows a friendly error and remains active

### Requirement: Standard library-only implementation
The application SHALL use only the Python standard library.

#### Scenario: No external dependency is required
- **WHEN** the program runs in the terminal
- **THEN** it does not require any third-party package or database dependency

### Requirement: Single-file implementation constraint
The application SHALL keep all logic within one Python file and shall not rely on a database or any external package.

#### Scenario: Single-file delivery is preserved
- **WHEN** the implementation is reviewed
- **THEN** all logic remains in a single Python file at the project root

### Requirement: Add task and list view are immediately observable to users
The system SHALL allow a user to add tasks and see them listed immediately.

#### Scenario: Immediate visibility after add
- **WHEN** the user adds a task and immediately chooses the view option
- **THEN** the newly created task appears in the list without restarting the program

### Requirement: Completing a task updates the displayed status
The system SHALL allow a user to complete a task and see the updated status in the task list.

#### Scenario: Task completion is reflected in the list
- **WHEN** the user marks a task complete
- **THEN** the task appears with a completed status marker in the list

### Requirement: Delete action removes a task from the list
The system SHALL allow a user to delete a task and confirm it is removed.

#### Scenario: Deletion confirmation is clear and effective
- **WHEN** the user deletes a task
- **THEN** the task is removed from the list and no longer appears in subsequent views

### Requirement: Invalid input does not terminate the session
The system SHALL produce a user-friendly message for an invalid menu option or invalid task number and return control to the menu.

#### Scenario: Recovery after misuse
- **WHEN** the user enters an invalid menu choice or task number
- **THEN** the app displays a user-friendly message and returns to the main menu without crashing

### Requirement: Blank and alphabetic input is handled without program termination
The system SHALL not crash when the user enters alphabetic or blank input.

#### Scenario: Blank and nonnumeric values are tolerated safely
- **WHEN** the user provides alphabetic or empty input at the menu or task selection prompts
- **THEN** the app handles the input safely and prompts again instead of exiting

### Requirement: Exit is explicit and single-path
The application SHALL exit only when the user selects the exit option.

#### Scenario: Program remains active until the user exits
- **WHEN** the user performs other actions in the loop
- **THEN** the application continues running and does not exit prematurely
