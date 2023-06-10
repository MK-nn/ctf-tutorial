from Crypto.Util.number import *
import sys

args = sys.argv

key = 364765105385226228888267246885507128079813677318333502635464281930855331056070734926401965510936356014326979260977790597194503012948
cipher = 92499232109251162138344223189844914420326826743556872876639400853892198641955596900058352490329330224967987380962193017044830636379

length = int(args[1])

# ROL の逆演算を行う
def ROR(bits, N):
    for _ in range(N):
        bits = ((bits >> 1) & (2**length - 1)
                ) | (((bits >> 1 << 1) ^ bits) << (length - 1))
    return bits

for i in range(32):
  cipher ^= key
  key = ROR(key, pow(cipher, 3, length))
print('flag =', long_to_bytes(cipher ^ key))
