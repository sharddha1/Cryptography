import os
import hashlib
import random
import sympy

def sha256_hash(file_path):
    sha256_hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)
            if not data:
                break
            sha256_hasher.update(data)
    return sha256_hasher.digest()

def generate_semiprime(bits=2048):
    p = sympy.randprime(2**(bits//2 - 1), 2**(bits//2))
    q = sympy.randprime(2**(bits//2 - 1), 2**(bits//2))
    return p * q

def modular_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def rsa_sign(file_path):
    # Step 1: Get SHA-256 hash of the file
    file_hash = sha256_hash(file_path)

    # Step 2: Generate random semiprime N
    N = generate_semiprime()

    # Step 3: Use e = 65537 for RSA digital signature
    e = 65537

    # Step 4: Calculate the digital signature using RSA
    hash_int = int.from_bytes(file_hash, byteorder='big')
    signature = pow(hash_int, e, N)

    return (N, e), hex(signature)

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python sign.py <filename>")
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    keys, signature = rsa_sign(filename)
    print(f"Public Key (N, e): {keys}")
    print(f"Digital Signature (hex): {signature}")
