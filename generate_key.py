from cryptography.fernet import Fernet

# Generate an encryption key
key = Fernet.generate_key()

# Save the key to a file securely
with open("key.key", "wb") as key_file:
    key_file.write(key)

print("Encryption key generated and saved as 'key.key'. Keep this file secure!")
