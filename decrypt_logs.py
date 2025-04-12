from cryptography.fernet import Fernet

# Load the encryption key
with open("key.key", "rb") as key_file:
    key = key_file.read()

# Initialize the Fernet cipher
cipher = Fernet(key)

# Decrypt and display the log entries
try:
    with open("keystrokes.log", "rb") as log_file:
        for line in log_file:
            decrypted_entry = cipher.decrypt(line.strip())
            print(decrypted_entry.decode())
except FileNotFoundError:
    print("No log file found!")
