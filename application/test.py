import tkinter as tk
from wellbeing import ride_score  # import the function from the other file

# --- Function connected to the button ---
def process_input():
    user_text = entry.get()               # Get input from Entry widget
    score = ride_score(user_text)         # Call the function from wellbeing.py
    output_label.config(text=f"Ride Score: {score}")  # Show result

# --- Tkinter window ---
root = tk.Tk()
root.title("Ride Score Calculator")
root.geometry("300x150")

# Widgets
tk.Label(root, text="Enter ride duration (minutes):").pack(pady=5)
entry = tk.Entry(root, width=30)
entry.pack(pady=5)

tk.Button(root, text="Calculate Score", command=process_input).pack(pady=5)

output_label = tk.Label(root, text="", fg="blue")
output_label.pack(pady=10)

# Run the GUI
root.mainloop()
