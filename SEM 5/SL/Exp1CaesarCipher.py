# A python program to illustrate Caesar Cipher Technique
def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr(((ord(char) + s - 65) % 26) + 65)

        # Encrypt lowercase characters
        else:
            result += chr(((ord(char) + s - 97) % 26) + 97)

    return result



def decrypt(ciphertext, s):
    decrypt_chars = []

    for char in ciphertext:

        if char.isupper():
            decrypt_chars += chr(((ord(char) - 65 - s) % 26) + 65)
        else:
            decrypt_chars += chr(((ord(char) - 97 - s) % 26) + 97)
    return "".join(decrypt_chars)


# check the above function
text = input("Enter the plaintext ")
s = int(input("Enter the shift key "))
print("Text : " + text)
print("Shift : " + str(s))
print("Cipher: " + encrypt(text, s))


ciphertext1 = input("Enter the cipher text ")
s = int(input("enter the key for the shift "))
print("Cipher Text : " + ciphertext1)
print("Shift " + str(s))
print("decrypt text " + decrypt(ciphertext1, s))
