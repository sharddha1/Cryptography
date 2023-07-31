import hashlib

def sha256_hash(file_path):
    sha256_hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while True:
            data = file.read(65536)
            if not data:
                break
            sha256_hasher.update(data)
    return sha256_hasher.digest()

def rsa_verify(file_path, N, e, signature_hex):
    # Convert signature to integer
    signature = int(signature_hex, 16)

    # Step 1: Get SHA-256 hash of the file
    file_hash = sha256_hash(file_path)

    # Step 2: Calculate the hash integer
    hash_int = int.from_bytes(file_hash, byteorder='big')

    # Step 3: Verify the signature using RSA
    decrypted_hash = pow(signature, e, N)

    return hash_int == decrypted_hash

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 5:
        print("Usage: python verifier.py <filename> <N> <e> <signature_hex>")
        sys.exit(1)

    filename = sys.argv[1]
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    N = int(sys.argv[2])
    e = int(sys.argv[3])
    signature_hex = sys.argv[4]

    result = rsa_verify(filename, N, e, signature_hex)
    if result:
        print("Signature is valid. Accept.")
    else:
        print("Signature is not valid. Reject.")
