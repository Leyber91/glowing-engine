import subprocess
import tkinter as tk
import importlib
from tkinter import filedialog

# Check if Pyperclip is installed
try:
    import pyperclip
except ImportError:
    # Pyperclip is not installed, install it
    print("Pyperclip is not installed, installing...")
    subprocess.run(["pip", "install", "pyperclip"])
    importlib.reload(pyperclip)

# Check if Pandoc is installed
result = subprocess.run(["which", "pandoc"], stdout=subprocess.PIPE)

if result.stdout:
    # Pandoc is installed
    print("Pandoc is already installed")
else:
    # Pandoc is not installed, run the install_pandoc.py script
    print("Pandoc is not installed, installing...")
    subprocess.run(["python", "Tool_installer/install_pandoc.py"])

# Create a GUI window
root = tk.Tk()
root.withdraw()

# Open a file selection dialog to choose the input file
input_file = filedialog.askopenfilename(title="Select the input file")

# Get the input file's directory and name
input_dir = input_file[:input_file.rindex("/")+1]
input_name = input_file[input_file.rindex("/")+1:]

# Generate the output file path and name
output_path = input_dir + input_name[:input_name.rindex(".")] + ".md"

# Check if the output file already exists
if not os.path.exists(output_path):
    # Convert the input file to Markdown
    subprocess.run(["pandoc", "-s", input_file, "-o", output_path])

# Read the output file
with open(output_path, "r") as f:
    output_content = f.read()

# Copy the output file's content to the clipboard
pyperclip.copy(output_content)

# Print a message to
