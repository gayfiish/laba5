import tkinter as tk
from tkinter import filedialog
from pathlib import Path


def choose_file(label: tk.Label) -> None:
    """Open a file dialog and display the selected file path."""
    file_path = filedialog.askopenfilename(
        title="Select a file",
        filetypes=(
            ("Text files", "*.txt"),
            ("Python files", "*.py"),
            ("All files", "*.*"),
        ),
    )

    if file_path:
        path = Path(file_path)
        label.config(
            text=f"Selected file:\n{path.name}"
        )
    else:
        label.config(text="No file selected.")


def create_app() -> tk.Tk:
    """Create and configure the file dialog application."""
    root = tk.Tk()
    root.title("File Dialog")
    root.geometry("450x220")

    title_label = tk.Label(
        root,
        text="Choose a file",
        font=("Arial", 14),
    )
    title_label.pack(pady=(30, 10))

    result_label = tk.Label(
        root,
        text="No file selected.",
        font=("Arial", 11),
    )
    result_label.pack(pady=10)

    choose_button = tk.Button(
        root,
        text="Select file",
        command=lambda: choose_file(result_label),
    )
    choose_button.pack(pady=10)

    return root


if __name__ == "__main__":
    app = create_app()
    app.mainloop()