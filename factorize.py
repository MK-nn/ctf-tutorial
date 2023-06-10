def main(n):
    factors = []
    primes = [2, 3]
    for i in primes:
        while n % i == 0:
            factors.append(i)
            n //= i
    f = primes[-1]
    while f * f <= n:
        print(f)
        if n % f == 0:
            factors.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        factors.append(n)
    return factors

if __name__ == "__main__":
    n = int(input())
    print(main(n))
