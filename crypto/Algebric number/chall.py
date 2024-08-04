import gmpy2
from fractions import Fraction
import random
from flag import flag


def generate_prime(bits=512):
    while True:
        num = gmpy2.mpz(random.getrandbits(bits))
        if gmpy2.is_prime(num):
            return num


p = generate_prime(512)
q = generate_prime(512) 
b = generate_prime(256)
a = q+p+1-b
s = (p+1-a)
n=p*q
assert gmpy2.is_prime(p) * gmpy2.is_prime(q) > 0

assert  1 + Fraction( q , p + 1) == Fraction(a + b, s + a)
print( a, b )

c = pow(int.from_bytes(flag.encode(), 'big'), 65537 , n)

print('n =', n)
print('c =', c)
