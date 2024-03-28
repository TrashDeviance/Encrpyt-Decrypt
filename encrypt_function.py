from cryptography.fernet import Fernet, InvalidToken
import os
import hashlib
from dotenv import load_dotenv

load_dotenv()

# storing the encrption key from an env variable
env_var = os.environ.get('ENCRYPTION_KEY')
fernet_usable = Fernet(env_var)


def open_read_file(file: str, mode_type: str) -> str:
    '''Reads from a file for the encryption and decryption process. User must specify a mode, r, rb, r+ etc. '''
    try:
        with open(file, mode=mode_type) as readable_file:
            read_file = readable_file.read()
            readable_file.close()
            return read_file
    except ValueError as error:
        print(f"Error: {error}")


def open_write_file(file: str, mode_type: str, write_data: str) -> str:
    '''Writes to a file for the encryption and decryption process. User must specify a mode, w, wb, w+ etc. '''
    try:
        with open(file, mode=mode_type) as writable_file:
            writable_file.write(write_data)
            writable_file.close()
            message = f"File \"{file}\", has been written to!"
            return message
    except ValueError as error:
        print(f"Error: {error}")


def string_to_byte_encoding(value: str):
    '''Converts a string to a byte with utf-8 encoding.'''
    convert = bytes(str(value), encoding='utf-8')
    return convert


def generate_key():
    '''Generates a Fernet encryption key and stores it within an env file.'''
    environent_file = '.env'
    if os.path.exists(environent_file):
        return
    else:
        key = Fernet.generate_key()
        with open(environent_file, mode='wb') as file:
            file.write("ENCRYPTION_KEY=".encode(encoding='utf-8') + key)


def generate_hash_digest(input_file: str):
    '''Generates a hash digest using the cryptographic SHA256 algorithm.'''
    hash_plaintext = hashlib.sha256(string_to_byte_encoding(input_file))
    hash_digest = hash_plaintext.hexdigest()
    return hash_digest


def encrypt_file(input_file: str):
    '''Encrypts the plaintext of a file and then writes the encryption to the file.'''
    plaintext_file = open_read_file(input_file, 'r')
    token = fernet_usable.encrypt(string_to_byte_encoding(plaintext_file))

    if plaintext_file.startswith('gAAAAA') and plaintext_file.endswith('='):
        print(f"File: \"{input_file}\" has already been encrypted!")
    else:
        open_write_file(input_file, 'wb', token)
        print(f"File: \"{input_file}\" has been encrypted!")


def decrypt_file(input_file: str):
    '''Decrypts the encryptes file and restores the origianl plaintext.'''
    try:
        read_encrypted_file = open_read_file(input_file, 'rb')
        decrypt_data = fernet_usable.decrypt(read_encrypted_file)
        open_write_file(input_file, 'wb', decrypt_data)
        print(f"File: \"{input_file}\" has been decrypted!")
    except InvalidToken as e:
        print(f"File has already been decrypted! {e}")
