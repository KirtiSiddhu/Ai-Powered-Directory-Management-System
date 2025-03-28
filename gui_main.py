import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
from directory.manager import DirectoryManager
from ai.model import AIModel
from config.settings import Settings
import os

class DirectoryManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("AI-Powered Directory Management System")
        self.root.geometry("700x600")
        self.root.configure(bg="#2c3e50")  # Dark background color

        # Initialize settings and AI model
        self.settings = Settings()
        self.ai_model = AIModel()
        self.directory_manager = DirectoryManager(self.ai_model)

        # Load or train the AI model
        self.initialize_ai_model()

        # Create GUI components
        self.create_widgets()

    def initialize_ai_model(self):
        try:
            self.ai_model.load_model("model.pkl")
            messagebox.showinfo("AI Model", "AI model loaded successfully.")
        except FileNotFoundError:
            messagebox.showwarning("AI Model", "No pre-trained model found. Training a new model...")
            X_train = [[1, 2], [3, 4], [5, 6]]
            y_train = [0, 1, 0]
            self.ai_model.train((X_train, y_train))
            self.ai_model.save_model("model.pkl")
            messagebox.showinfo("AI Model", "AI model trained and saved successfully.")

    def create_widgets(self):
        # Style customization
        style = ttk.Style()
        style.configure("TButton", font=("Helvetica", 12, "bold"), padding=10)
        style.map("TButton", background=[("active", "#c0392b")])  # Hover effect

        # Title Label
        title_label = ttk.Label(self.root, text="Directory Management System", font=("Helvetica", 18, "bold"), background="#2c3e50", foreground="white")
        title_label.pack(pady=10)

        # Frame for buttons
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=10)

        # Buttons with animations
        button_texts = [
            ("➕ Add Entry", self.add_entry),
            ("❌ Remove Entry", self.remove_entry),
            ("🔄 Update Entry", self.update_entry),
            ("📂 List Entries", self.list_entries),
            ("⚙️ Run Directory Management", self.run_management),
            ("📄 Create File", self.create_file),
            ("🗑️ Remove File", self.remove_file),
            ("🚪 Exit", self.root.quit)
        ]

        for text, command in button_texts:
            btn = ttk.Button(button_frame, text=text, command=command, style="TButton")
            btn.pack(fill=tk.X, pady=5, padx=20)

    def add_entry(self):
        entry = filedialog.askdirectory(title="Select Directory to Add")
        if entry:
            self.directory_manager.add_entry(entry)
            messagebox.showinfo("Add Entry", f"Entry '{entry}' added successfully.")

    def remove_entry(self):
        entry = filedialog.askdirectory(title="Select Directory to Remove")
        if entry:
            self.directory_manager.remove_entry(entry)
            messagebox.showinfo("Remove Entry", f"Entry '{entry}' removed successfully.")

    def update_entry(self):
        old_entry = filedialog.askdirectory(title="Select Directory to Update")
        if old_entry:
            new_entry = filedialog.askdirectory(title="Select New Directory")
            if new_entry:
                self.directory_manager.update_entry(old_entry, new_entry)
                messagebox.showinfo("Update Entry", f"Entry '{old_entry}' updated to '{new_entry}'.")

    def list_entries(self):
        entries = self.directory_manager.list_entries()
        if entries:
            messagebox.showinfo("List Entries", "\n".join(entries))
        else:
            messagebox.showinfo("List Entries", "No entries found.")

    def run_management(self):
        directory_path = filedialog.askdirectory(title="Select Directory to Manage")
        if directory_path:
            self.directory_manager.run()
            messagebox.showinfo("Run Management", f"Directory management completed for '{directory_path}'.")

    def create_file(self):
        directory_path = filedialog.askdirectory(title="Select Directory to Create File")
        if directory_path:
            file_name = simpledialog.askstring("Create File", "Enter the file name:")
            if file_name:
                content = simpledialog.askstring("Create File", "Enter the file content:")
                self.directory_manager.create_file(directory_path, file_name, content)
                messagebox.showinfo("Create File", f"File '{file_name}' created successfully.")

    def remove_file(self):
        file_path = filedialog.askopenfilename(title="Select File to Remove")
        if file_path:
            self.directory_manager.remove_file(file_path)
            messagebox.showinfo("Remove File", f"File '{file_path}' removed successfully.")

# Run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = DirectoryManagementApp(root)
    root.mainloop()

