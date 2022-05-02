import hashlib
import os
import base64

class Hasher:
    def generate_hash(text, salt):
        hash = base64.b64encode(hashlib.pbkdf2_hmac(
            'sha256', # The hash digest algorithm for HMAC
            text.encode('utf-8'), # Convert the password to bytes
            salt.encode('utf-8'), # Provide the salt
            100000, # It is recommended to use at least 100,000 iterations of SHA-256
            dklen=128 # Get a 128 byte key
        ))
        return hash
