import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import ImageGrab


def take_screenshot():
    try:
        # Take screenshot
        screenshot = ImageGrab.grab()

        # Ask where to save the screenshot
        file_path = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG Image", "*.png")]
        )

        if file_path:
            screenshot.save(file_path)
            messagebox.showinfo("Success", "Screenshot saved successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to take screenshot:\n{e}")


# Create the main window
root = tk.Tk()
root.title("Screenshot Tool")
root.geometry("500x300")

# Create button
btn = tk.Button(
    root,
    text="Click the button to take a screenshot",
    command=take_screenshot,
    font=("Arial", 14),
    bg="#00c853",
    fg="white"
)
btn.pack(pady=50)

# Start the Tkinter event loop
root.mainloop()
