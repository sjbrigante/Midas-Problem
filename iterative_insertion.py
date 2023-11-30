import tkinter as tk
from tkinter import font

def process_forward(initial, indexes):
    final = initial
    for index in indexes:
        final = final[:index] + final + final[index:]
    return final

def process_backwards_iterative(initial, indexes):
    final = initial
    removed_positions = []

    for index in reversed(indexes):
        chars_to_remove = len(final) // 2
        removed_positions.append(index)
        final = final[:index] + final[index + chars_to_remove:]

    return final, removed_positions

def on_process():
    initial_text = entry_initial.get()
    indexes_text = entry_indexes.get()

    try:
        indexes = [int(index) for index in indexes_text.split(',')]
    except ValueError:
        result_text_widget.delete(1.0, tk.END)
        result_text_widget.insert(tk.END, "Error: Invalid index format")
        return

    forward_result = process_forward(initial_text, indexes)
    _, removed_positions = process_backwards_iterative(forward_result, indexes)

    result_text_widget.delete(1.0, tk.END)
    result_text_widget.insert(tk.END, f"Output String:\n{forward_result}")
    result_length_var.set("Length of Output String: {}".format(len(forward_result)))
    position_list_var.set("Inserted Positions: {}".format(indexes))

# Create main window
root = tk.Tk()
root.title("String Processing Tool")

# Create fonts
label_font = font.Font(family="Helvetica", size=12, weight="bold")
entry_font = font.Font(family="Helvetica", size=12)
button_font = font.Font(family="Helvetica", size=12, weight="bold")

# Create widgets
label_initial = tk.Label(root, text="Initial String:", font=label_font)
entry_initial = tk.Entry(root, font=entry_font)

label_indexes = tk.Label(root, text="Indexes (comma-separated):", font=label_font)
entry_indexes = tk.Entry(root, font=entry_font)

result_text_widget = tk.Text(root, height=10, width=50, wrap=tk.WORD, font=entry_font)

result_length_var = tk.StringVar()
label_length = tk.Label(root, textvariable=result_length_var, font=label_font)

position_list_var = tk.StringVar()
label_positions = tk.Label(root, textvariable=position_list_var, font=label_font)

process_button = tk.Button(root, text="Process", command=on_process, font=button_font, bg="#4CAF50", fg="white")

# Arrange widgets in the layout
label_initial.pack(pady=5)
entry_initial.pack(pady=5)

label_indexes.pack(pady=5)
entry_indexes.pack(pady=5)

process_button.pack(pady=10)

result_text_widget.pack(pady=5)
label_length.pack(pady=5)
label_positions.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
