def find_prime_factors(n):
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return i, n // i
    return 1, n
def compute_private_key(public_key, zhi_n):
    k = 1
    while True:
        d = (1 + k * zhi_n) / public_key
        if d.is_integer():
            return int(d)
        k += 1
def encrypt_message(message, public_key, receiver_n):
    return pow(message, public_key, receiver_n)
def decrypt_message(cipher, private_key, n):
    return pow(cipher, private_key, n)

def main():
    public_key = int(input("Enter public key: "))
    n = int(input("Enter n: "))
    p, q = find_prime_factors(n)
    zhi_n = (p - 1) * (q - 1)
    print(f"p: {p}\nq: {q}\nφ(n): {zhi_n}")
    private_key = compute_private_key(public_key, zhi_n)
    print(f"Public key: ({public_key}, {n})")
    print(f"Private key: ({private_key}, {n})")

    while True:
        choice = int(input("\n1. Encrypt\n2. Decrypt\n3. Exit\nChoose an operation: "))
        print()

        if choice == 1:
            message = int(input("Enter the message: "))
            receiver_public_key = int(input("Enter the recipient's public key: "))
            receiver_n = int(input("Enter the recipient's n: "))
            cipher = encrypt_message(message, receiver_public_key, receiver_n)
            print("Cipher text: ", cipher)

        elif choice == 2:
            cipher = int(input("Enter the cipher text: "))
            message = decrypt_message(cipher, private_key, n)
            print("Decrypted message: ", message)

        elif choice == 3:
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
