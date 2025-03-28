# This file is the entry point of the application for the AI-powered directory management system.

from directory.manager import DirectoryManager
from ai.model import AIModel
from config.settings import Settings

def main():
    # Initialize settings
    settings = Settings()
    print("Model Parameters:", settings.model_parameters)  # Example usage of settings

    # Initialize the AI model
    ai_model = AIModel()

    # Train or load the AI model
    print("\nInitializing AI model...")
    try:
        # Attempt to load a pre-trained model
        ai_model.load_model("model.pkl")
        print("AI model loaded successfully.")
    except FileNotFoundError:
        print("No pre-trained model found. Training a new model...")
        # Example training data (replace with actual data)
        X_train = [[1, 2], [3, 4], [5, 6]]
        y_train = [0, 1, 0]
        ai_model.train((X_train, y_train))
        ai_model.save_model("model.pkl")
        print("AI model trained and saved successfully.")

    # Initialize the directory manager with the AI model
    directory_manager = DirectoryManager(ai_model)

    # Menu for directory management
    while True:
        print("\nDirectory Management System")
        print("1. Add an entry")
        print("2. Remove an entry")
        print("3. Update an entry")
        print("4. List all entries")
        print("5. Run directory management system")
        print("6. Exit")
        print("7. Create a file")
        print("8. Remove a file")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add an entry
            entry = input("Enter the path to add: ")
            directory_manager.add_entry(entry)
            print(f"Entry '{entry}' added successfully.")
        elif choice == "2":
            # Remove an entry
            entry = input("Enter the entry to remove: ")
            directory_manager.remove_entry(entry)
            print(f"Entry '{entry}' removed successfully (if it existed).")
        elif choice == "3":
            # Update an entry
            old_entry = input("Enter the entry to update: ")
            new_entry = input("Enter the new entry: ")
            directory_manager.update_entry(old_entry, new_entry)
            print(f"Entry '{old_entry}' updated to '{new_entry}' (if it existed).")
        elif choice == "4":
            # List all entries
            entries = directory_manager.list_entries()
            if entries:
                print("Directory Entries:")
                for i, entry in enumerate(entries, start=1):
                    print(f"{i}. {entry}")
            else:
                print("No entries found.")
        elif choice == "5":
            # Run the directory management system
            print("Starting the directory management system...")
            directory_manager.run()
        elif choice == "6":
            # Exit the program
            print("Exiting the system. Goodbye!")
            break
        if choice == "7":
            # Create a file
            directory_path = input("Enter the directory path: ")
            file_name = input("Enter the file name (e.g., example.txt): ")
            content = input("Enter the content for the file (leave blank for an empty file): ")
            directory_manager.create_file(directory_path, file_name, content)
       
        if choice == "8":
        # Remove a file
            file_path = input("Enter the full path of the file to remove: ")
            directory_manager.remove_file(file_path)
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
