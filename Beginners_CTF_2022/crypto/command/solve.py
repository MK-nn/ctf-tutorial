from Crypto.Util.Padding import pad

fizzbuzz = list(bytes.fromhex(input("Fizzbuzz token: ")))
iv, enc = fizzbuzz[:16], fizzbuzz[16:]

old_cmd = pad(b"fizzbuzz", 16)
cmd = pad(b"getflag", 16)
for i in range(len(old_cmd)):
    iv[i] = iv[i] ^ old_cmd[i] ^ cmd[i]

print(bytes(iv+enc).hex())
