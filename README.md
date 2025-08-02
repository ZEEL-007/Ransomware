# 🔐 Ransomware Simulation (Educational Purpose Only)

This project is a simple Python-based simulation of how ransomware works — for **educational and ethical learning only**. It includes two main scripts:

- `encrypt.py` – encrypts files in a given directory using symmetric encryption (Fernet)
- `decrypt.py` – decrypts the previously encrypted files using the same key

> ⚠️ This script is **not meant for malicious use**. It's created for cybersecurity learning, ethical hacking practice, or personal experimentation in a safe environment (like a VM).

---

## 🧠 How It Works

- The encryption script (`encrypt.py`) generates a secret key and encrypts all files inside a target directory.
- The decryption script (`decrypt.py`) uses the stored key to decrypt those files back to normal.

Make sure to **keep the key safe**, or you'll lose access to the files (just like real ransomware).

---

## ⚙️ Requirements

Make sure Python is installed on your system. Then install the `cryptography` package:

```bash
pip install cryptography
```

## 🚀 How to Use?

- 1. Encrypt Files

Run the encrypt script and follow the prompts:

```bash
python encrypt.py
```

It will:

- Generate a key
- Save it as a .key file
- Encrypt all files in the specified folder


