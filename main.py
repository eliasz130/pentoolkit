#!/usr/bin/env python3
import platform
import subprocess
import os

def run_file(file_path):
    try:
        if platform.system() == "Windows":
            os.system(file_path)
        else:
            subprocess.run(file_path, shell=True)
    except Exception as e:
        print(f"Error running the file: {e}")

def main():
    os_paths = {
        "Windows": "\\windows\\main.py",
        "Linux": "linux/main.py",
        "Darwin": "mac/main.py"
    }

    current_os = platform.system()
    file_to_run = os_paths.get(current_os)

    if file_to_run and os.path.exists(file_to_run):
        print(f"Running {file_to_run} on {current_os}")
        run_file(file_to_run)
    else:
        print(f"Unsupported OS or file does not exist: {current_os}")

if __name__ == "__main__":
    main()
