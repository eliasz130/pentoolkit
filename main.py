#Imports
import platform
import subprocess
import os

#Defs
def run_file(file_path):
    try:
        if platform.system() == "Windows":
            os.system(file_path)  # Use os.system for .bat or executables
        else:
            subprocess.run(file_path, shell=True)  # Use subprocess for shell scripts
    except Exception as e:
        print(f"Error running the file: {e}")

def main():
    # Detect the current operating system
    current_os = platform.system()

    # Define paths to files based on the operating system
    if current_os == "Windows":
        file_to_run = "C:\\pentoolkit\\windows\\main.py"
    elif current_os == "Linux":
        file_to_run = "/pentoolkit/linux/main.py"
    elif current_os == "Darwin":  # macOS
        file_to_run = "/pentoolkit/main.py"
    else:
        print(f"Unsupported OS: {current_os}")
        return

    # Run the file if a valid path is found
    if os.path.exists(file_to_run):
        print(f"Running {file_to_run} on {current_os}")
        run_file(file_to_run)
    else:
        print(f"File does not exist: {file_to_run}")
#Run
if __name__ == "__main__":
    main()
