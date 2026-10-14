import tkinter as tk


def show_text(entry: tk.Entry, label: tk.Label) -> None:
    """Display text entered by the user."""
    text = entry.get().strip()

    if text:
        label.config(text=f"You entered: {text}")
    else:
        label.config(text="Please enter some text.")


def create_app() -> tk.Tk:
    """Create and configure the main application window."""
    root = tk.Tk()
    root.title("Text Input")
    root.geometry("400x200")

    instruction_label = tk.Label(
        root,
        text="Enter text:",
        font=("Arial", 12),
    )
    instruction_label.pack(pady=(20, 5))

    entry = tk.Entry(root, width=35)
    entry.pack(pady=5)

    result_label = tk.Label(
        root,
        text="",
        font=("Arial", 11),
    )
    result_label.pack(pady=10)

    button = tk.Button(
        root,
        text="Show text",
        command=lambda: show_text(entry, result_label),
    )
    button.pack(pady=5)

    return root


if __name__ == "__main__":
    app = create_app()
    app.mainloop()