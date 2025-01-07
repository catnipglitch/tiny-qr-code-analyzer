def copy_to_clipboard(text):
    import pyperclip
    pyperclip.copy(text)

def reset_fields(*fields):
    for field in fields:
        field.delete(0, 'end')  # Clear the input field
        field.insert(0, '')     # Reset to empty string

def show_messagebox(message):
    import tkinter as tk
    from tkinter import messagebox
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    messagebox.showinfo("Information", message)
    root.destroy()