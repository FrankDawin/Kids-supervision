from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding


def encrypt_file(input_file, output_file, public_key):
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(output_file, 'wb') as f:
        f.write(ciphertext)

# Generate key pair
private_key, public_key = generate_key_pair()

# Save the public key to a file
save_public_key(public_key)

# File paths
input_file_path = 'plaintext.txt'
encrypted_file_path = 'encrypted_file.enc'

# Encrypt the text file
encrypt_file(input_file_path, encrypted_file_path, public_key)

print(f"File '{input_file_path}' encrypted and saved to '{encrypted_file_path}'.")


def load_private_key(private_key_path):
    with open(private_key_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

def decrypt_file(encrypted_file, decrypted_file, private_key):
    with open(encrypted_file, 'rb') as f:
        ciphertext = f.read()

    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    with open(decrypted_file, 'wb') as f:
        f.write(plaintext)

# File paths
private_key_path = 'private_key.pem'
decrypted_file_path = 'decrypted_file.txt'
encrypted_file_path = 'encrypted_file.enc'

# Load the private key
private_key = load_private_key(private_key_path)

# Decrypt the file
decrypt_file(encrypted_file_path, decrypted_file_path, private_key)

print(f"File '{encrypted_file_path}' decrypted and saved to '{decrypted_file_path}'.")


def generate_key_pair():
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048,
        backend=default_backend()
    )
    public_key = private_key.public_key()
    return private_key, public_key


def save_public_key(public_key, filename="public_key.pem"):
    public_key_bytes = public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    )
    with open(filename, "wb") as f:
        f.write(public_key_bytes)


def save_private_key(private_key, password, filename="private_key.pem"):
    encryption_algorithm = serialization.BestAvailableEncryption(password.encode())
    private_key_bytes = private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=encryption_algorithm
    )
    with open(filename, "wb") as f:
        f.write(private_key_bytes)


# Generate key pair
private_key, public_key = generate_key_pair()

# Save the private key with a password
password = "your_secure_password"
save_private_key(private_key, password)

print(f"Private key saved to 'private_key.pem' with password protection.")


if __name__ == "__main__":
    print(generate_key_pair())
    save_public_key(generate_key_pair()[1])

