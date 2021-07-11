from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA512, SHA384, SHA256, SHA, MD5
from Crypto import Random
from base64 import b64encode, b64decode
import binascii
hash = "SHA-256"

def newkeys(keysize):
   random_generator = Random.new().read
   key = RSA.generate(keysize, random_generator)
   private, public = key, key.publickey()
   return public, private

def importKey(externKey):
   return RSA.importKey(externKey)

def getpublickey(priv_key):
   return priv_key.publickey()

def encrypt(message, pub_key):
   cipher = PKCS1_OAEP.new(pub_key)
   return cipher.encrypt(message)

def decrypt(ciphertext, priv_key):
   cipher = PKCS1_OAEP.new(priv_key)
   return cipher.decrypt(ciphertext)

public, private = newkeys(1024)
print(public)
print(private)
f = open('public.pem', 'wb')
f.write(public.exportKey('PEM'))
f.close()
f = open('private.pem', 'wb')
f.write(private.exportKey('PEM'))
f.close()

message = "Hello"
print(message.encode())
c = encrypt(message.encode(), public)
c = b64encode(c)
print(c)

# Embed
bits = list(map(int, ''.join([bin(c[i]).lstrip('0b').rjust(8,'0') for i in range(0, len(c))])))

# Decode
string = "".join(chr(int("".join(map(str,bits[i:i+8])),2)) for i in range(0,len(bits),8))
print(string)
print(string.encode())
dc = decrypt(b64decode(string.encode()), private)
print(dc.decode())