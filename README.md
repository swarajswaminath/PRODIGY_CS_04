Simple Keylogger
This simple keylogger records and logs keystrokes, focusing on logging the keys pressed and saving them to a file. The application uses the pynput library to monitor keyboard events and logs both character keys and special keys (like Shift, Ctrl, etc.).

Features
Capture all keystrokes.
Log the recorded keystrokes to a file(keylog.txt).
Stop logging when the esc key is pressed.
Ensure ethical considerations and permissions are in place.
Requirements
pynput Library: The code imports the Listener class from the pynput.keyboard module, which is part of the pynput library. You can install the pynput library using pip, the Python package manager.
pip install pynput
2.Python: The program is written in Python, so you'll need a Python interpreter installed on your system. If not, follow the instructions below to install it.

sudo apt install python3
How To Use
1.Clone the repository:

https://github.com/swarajswaminath/PRODIGY_CS_04.git
2.Navigate to the Directory:

cd PRODIGY_CS_04
3.Run the Script

python3 Keylogger.py
