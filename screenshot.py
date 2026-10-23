import tkinter as tk
from PIL import ImageGrab
from datetime import datetime


def take_screenshot():
    # Take screenshot
    screenshot = ImageGrab.grab()

    # Create filename using current date and time
    current_time = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"screenshot_{current_time}.png"

    # Save screenshot
    screenshot.save(filename)

    # Show status in the Tkinter window
    status_label.config(text=f"Saved: {filename}")


# Create Tkinter window
root = tk.Tk()
root.title("Screenshot Tool")
root.geometry("400x200")

# Button
screenshot_button = tk.Button(
    root,
    text="Take Screenshot",
    command=take_screenshot,
    font=("Arial", 14)
)
screenshot_button.pack(pady=40)

# Status label
status_label = tk.Label(root, text="Click the button to take a screenshot")
status_label.pack()

# Start Tkinter
root.mainloop()
