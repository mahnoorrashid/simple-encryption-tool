#!/usr/bin/env python3
"""
Simple Text & File Encryption Tool
Author: Mahnoor Rashid
"""

import base64
import hashlib
from pathlib import Path

from cryptography.fernet import Fernet


def derive_key_from_password(password: str) -> bytes:
    """
    Derive a 32-byte key from a password using SHA-256,
    then make it URL-safe for Fernet.
    """
    digest = hashlib.sha256(password.encode("utf-8")).digest()
    return base64.urlsafe_b64encode(digest)


def get_fernet(password: str) -> Fernet:
    key = derive_key_from_password(password)
    return Fernet(key)


def encrypt_text(plaintext: str, password: str) -> str:
    f = get_fernet(password)
    token = f.encrypt(plaintext.encode("utf-8"))
    return token.decode("utf-8")


def decrypt_text(token: str, password: str) -> str:
    f = get_fernet(password)
    try:
        plaintext = f.decrypt(token.encode("utf-8"))
        return plaintext.decode("utf-8")
    except Exception:
        raise ValueError("Decryption failed. Wrong password or corrupted data.")


def encrypt_file(input_path: Path, output_path: Path, password: str) -> None:
    f = get_fernet(password)
    data = input_path.read_bytes()
    token = f.encrypt(data)
    output_path.write_bytes(token)


def decrypt_file(input_path: Path, output_path: Path, password: str) -> None:
    f = get_fernet(password)
    data = input_path.read_bytes()
    try:
        plaintext = f.decrypt(data)
    except Exception:
        raise ValueError("Decryption failed. Wrong password or corrupted file.")
    output_path.write_bytes(plaintext)


def menu() -> None:
    print("🔐 Simple Encryption Tool")
    print("1) Encrypt text")
    print("2) Decrypt text")
    print("3) Encrypt file")
    print("4) Decrypt file")
    choice = input("Choose an option (1-4): ").strip()

    if choice not in {"1", "2", "3", "4"}:
        print("Invalid choice.")
        return

    password = input("Enter password (keep this safe!): ").strip()

    if choice == "1":
        plaintext = input("Enter text to encrypt: ")
        token = encrypt_text(plaintext, password)
        print("\nEncrypted text (copy & store safely):")
        print(token)

    elif choice == "2":
        token = input("Enter text to decrypt: ")
        try:
            plaintext = decrypt_text(token, password)
            print("\nDecrypted text:")
            print(plaintext)
        except ValueError as e:
            print(e)

    elif choice == "3":
        in_path = Path(input("Enter path to file to encrypt: ").strip())
        if not in_path.exists():
            print("File not found.")
            return
        out_path = Path(input("Enter output path for encrypted file: ").strip())
        encrypt_file(in_path, out_path, password)
        print(f"\nEncrypted file written to: {out_path}")

    elif choice == "4":
        in_path = Path(input("Enter path to encrypted file: ").strip())
        if not in_path.exists():
            print("File not found.")
            return
        out_path = Path(input("Enter output path for decrypted file: ").strip())
        try:
            decrypt_file(in_path, out_path, password)
            print(f"\nDecrypted file written to: {out_path}")
        except ValueError as e:
            print(e)


if __name__ == "__main__":
    menu()
