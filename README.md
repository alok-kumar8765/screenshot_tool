# Python Desktop Screenshot Utilities

A collection of simple, lightweight Python desktop applications built with **Tkinter** and **Pillow (PIL)** for capturing and saving screen snapshots.

This repository includes two variants designed for different user workflows:

1. **`screenshot.py`**: Quick One-Click Saver — Automatically timestamps and saves screenshots to the working directory without prompt delays.
2. **`ss.py`**: Save-As File Dialog Saver — Opens a system file dialog box so you can select the exact output location and file name.

---

## Features

| Feature | `screenshot.py` | `ss.py` |
| :--- | :--- | :--- |
| **Primary Action** | Instant timestamped save | File picker dialog (`Save As`) |
| **Output Location** | Working Directory | User-selected folder |
| **File Naming Format** | `screenshot_YYYY-MM-DD_HH-MM-SS.png` | Custom user naming |
| **UI Notifications** | Dynamic inline status label | System pop-up dialog (`messagebox`) |
| **Error Handling** | Basic | Try-Except block with alert dialogs |

---

## Requirements

Both scripts require Python 3.x and the `Pillow` (PIL) library for screen capture.

### Prerequisites & Dependencies

* **Python 3.x**
* **Tkinter** (Included by default in most standard Python installations)
* **Pillow** (`PIL`)

---

## Installation

1. **Clone or download this repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install required dependencies:**
   ```bash
   pip install pillow
   ```

---

## Usage Instructions

### 1. Automated Timestamp Tool (`screenshot.py`)

Best for rapid screenshot capture where you don't want to specify file paths each time.

* **Run the script:**
  ```bash
  python screenshot.py
  ```
* **How it works:**
  1. Click **Take Screenshot**.
  2. The full screen is captured.
  3. The image is saved automatically as `screenshot_YYYY-MM-DD_HH-MM-SS.png`.
  4. The status label on the application window updates with the filename.

---

### 2. Custom Save Location Tool (`ss.py`)

Best when you need full control over where screenshots are stored and what they are named.

* **Run the script:**
  ```bash
  python ss.py
  ```
* **How it works:**
  1. Click the green button (**Click the button to take a screenshot**).
  2. The full screen is captured.
  3. A file save dialog opens requesting a location and file name.
  4. Upon saving, a success message pop-up will confirm the operation.

---

## Code Comparison & Architecture

* **`ImageGrab.grab()`** from Pillow is used across both tools to capture full-screen images.
* **Tkinter GUI Loop:** Both tools use Tkinter event loops (`root.mainloop()`) to provide simple, non-blocking window controls.

---

## Troubleshooting

* **Tkinter missing on Linux/Ubuntu:**
  If you run into an error regarding `_tkinter`, install it via your package manager:
  ```bash
  sudo apt-get install python3-tk
  ```
* **Headless Systems:**
  `ImageGrab.grab()` requires an active graphical desktop environment (GUI). It will fail in purely headless server environments.

---

## License

This project is open-source and free to use under the MIT License.