Simple Python Keylogger
This is a simple keylogger script written in Python using the pynput library. The keylogger captures keystrokes and logs them into a specified text file.

Features
Captures alphanumeric keystrokes.
Logs special keys with additional information.
Prerequisites
Python 3.x
pynput library (pip install pynput)
Usage
Clone the repository:

bash
Copy code
git clone(https://github.com/zacobrohan/Python-Keylogger-Project)
Navigate to the project directory:

bash
Copy code
cd keylogger
Run the script:

bash
Copy code
python keylogger.py
Enter the desired log file path when prompted. Press 'Enter' to use the default path (/home/kali/Desktop/keylogger_output.txt).

The keylogger will start, and you can stop it by pressing the 'Esc' key.

Configuration
The default log file path is /home/kali/Desktop/keylogger_output.txt. You can change this by providing a different path when prompted.

If the specified log file already exists, you will be prompted to either append to it or create a new file with a timestamp.

Important Note
This code is for educational purposes only. Make sure you have the right to monitor the activities you intend to log, and use it responsibly and legally.

License
This project is licensed under the MIT License.
