import os
from datetime import datetime

NOTES_FILE = "notes.txt"

def add_note():
    note = input("Enter your note: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(NOTES_FILE, "a") as file:
        file.write(f"[{timestamp}] {note}\n")
    print("Note added with timestamp!\n")

def view_notes():
    if not os.path.exists(NOTES_FILE):
        print("No notes found!\n")
        return

    with open(NOTES_FILE, "r") as file:
        notes = file.readlines()

    if notes:
        print("\nYour Notes:")
        for idx, note in enumerate(notes, start=1):
            print(f"{idx}. {note.strip()}")
    else:
        print("No notes found!")
    print()

def delete_note():
    view_notes()
    try:
        note_number = int(input("Enter the note number to delete: "))
        with open(NOTES_FILE, "r") as file:
            notes = file.readlines()

        if 0 < note_number <= len(notes):
            deleted = notes.pop(note_number - 1)
            with open(NOTES_FILE, "w") as file:
                file.writelines(notes)
            print(f"Deleted note: {deleted.strip()}\n")
        else:
            print("Invalid note number!\n")
    except ValueError:
        print("Please enter a valid number!\n")

def main():
    while True:
        print("==== NOTES APP ====")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Delete Note")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_note()
        elif choice == "4":
            print("Exiting the Notes App. Goodbye!")
            break
        else:
            print("Invalid option! Try again.\n")

if __name__ == "__main__":
    main()
