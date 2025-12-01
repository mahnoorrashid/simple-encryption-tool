# 🔐 Simple Encryption Tool (Python)

A simple command-line tool to **encrypt and decrypt text or files** using a password.  
Uses the `cryptography` library (Fernet) for symmetric encryption.

---

## ✨ Features

- Encrypt & decrypt plain text with a password
- Encrypt & decrypt files (e.g. `.txt`, `.log`, etc.)
- Password-based key derivation (SHA-256 → Fernet key)
- Clear error message if the wrong password is used

---

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Install dependencies:

   ```bash
   pip install cryptography

3.	Run the tool:
   python3 encryption_tool.py

4.	Choose one of the menu options:
	•	1 – Encrypt text
	•	2 – Decrypt text
	•	3 – Encrypt file
	•	4 – Decrypt file

📘 Example (Text Encryption)
🔐 Simple Encryption Tool
1) Encrypt text
2) Decrypt text
3) Encrypt file
4) Decrypt file
Choose an option (1-4): 1
Enter password (keep this safe!): mySecretPass
Enter text to encrypt: hello mongo db

Encrypted text (copy & store safely):
gAAAAABnn...

📝 Future Improvements
	•	Add a GUI or web interface
	•	Add support for multiple algorithms
	•	Store keys securely in a key vault
	•	Add unit tests

⸻

👩🏽‍💻 Author

Mahnoor Rashid
