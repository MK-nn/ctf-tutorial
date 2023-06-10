from Crypto.Util.number import *
from random import getrandbits
from os import urandom

seed = 219857298424504813337494024829602082766
cipher = 38366804914662571886103192955255674055487701488717997084670307464411166461113108822142059

class LFSR:
    def __init__(self):
        self.bits = 128
        self.rr = seed
        self.switch = 0
    def init(self):
        self.rr = seed
        self.switch = 0

    def next(self):
        r = self.rr
        if self.switch == 0:
            b = ((r >> 0) & 1) ^ \
                ((r >> 2) & 1) ^ \
                ((r >> 4) & 1) ^ \
                ((r >> 6) & 1) ^ \
                ((r >> 9) & 1)
        if self.switch == 1:
            b = ((r >> 1) & 1) ^ \
                ((r >> 5) & 1) ^ \
                ((r >> 7) & 1) ^ \
                ((r >> 8) & 1)
        r = (r >> 1) + (b << (self.bits - 1))
        self.rr = r
        self.switch = 1 - self.switch
        return r & 1

    def gen_randbits(self, bits):
        key = 0
        for i in range(bits):
            key <<= 1
            key += self.next()
        return key


lfsr = LFSR()

# for _ in range(127):
#     print(lfsr.next(), end="")
# print()
# neko = urandom(ord("🐈")*ord("🐈")*ord("🐈"))
# key = lfsr.gen_randbits(len(neko) * 8)
# cipher = bytes_to_long(neko) ^ key
neko_length = ord("🐈")*ord("🐈")*ord("🐈")
print('neko length=>', neko_length)

# sequence = []
# period = 0
# for i in range(neko_length):
#     print(i / neko_length * 100)
#     sequence.append(lfsr.next())
#     if i > 30:
#         if sequence[:30] == sequence[i-30:]:
#             print('discovered period:')
#             print('i = ', i)
#             period = i-30
#             break

#   📄🐈💨💨💨💨
# ╭─^────────╮
# │  cipher  │
# ╰──────────╯

# key = lfsr.gen_randbits(len(flag) * 8)
# cipher = bytes_to_long(flag) ^ key

# print("seed =", seed)
# print("cipher =", cipher)

candidate = [9, 11, 27, 33, 81, 99, 297, 431, 891, 1087, 1293, 3261, 3879, 4741, 9783, 11637, 11957, 14223, 29349, 34911, 35871, 42669, 88047, 107613, 128007, 322839, 384021, 468497, 968517, 1405491, 4216473, 5024893, 5153467, 12649419, 15074679, 15460401, 37948257, 45224037, 46381203, 55273823, 135672111, 139143609, 165821469, 407016333, 417430827, 497464407, 1492393221, 2165728883, 4477179663, 5462058691,
             6497186649, 16386176073, 19491559947, 23823017713, 49158528219, 58474679841, 60082645601, 71469053139, 147475584657, 175424039523, 180247936803, 214407159417, 442426753971, 540743810409, 643221478251, 1622231431227, 1929664434753, 2354147295821, 4866694293681, 7062441887463, 21187325662389, 25895620254031, 63561976987167, 77686860762093, 190685930961501, 233060582286279, 699181746858837, 2097545240576511]
for c in candidate:
    for d in range(c - 5, c + 5):
        lfsr.init()
        period = d
        print('period=>', period)
        for _ in range(neko_length % period):
            lfsr.next()

        for i in range(30, 60):
            flag_length = i
            key = lfsr.gen_randbits(flag_length * 8)
            flag = long_to_bytes(cipher ^ key)
            if 'ctf' in str(flag):
                print('flag=>', flag)
