import os

class DirectoryManager:
    def __init__(self, ai_model=None):
        """
        Initialize the DirectoryManager.
        :param ai_model: An optional AIModel instance for AI-powered functionalities.
        """
        self.directory_entries = []
        self.ai_model = ai_model

    def add_entry(self, entry):
        """
        Add an entry to the directory entries list.
        :param entry: The entry to add.
        """
        self.directory_entries.append(entry)

    def remove_entry(self, entry):
        """
        Remove an entry from the directory entries list.
        :param entry: The entry to remove.
        """
        if entry in self.directory_entries:
            self.directory_entries.remove(entry)

    def update_entry(self, old_entry, new_entry):
        """
        Update an existing entry in the directory entries list.
        :param old_entry: The entry to update.
        :param new_entry: The new entry to replace the old one.
        """
        if old_entry in self.directory_entries:
            index = self.directory_entries.index(old_entry)
            self.directory_entries[index] = new_entry

    def list_entries(self):
        """
        List all directory entries.
        :return: A list of directory entries.
        """
        return self.directory_entries

    def scan_directory(self, path):
        """
        Scan the directory and return a list of files.
        :param path: Path to the directory.
        :return: List of file paths.
        """
        try:
            supported_files = []
            for f in os.listdir(path):
                file_path = os.path.join(path, f)
                if os.path.isfile(file_path) and os.path.splitext(f)[1] in Config.SUPPORTED_FILE_TYPES:
                    supported_files.append(file_path)
            print(f"Supported files found: {supported_files}")  # Debugging line
            return supported_files
        except FileNotFoundError:
            print(f"Error: Directory '{path}' not found.")
            return []
        except PermissionError:
            print(f"Error: Permission denied for directory '{path}'.")
            return []

    def process_files(self, files):
        """
        Process the files using the AI model.
        :param files: List of file paths to process.
        """
        if not self.ai_model:
            print("No AI model integrated. Skipping AI processing.")
            return

        print(f"Processing {len(files)} files with AI model...")
        for file in files:
            # Placeholder for feature extraction logic
            print(f"Processing file: {file}")
            # Example: Use AIModel for predictions (replace `features` with actual extracted features)
            # features = extract_features(file)  # Implement feature extraction logic
            # predictions = self.ai_model.predict(features)
            # print(f"Predictions for {file}: {predictions}")

    def run(self):
        """
        Start the directory management process.
        """
        directory_path = input("Enter the directory path to manage: ")
        files = self.scan_directory(directory_path)
        if files:
            print(f"Found {len(files)} files in {directory_path}.")
            self.process_files(files)
        else:
            if os.path.exists(directory_path):
                print(f"No files found in the directory '{directory_path}'.")
            else:

                print("No files found or an error occurred.")
    def create_file(self, directory_path, file_name, content=""):
        """
        Create a file in the specified directory.
        :param directory_path: Path to the directory where the file will be created.
        :param file_name: Name of the file to create.
        :param content: Content to write to the file (optional).
        """
        try:
            # Ensure the directory exists
            if not os.path.exists(directory_path):
                os.makedirs(directory_path)  # Create the directory if it doesn't exist

            # Create the file with the specified content
            file_path = os.path.join(directory_path, file_name)
            with open(file_path, "w") as file:
                file.write(content)
            print(f"File '{file_name}' created successfully in '{directory_path}'.")
        except Exception as e:
            print(f"Error creating file: {e}")
    def remove_file(self, file_path):
        """
        Remove a file from the specified path.
        :param file_path: Path to the file to be removed.
        """
        try:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"File '{file_path}' removed successfully.")
            else:
                print(f"File '{file_path}' does not exist.")
        except Exception as e:
            print(f"Error removing file: {e}")
