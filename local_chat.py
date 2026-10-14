import tkinter as tk
from datetime import datetime
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


class LocalChatApp:
    """Simple local chat application for two users."""

    def __init__(self, root: tk.Tk) -> None:
        """Create and configure chat widgets."""
        self.root = root
        self.root.title("Local Chat")
        self.root.geometry("600x500")

        title_label = tk.Label(
            root,
            text="Local Chat",
            font=("Arial", 16, "bold"),
        )
        title_label.pack(pady=(15, 10))

        self.chat_area = ScrolledText(
            root,
            width=65,
            height=18,
            state="disabled",
            wrap="word",
        )
        self.chat_area.pack(
            padx=15,
            pady=10,
            fill="both",
            expand=True,
        )

        controls_frame = tk.Frame(root)
        controls_frame.pack(
            padx=15,
            pady=10,
            fill="x",
        )

        self.user_box = ttk.Combobox(
            controls_frame,
            values=("User 1", "User 2"),
            state="readonly",
            width=10,
        )
        self.user_box.current(0)
        self.user_box.pack(
            side="left",
            padx=(0, 10),
        )

        self.message_entry = tk.Entry(
            controls_frame,
        )
        self.message_entry.pack(
            side="left",
            fill="x",
            expand=True,
            padx=(0, 10),
        )

        send_button = tk.Button(
            controls_frame,
            text="Send",
            command=self.send_message,
        )
        send_button.pack(side="left")

        clear_button = tk.Button(
            root,
            text="Clear chat",
            command=self.clear_chat,
        )
        clear_button.pack(pady=(0, 15))

        self.message_entry.bind(
            "<Return>",
            self.send_message,
        )

        self.message_entry.focus()

    def send_message(self, event: object = None) -> None:
        """Add a message from the selected user to the chat."""
        del event

        user = self.user_box.get()
        message = self.message_entry.get().strip()

        if not message:
            return

        current_time = datetime.now().strftime("%H:%M:%S")
        chat_message = f"[{current_time}] {user}: {message}\n"

        self.chat_area.config(state="normal")
        self.chat_area.insert("end", chat_message)
        self.chat_area.config(state="disabled")
        self.chat_area.see("end")

        self.message_entry.delete(0, "end")

    def clear_chat(self) -> None:
        """Remove all messages from the chat."""
        self.chat_area.config(state="normal")
        self.chat_area.delete("1.0", "end")
        self.chat_area.config(state="disabled")


def create_app() -> tk.Tk:
    """Create the main window and initialize the local chat."""
    root = tk.Tk()
    LocalChatApp(root)
    return root


if __name__ == "__main__":
    app = create_app()
    app.mainloop()