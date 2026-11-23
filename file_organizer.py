import os
import shutil
import time

# Terminal colors
GREEN = "\033[92m"
RED = "\033[91m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# Dictionary mapping folder names to file extensions
FILE_CATEGORIES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".xlsx", ".csv", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Audio": [".mp3", ".wav", ".aac", ".ogg"],
    "Archives": [".zip", ".tar", ".gz", ".rar", ".7z"],
    "Code": [".py", ".js", ".html", ".css", ".json"]
}


def get_category(extension):
    """Finds which category folder a file extension belongs to."""
    for category, extensions in FILE_CATEGORIES.items():
        if extension in extensions:
            return category
    return "Others"


def create_test_folder():
    """Creates a sample messy folder with dummy files for safe testing."""
    test_dir = "messy_test_folder"
    os.makedirs(test_dir, exist_ok=True)

    sample_files = [
        "vacation_photo.jpg",
        "screenshot_2026.png",
        "project_report.pdf",
        "budget_sheet.xlsx",
        "lecture_recording.mp4",
        "podcast_episode.mp3",
        "website_backup.zip",
        "notes.txt"
    ]

    for filename in sample_files:
        file_path = os.path.join(test_dir, filename)
        with open(file_path, "w") as f:
            f.write("Sample file created for testing the Python File Organizer.")

    print(GREEN + f"\n✅ Created '{test_dir}' with {len(sample_files)} messy files!" + RESET)


def organize_folder(folder_path):
    """Scans a folder and moves every file into its matching category folder."""
    # Expands '~' so paths like '~/Downloads' work automatically
    folder_path = os.path.expanduser(folder_path)

    if not os.path.exists(folder_path):
        print(RED + f"\n❌ Folder not found: '{folder_path}'" + RESET)
        return

    moved_count = 0

    for filename in os.listdir(folder_path):
        # Never move this script itself
        if filename == "file_organizer.py":
            continue

        source_path = os.path.join(folder_path, filename)

        # Skip existing subfolders
        if os.path.isdir(source_path):
            continue

        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Skip files with no extension
        if extension == "":
            continue

        category = get_category(extension)
        destination_folder = os.path.join(folder_path, category)
        os.makedirs(destination_folder, exist_ok=True)

        destination_path = os.path.join(destination_folder, filename)
        shutil.move(source_path, destination_path)

        print(f"📦 Moved: {filename}  -->  {CYAN}{category}/{RESET}")
        moved_count = moved_count + 1

    print("\n==========================================")
    if moved_count == 0:
        print(YELLOW + "✨ Nothing to organize—this folder is already clean!" + RESET)
    else:
        print(GREEN + f"🎉 Done! Organized {moved_count} files automatically." + RESET)
    print("==========================================")


print("\n==========================================")
print(CYAN + "   🗂️  AUTOMATED FILE ORGANIZER 🗂️" + RESET)
print("==========================================")

while True:
    print("\nChoose an option:")
    print("1. 🧪 Create a sample messy folder (safe test)")
    print("2. 🧹 Organize a folder")
    print("3. 🚪 Exit")

    choice = input("\nEnter choice (1-3): ").strip()

    if choice == "1":
        create_test_folder()

    elif choice == "2":
        target = input("📁 Enter folder name or path (e.g. messy_test_folder or ~/Downloads): ").strip()
        print("Scanning and organizing files...")
        time.sleep(0.5)
        organize_folder(target)

    elif choice == "3":
        print(CYAN + "\n👋 Goodbye! Keep your folders clean!\n" + RESET)
        break

    else:
        print(RED + "❌ Invalid choice. Please enter 1, 2, or 3." + RESET)