import os
import platform
import urllib.request

# Determine the operating system and architecture
system = platform.system()
architecture = platform.architecture()[0]

# Choose the appropriate installer URL based on the operating system and architecture
if system == "Windows":
    if architecture == "64bit":
        url = "https://github.com/jgm/pandoc/releases/download/2.11.4/pandoc-2.11.4-windows-x86_64.msi"
    else:
        url = "https://github.com/jgm/pandoc/releases/download/2.11.4/pandoc-2.11.4-windows-i386.msi"
elif system == "Darwin":
    url = "https://github.com/jgm/pandoc/releases/download/2.11.4/pandoc-2.11.4-macOS.pkg"
elif system == "Linux":
    if architecture == "64bit":
        url = "https://github.com/jgm/pandoc/releases/download/2.11.4/pandoc-2.11.4-linux-amd64.deb"
    else:
        url = "https://github.com/jgm/pandoc/releases/download/2.11.4/pandoc-2.11.4-linux-i386.deb"

# Download the installer
print("Downloading Pandoc installer...")
urllib.request.urlretrieve(url, "pandoc-installer.msi")

# Install Pandoc
if system == "Windows":
    os.system("msiexec /i pandoc-installer.msi /qn")
elif system == "Darwin":
    os.system("open pandoc-installer.pkg")
elif system == "Linux":
    os.system("sudo dpkg -i pandoc-installer.deb")

# Remove the installer file
os.remove("pandoc-installer.msi")

# Print a message to confirm the installation
print("Pandoc has been successfully installed.")
