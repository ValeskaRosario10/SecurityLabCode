# Function to compute the greatest common divisor (GCD) using the Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Function to compute the modular inverse of 'a' modulo 'm' using the Extended Euclidean Algorithm
def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1  # Initialize variables for the Extended Euclidean Algorithm
    if m == 1:
        return 0  # Modular inverse does not exist if the modulus is 1
    while a > 1:
        q = a // m  # Compute the quotient of 'a' divided by 'm'
        m, a = a % m, m  # Update 'a' and 'm' to continue the algorithm
        x0, x1 = x1 - q * x0, x0  # Update coefficients for the modular inverse
    if x1 < 0:
        x1 += m0  # Adjust 'x1' to be positive by adding 'm0'
    return x1

# Function to generate RSA public and private keys based on input primes and public exponent
def generate_keys(p, q, e):
    n = p * q  # Compute the modulus 'n' used for both public and private keys
    phi = (p - 1) * (q - 1)  # Compute Euler's totient function for modulus 'n'
    d = mod_inverse(e, phi)  # Compute the modular inverse of 'e' modulo 'phi' to get the private key
    return (e, n), (d, n)  # Return the public key and private key tuples

# Function to sign a message using the RSA private key
def sign_message(message, private_key):
    d, n = private_key  # Extract the private key components
    return pow(message, d, n)  # Apply RSA signing formula: message^d % n

# Function to verify a digital signature using the RSA public key
def verify_signature(message, signature, public_key):
    e, n = public_key  # Extract the public key components
    return pow(signature, e, n) == message  # Verify the signature by comparing message with signature^e % n

# Main function to handle user input and interaction
def main():
    # Request user input for RSA key generation parameters
    print("Enter the following details for RSA key generation:")
    p = int(input("Prime number p: "))  # Input for the first prime number
    q = int(input("Prime number q: "))  # Input for the second prime number
    e = int(input("Public key e: "))  # Input for the public exponent
    
    # Generate RSA keys based on user inputs
    public_key, private_key = generate_keys(p, q, e)
    print(f"\nGenerated Keys:")
    print(f"Public Key: {public_key}")  # Display the public key (e, n)
    print(f"Private Key: {private_key}")  # Display the private key (d, n)
    # Request user input for signing a message
    message = int(input("\nEnter the message to sign: "))  # Input for the message to be signed
    signature = sign_message(message, private_key)  # Generate the digital signature
    print(f"Digital Signature: {signature}")  # Display the generated digital signature
    # Request user input for signature verification
    print("\nEnter the signature and message to verify:")
    input_signature = int(input("Signature: "))  # Input for the signature to be verified
    input_message = int(input("Message: "))  # Input for the original message
    is_valid = verify_signature(input_message, input_signature, public_key) 
 # Verify the signature
    if is_valid:
        print("The message is authentic")  # If valid, confirm the authenticity of the message
    else:
        print("Message is altered. Discard.")  # If invalid, indicate that the message may have been tampered with
if __name__ == "__main__":
    main()  # Execute the main function to start the program

