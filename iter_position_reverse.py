import tkinter as tk

def process_input():
    s = entry.get()
    
    out, current = [], len(s) // 2 

    while True:
        for i in range(len(s) - current):
            left, center, right = s[:i], s[i : i + current], s[i + current :]

            if left + right == center:
                out.append(i)
                s, current = center, len(center) // 2
                break
        else:
            break

    result_label.config(text=f"Output: {out[::-1]}, Remaining: {s}")

# Create the main window
root = tk.Tk()
root.title("String Processing")

# Create and place widgets
label = tk.Label(root, text="Enter the string:")
label.pack(pady=10)

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

process_button = tk.Button(root, text="Process", command=process_input)
process_button.pack(pady=10)

result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
