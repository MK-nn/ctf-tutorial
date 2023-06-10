from Crypto.Util.number import *
from random import getrandbits

flag = b'ctf4b{}'

def ROL(bits, N):
    for _ in range(N):
        print('bin bits =     ', bin(bits))
        bits = ((bits << 1) & (2**length - 1)) | (bits >> (length - 1))
    return bits

# ROL の逆演算を行う
def deROL(bits, N):
    for _ in range(N):
        bits = ((bits >> 1) & (2**length - 1)) | (bits << (length - 1))
    return bits

print("flag =", flag)
print('do bytes to long')
flag = bytes_to_long(flag)
print("flag =", flag)
length = flag.bit_length()
print('flag length =', length)

key = getrandbits(length)
print("key =", key)
print('key length =', key.bit_length())
print('bin key    =', bin(key))
print('bin flag   =', bin(flag))
cipher = flag ^ key
print('bin cipher =', bin(cipher))
print("cipher =", cipher)

print('aaaa key =', key)
for i in range(32):
    print("=========================")
    print('for i =', i)
    print('do ROL')
    print('key =', key)
    print('cipher = ', cipher)
    print('bin key =', bin(key))
    print('pow =', pow(cipher, 3, length))
    key = ROL(key, pow(cipher, 3, length))
    print('key =', bin(key))
    print('cipher =', bin(cipher))
    cipher = cipher ^ key
    print('cipher =', bin(cipher))
print('ssss key =', key)

print("**************************")
print('bin key    =', bin(key))
print('bin cipher =', bin(cipher))
print('bin flag   =', bin(key ^ cipher))
print('length =', key.bit_length())

print("key =", key)
print("cipher =", cipher)