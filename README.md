# Secure Password Manager & Generator
**Python-Based Cryptographic Tool**

## Project Overview
This repository contains a secure, local-first password management system. Unlike basic text-storage applications, this project utilizes **Symmetric Encryption** to protect sensitive user credentials. It features an integrated password generator that creates high-entropy strings to mitigate the risk of brute-force attacks.

## Key Features
* **Fernet Symmetric Encryption:** Uses the `cryptography` library to ensure that all stored passwords are encrypted with a unique key. Even if the storage file is compromised, the contents remain unreadable without the associated `.key` file.
* **Custom Password Generator:** Dynamically creates passwords using a combination of ASCII letters, special characters, and weighted numeric digits to ensure strong complexity and minimum length requirements.
* **File-Based Persistence:** Manages a local `secretaccess.text` file, utilizing pipe-delimited formatting for efficient data retrieval and parsing.
* **Command Line Interface (CLI):** Features a simple, interactive menu for adding new credentials, viewing decrypted entries, or generating new keys.

## Technical Stack
* **Language:** Python
* **Core Libraries:**
    * `cryptography` (Fernet module): For AES-based encryption/decryption.
    * `random` & `string`: For secure credential generation.
    * `os`: For file handling and directory management.

## How it Works
1.  **Key Generation:** The system generates a `key.key` file (Symmetric Key). **This file must be kept secret and is required for every session.**
2.  **Encryption:** When a user adds a password, the generator creates a string, the Fernet object encrypts the bytes, and the resulting token is stored in the local flat-file.
3.  **Decryption:** When "view" mode is selected, the script reads the encrypted tokens, applies the key, and returns the plain-text passwords to the console for the user.

## Security Considerations
This project was built for educational purposes to demonstrate:
* The difference between plain-text and encrypted storage.
* Proper handling of encryption keys.
* The importance of
