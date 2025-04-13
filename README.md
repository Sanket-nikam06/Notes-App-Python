# Notes-App-Python
A simple command-line notes application written in Python that allows you to manage your notes efficiently.

## Features

- Add notes with automatic timestamps
- View all saved notes with their creation time
- Delete specific notes by their number
- Simple and intuitive command-line interface

## Requirements

- Python 3.x

## Installation

1. Clone or download this repository
2. Navigate to the project directory
3. No additional dependencies required - the app uses only Python standard library

## Usage

Run the application using Python:

```bash
python Notes.py
```

The app provides a menu with the following options:

1. **Add Note**: Enter your note text, and it will be saved with the current timestamp
2. **View Notes**: Display all saved notes with their timestamps
3. **Delete Note**: Remove a specific note by selecting its number
4. **Exit**: Close the application

## File Storage

Notes are stored in a text file (`notes.txt`) in the same directory as the application. Each note is saved with a timestamp in the format: `[YYYY-MM-DD HH:MM:SS] Note text`

## Example

```
==== NOTES APP ====
1. Add Note
2. View Notes
3. Delete Note
4. Exit
Choose an option: 1
Enter your note: Remember to buy groceries
Note added with timestamp!

Choose an option: 2
Your Notes:
1. [2025-02-20 15:30:45] Remember to buy groceries
```
