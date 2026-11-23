# Python Automated File Organizer

A command-line automation script built with Python that declutters messy folders by sorting files into categorized subdirectories (`Images`, `Documents`, `Videos`, `Audio`, `Archives`, and `Code`) based on file extension.

## Features
- **Automatic Categorization:** Maps 30+ common file extensions into clean, organized folders.
- **Built-In Safe Test Mode:** Generates a sample `messy_test_folder` so users can preview the organizer safely before running it on personal directories.
- **Cross-Platform Path Handling:** Uses `os.path.join()` and `os.path.expanduser()` so shortcuts like `~/Downloads` work seamlessly.
- **Non-Destructive:** Skips existing subfolders and hidden/extensionless system files.

## How to Run
Make sure Python 3 is installed on your computer (no external packages required), then run:
```bash
python file_organizer.py
```

## What I Learned
- Navigating directories and creating folders with Python's **`os`** module
- Extracting file extensions cleanly using **`os.path.splitext()`**
- Moving files programmatically with **`shutil.move()`**
- Combining **dictionaries**, **functions**, and **loops** to solve a real-world workflow problem
