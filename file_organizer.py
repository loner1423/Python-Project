"""
File Organizer Script
Run: python file_organizer.py <directory>
Sorts files into subfolders by extension.
"""
import os, sys, shutil, pathlib

def organize(folder):
    folder = pathlib.Path(folder)
    for item in folder.iterdir():
        if item.is_file():
            ext = item.suffix.lower().lstrip(".") or "no_ext"
            target = folder / ext
            target.mkdir(exist_ok=True)
            shutil.move(str(item), str(target / item.name))
    print("Organized:", folder)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python file_organizer.py <directory>")
        sys.exit(1)
    organize(sys.argv[1])
