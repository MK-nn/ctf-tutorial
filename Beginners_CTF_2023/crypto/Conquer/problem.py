from Crypto.Util.number import *
from random import getrandbits
# from flag import flag

flag = b'ctf4b{____}'

def ROL(bits, N):
    for _ in range(N):
        bits = ((bits << 1) & (2**length - 1)) | (bits >> (length - 1))
    return bits


flag = bytes_to_long(flag)
length = flag.bit_length()
print('length =', length)

key = getrandbits(length)
cipher = flag ^ key

for i in range(32):
    key = ROL(key, pow(cipher, 3, length))
    cipher ^= key

print("key =", key)
print("cipher =", cipher)

print('key length =', key.bit_length())
print('cipher length =', cipher.bit_length())
