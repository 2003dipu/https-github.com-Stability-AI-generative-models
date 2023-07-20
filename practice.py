"""
import random
import string

def generate_cipher_key():
    chars = " " + string.punctuation + string.digits + string.ascii_letters
    chars = list(chars)
    key = chars.copy()
    random.shuffle(key)
    return chars, key

def encrypt_message(plain_text, chars, key):
    return "".join(key[chars.index(letter)] for letter in plain_text)

def decrypt_message(cipher_text, chars, key):
    return "".join(chars[key.index(letter)] for letter in cipher_text)

chars, key = generate_cipher_key()

# Encrypt
plain_text = input("Enter a message to encrypt: ")
cipher_text = encrypt_message(plain_text, chars, key)
print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# Decrypt
cipher_text = input("Enter a message to decrypt: ")
plain_text = decrypt_message(cipher_text, chars, key)
print(f"Encrypted message: {cipher_text}")
print(f"Original message: {plain_text}")
"""
# App
import random
import string
import tkinter as tk
from tkinter import messagebox

class EncryptionApp:
    def __init__(self):
        self.chars = " " + string.punctuation + string.digits + string.ascii_letters
        self.chars = list(self.chars)
        self.key = self.chars.copy()
        random.shuffle(self.key)

    def encrypt_message(self, plain_text):
        return "".join(self.key[self.chars.index(letter)] for letter in plain_text)

    def decrypt_message(self, cipher_text):
        return "".join(self.chars[self.key.index(letter)] for letter in cipher_text)

    def run(self):
        root = tk.Tk()
        root.title("Encryption App")

        def encrypt():
            plain_text = input_entry.get()
            if plain_text:
                cipher_text = self.encrypt_message(plain_text)
                output_label.config(text=cipher_text)
            else:
                messagebox.showwarning("Error", "Please enter a message.")

        def decrypt():
            cipher_text = input_entry.get()
            if cipher_text:
                plain_text = self.decrypt_message(cipher_text)
                output_label.config(text=plain_text)
            else:
                messagebox.showwarning("Error", "Please enter a message.")

        input_label = tk.Label(root, text="Enter a message:")
        input_label.pack()

        input_entry = tk.Entry(root)
        input_entry.pack()

        encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
        encrypt_button.pack()

        decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
        decrypt_button.pack()

        output_label = tk.Label(root, text="")
        output_label.pack()

        root.mainloop()

if __name__ == "__main__":
    app = EncryptionApp()
    app.run()






