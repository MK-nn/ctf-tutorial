from Crypto.Util.number import isPrime, bytes_to_long
# from secret import flag
import secrets

flag = b'ctf4b{y0u_4r3_4_g00d_c00k1ng_ch3f!}'

# meat = bytes_to_long(secrets.token_bytes(256))
meat = 15805708222816330524745094271130487046751308330362920220166317995445642478569851346673057671209353584484618443794212010617496843751747971904826920548444032786150201291426834419283123798196698241746938627587891659709196278630161164742775627906890894516435855694728716296710262148678544779461591557638263373259034657348648515186185918855676231521284974945954575647385654858461346905296350672796692410884948669498679784214598489019547210975887565837073435159756411863201992614997275535973003693995518560523699037310217690087924209933259306626138879045797591502931836862086592221196485442644818887760450902227606127625889
print(meat)
assert meat.bit_length() <= 2048
# salt = bytes_to_long(secrets.token_bytes(8))
salt = 3224510818096649001
pepper = 3

def bake(meat: int, g: int, p: int):
    # baked = (pow((meat ^ salt) * g**pepper, meat + g*pepper, p) + g * (meat ^ salt)**pepper) % p
    baked = pow((meat ^ salt) * g**3, meat + g*3, p) + (g * (meat ^ salt)**3 % p)
    return baked

print("Let's cook together!")
print("Give me a prime to cook.")
p = int(input("p = "))
if not (128 < p.bit_length() <= 2048):
    print("p should be 2^128 <= p < 2^2048.")
    exit()
if not isPrime(p):
    print("p should be prime!")
    exit()
print("This is meat:", pow(meat, 3, p))
for _ in range(16):
    g = int(input("g = "))
    g %= p
    if not (128 < g.bit_length()):
        print("g should be 2^128 <= g.")
        continue
    print("Here you are. Enjoy!", bake(meat, g, p))
print("You must be full.")
challenge = int(input("Thank you. By the way, where do you think this meat comes from?"))
if meat == challenge:
    print("Nice!", flag)
