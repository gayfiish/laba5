import tkinter as tk
from tkinter import ttk


def update_progress(
    root: tk.Tk,
    progress_bar: ttk.Progressbar,
    label: tk.Label,
    start_button: tk.Button,
    value: int = 0,
) -> None:
    """Gradually update the progress bar from 0 to 100."""
    progress_bar["value"] = value
    label.config(text=f"Progress: {value}%")

    if value < 100:
        root.after(
            100,
            update_progress,
            root,
            progress_bar,
            label,
            start_button,
            value + 5,
        )
    else:
        label.config(text="Completed!")
        start_button.config(state="normal")


def start_progress(
    root: tk.Tk,
    progress_bar: ttk.Progressbar,
    label: tk.Label,
    start_button: tk.Button,
) -> None:
    """Start progress bar animation."""
    progress_bar["value"] = 0
    start_button.config(state="disabled")
    update_progress(root, progress_bar, label, start_button)


def create_app() -> tk.Tk:
    """Create and configure the progress bar application."""
    root = tk.Tk()
    root.title("Progress Bar")
    root.geometry("400x200")

    label = tk.Label(
        root,
        text="Progress: 0%",
        font=("Arial", 12),
    )
    label.pack(pady=(30, 10))

    progress_bar = ttk.Progressbar(
        root,
        orient="horizontal",
        length=300,
        mode="determinate",
        maximum=100,
    )
    progress_bar.pack(pady=10)

    start_button = tk.Button(
        root,
        text="Start",
    )
    start_button.config(
        command=lambda: start_progress(
            root,
            progress_bar,
            label,
            start_button,
        )
    )
    start_button.pack(pady=10)

    return root


if __name__ == "__main__":
    app = create_app()
    app.mainloop()