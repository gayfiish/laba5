import tkinter as tk

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def build_plot(
    figure: Figure,
    canvas: FigureCanvasTkAgg,
    entry: tk.Entry,
    result_label: tk.Label,
) -> None:
    """Build a quadratic function plot using the entered coefficient."""
    try:
        coefficient = float(entry.get())
    except ValueError:
        result_label.config(text="Error: enter a number.")
        return

    x_values = list(range(-10, 11))
    y_values = [
        coefficient * x**2
        for x in x_values
    ]

    figure.clear()

    axes = figure.add_subplot(111)
    axes.plot(x_values, y_values)
    axes.set_title(f"y = {coefficient}x²")
    axes.set_xlabel("x")
    axes.set_ylabel("y")
    axes.grid(True)

    canvas.draw()

    result_label.config(text="Graph updated.")


def create_app() -> tk.Tk:
    """Create and configure the matplotlib Tkinter application."""
    root = tk.Tk()
    root.title("Matplotlib in Tkinter")
    root.geometry("700x600")

    input_frame = tk.Frame(root)
    input_frame.pack(pady=10)

    label = tk.Label(
        input_frame,
        text="Coefficient a:",
        font=("Arial", 11),
    )
    label.pack(side="left", padx=5)

    entry = tk.Entry(
        input_frame,
        width=10,
    )
    entry.insert(0, "1")
    entry.pack(side="left", padx=5)

    result_label = tk.Label(
        root,
        text="",
        font=("Arial", 10),
    )
    result_label.pack()

    figure = Figure(
        figsize=(6, 4),
        dpi=100,
    )

    canvas = FigureCanvasTkAgg(
        figure,
        master=root,
    )
    canvas.get_tk_widget().pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10,
    )

    button = tk.Button(
        root,
        text="Build graph",
        command=lambda: build_plot(
            figure,
            canvas,
            entry,
            result_label,
        ),
    )
    button.pack(pady=(0, 15))

    build_plot(
        figure,
        canvas,
        entry,
        result_label,
    )

    return root


if __name__ == "__main__":
    app = create_app()
    app.mainloop()