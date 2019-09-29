from typing import AnyStr
import hashlib as hlb
import os

def get_csci_salt():
    """Returns the appropriate salt for CSCI E-29"""
    CSCI_SALT = '3f87b3a5b7e48ba408964366a7194789249d4ed33b962a9e5d76c5d6122237bc'
    return bytes.fromhex(str(CSCI_SALT))

    # Hint: use os.environment and bytes.fromhex


def hash_str(some_val, salt=""):
    """Converts strings to hash digest

    See: https://en.wikipedia.org/wiki/Salt_(cryptography)

    :param some_val: thing to hash

    :param salt: Add randomness to the hashing

    """
    return hlb.sha256(str(salt).encode() + str(some_val).encode()).digest()


def get_user_id(username):
    salt = get_csci_salt()
    return hash_str(str(username).lower(), salt=salt).hex()[:8]



# env_salt = os.getenv('CSCI_SALT','value does not exist')
# print(env_salt)
# print(hash_str('hello world',env_salt))
# print(get_user_id('frankie'))