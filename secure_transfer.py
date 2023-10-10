from cryptography.fernet import Fernet

def generate_key():
    """Generate an encryption key."""
    return Fernet.generate_key()

def encrypt_file_content(content, key):
    """Encrypt the content using the provided key."""
    cipher = Fernet(key)
    encrypted_content = cipher.encrypt(content.encode())
    return encrypted_content

def decrypt_file_content(encrypted_content, key):
    """Decrypt the content using the provided key."""
    cipher = Fernet(key)
    decrypted_content = cipher.decrypt(encrypted_content).decode()
    return decrypted_content

# Example Usage:
key = generate_key()
print(f"Generated Key: {key}")

original_content = "This is a secret message"
encrypted = encrypt_file_content(original_content, key)
print(f"Encrypted: {encrypted}")

decrypted = decrypt_file_content(encrypted, key)
print(f"Decrypted: {decrypted}")
