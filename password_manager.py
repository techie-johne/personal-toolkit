#!/usr/bin/env python3
"""
Simple Encrypted Password Manager
--------------------------------
A basic tool to store and retrieve passwords with AES encryption.
For educational purposes only.
"""
import base64
import os
import json
import getpass
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

class PasswordManager:
    def __init__(self, password_file="passwords.enc"):
        self.password_file = password_file
        self.passwords = {}
        self.key = None
    
    def initialize(self, master_password):
        # Generate a key from the master password
        salt = os.urandom(16)
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
        self.key = key
        
        # Save salt for future use
        with open("salt.bin", "wb") as salt_file:
            salt_file.write(salt)
        
        print("Password manager initialized successfully!")
    
    def load_key(self, master_password):
        # Load the salt
        try:
            with open("salt.bin", "rb") as salt_file:
                salt = salt_file.read()
        except FileNotFoundError:
            print("Error: Password manager not initialized.")
            return False
        
        # Regenerate the key
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(master_password.encode()))
        self.key = key
        return True
    
    def add_password(self, service, username, password):
        if not self.key:
            print("Error: Please unlock the password manager first")
            return
        
        if service not in self.passwords:
            self.passwords[service] = []
        
        self.passwords[service].append({
            "username": username,
            "password": password
        })
        self.save_passwords()
        print(f"Password for {service} added successfully!")
    
    def get_password(self, service):
        if not self.key:
            print("Error: Please unlock the password manager first")
            return
        
        if service in self.passwords:
            return self.passwords[service]
        else:
            print(f"No passwords found for {service}")
            return []
    
    def save_passwords(self):
        if not self.key:
            print("Error: Please unlock the password manager first")
            return
        
        # Encrypt passwords
        f = Fernet(self.key)
        encrypted_data = f.encrypt(json.dumps(self.passwords).encode())
        
        # Save to file
        with open(self.password_file, "wb") as password_file:
            password_file.write(encrypted_data)
    
    def load_passwords(self):
        if not self.key:
            print("Error: Please unlock the password manager first")
            return False
        
        try:
            with open(self.password_file, "rb") as password_file:
                encrypted_data = password_file.read()
            
            # Decrypt passwords
            f = Fernet(self.key)
            decrypted_data = f.decrypt(encrypted_data)
            self.passwords = json.loads(decrypted_data.decode())
            return True
        except FileNotFoundError:
            # No passwords yet, that's okay
            self.passwords = {}
            return True
        except Exception as e:
            print(f"Error loading passwords: {e}")
            return False

def main():
    pm = PasswordManager()
    
    print("Simple Password Manager")
    print("======================")
    
    # Check if password manager is initialized
    try:
        with open("salt.bin", "rb"):
            initialized = True
    except FileNotFoundError:
        initialized = False
    
    if not initialized:
        print("First time setup - create a master password")
        master_password = getpass.getpass("Create master password: ")
        confirm_password = getpass.getpass("Confirm master password: ")
        
        if master_password != confirm_password:
            print("Error: Passwords don't match")
            return
        
        pm.initialize(master_password)
    else:
        master_password = getpass.getpass("Enter master password: ")
        if not pm.load_key(master_password):
            return
        
        if not pm.load_passwords():
            print("Error: Incorrect master password or corrupted data")
            return
    
    while True:
        print("\nOptions:")
        print("1. Add password")
        print("2. Get password")
        print("3. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == "1":
            service = input("Service name: ")
            username = input("Username: ")
            password = getpass.getpass("Password: ")
            pm.add_password(service, username, password)
        elif choice == "2":
            service = input("Service name: ")
            accounts = pm.get_password(service)
            if accounts:
                for idx, account in enumerate(accounts, 1):
                    print(f"{idx}. Username: {account['username']}")
                    print(f"   Password: {account['password']}")
            else:
                print(f"No accounts found for {service}")
        elif choice == "3":
            break
        else:
            print("Invalid option, please try again")

if __name__ == "__main__":
    main()
