import json
from base64 import b64encode, b64decode
from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import quantumrandom, sys

plaintext = "Do you really listen when you are talking with someone? I have a friend who listens in an unforgiving way. She actually takes every word you say as being something important and when you have a friend that listens like that, words take on a whole new meaning."

encoded_text = plaintext.encode()
# key = get_random_bytes(32)
# print(key)
key = quantumrandom.binary()[:32]
print(type(key))
print(int.from_bytes(key, byteorder=sys.byteorder))
cipher = ChaCha20.new(key=key)
ciphertext = cipher.encrypt(encoded_text)
nonce = b64encode(cipher.nonce).decode('utf-8')
ct = b64encode(ciphertext).decode('utf-8')
result = json.dumps({'nonce':nonce, 'ciphertext':ct})
print(result)

try:
     nonce = b64decode(nonce)
     ciphertext = b64decode(ct)
     cipher = ChaCha20.new(key=key, nonce=nonce)
     plaintext = cipher.decrypt(ciphertext)
     print("The message was ", plaintext.decode())
except ValueError:
     print("Incorrect decryption")