import subprocess
import tkinter as tk
from tkinter import filedialog

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

# Prompt the user for the output file name
output_file = input("Enter the name of the output file: ")

# Run the pandoc command to convert the input file to Markdown
subprocess.run(["pandoc", "-s", input_file, "-o", output_file])

# Print a message to confirm the conversion
print(f"Successfully converted {input_file} to {output_file}")
