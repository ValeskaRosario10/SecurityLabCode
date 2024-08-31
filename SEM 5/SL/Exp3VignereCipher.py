def vigenere_encrypt(plain_text, key):
    encrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in plain_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.islower():
                encrypted_text += chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('a'))
            else:
                encrypted_text += chr((ord(char) - ord('a' if char.islower() else 'A') + shift) % 26 + ord('A'))
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text

def main():
    plain_text = input("Enter the plain text: ")
    key = input("Enter the encryption key: ")
    encrypted_text = vigenere_encrypt(plain_text, key)
    print("Encrypted text:", encrypted_text)

if __name__ == "__main__":
    main()


#decription
def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ""
    key = key.upper()
    key_index = 0

    for char in encrypted_text:
        if char.isalpha():
            shift = ord(key[key_index % len(key)]) - ord('A')
            if char.islower():
                decrypted_text += chr((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26 + ord('a'))
            else:
                decrypted_text += chr((ord(char) - ord('a' if char.islower() else 'A') - shift) % 26 + ord('A'))
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text

def main():
    encrypted_text = input("Enter the encrypted text: ")
    key = input("Enter the decryption key: ")
    decrypted_text = vigenere_decrypt(encrypted_text, key)
    print("Decrypted text:", decrypted_text)

if __name__ == "__main__":
    main()