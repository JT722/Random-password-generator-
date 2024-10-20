import random
import string
import pyperclip
import tkinter as tk
from tkinter import messagebox

# Function to generate a random password based on user criteria
def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = string.ascii_lowercase
    
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation
    
    if not characters:
        return "No valid character types selected!"
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Function to handle button click
def generate():
    length = int(length_entry.get())
    use_uppercase = uppercase_var.get()
    use_numbers = numbers_var.get()
    use_symbols = symbols_var.get()

    password = generate_password(length, use_uppercase, use_numbers, use_symbols)
    result_label.config(text=password)

def copy_to_clipboard():
    password = result_label.cget("text")
    pyperclip.copy(password)
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# Create the GUI
root = tk.Tk()
root.title("Secure Password Generator")

# Length input
length_label = tk.Label(root, text="Password Length:")
length_label.pack()
length_entry = tk.Entry(root)
length_entry.pack()

# Options
uppercase_var = tk.BooleanVar()
numbers_var = tk.BooleanVar()
symbols_var = tk.BooleanVar()

uppercase_check = tk.Checkbutton(root, text="Include Uppercase", variable=uppercase_var)
uppercase_check.pack()
numbers_check = tk.Checkbutton(root, text="Include Numbers", variable=numbers_var)
numbers_check.pack()
symbols_check = tk.Checkbutton(root, text="Include Symbols", variable=symbols_var)
symbols_check.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate)
generate_button.pack()

# Display generated password
result_label = tk.Label(root, text="")
result_label.pack()

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

# Start the GUI event loop
root.mainloop()
