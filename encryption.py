def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            encrypted_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    while True:
        choice = input("Do you want to (e)ncrypt or (d)ecrypt a message? (q to quit): ").lower()
        if choice == 'q':
            break
        elif choice in ['e', 'd']:
            text = input("Enter your message: ")
            shift = int(input("Enter the shift number (1-25): "))
            if choice == 'e':
                print("Encrypted message:", encrypt(text, shift))
            else:
                print("Decrypted message:", decrypt(text, shift))
        else:
            print("Invalid choice. Please enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit.")

if __name__ == '__main__':
    main()
