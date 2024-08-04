from sympy import isprime, mod_inverse
import rsa

class LCG:
    m = 672257317069504227456345634563456638468237648326562347865873434523453435234  
    c = 7382843889490547368345634563456345664563478465784365896324785642534234435234 
    n = 9223372036854775783645634563456345656345634564349857892346587234723345234532523453 

    def __init__(self, seed):
        self.state = seed
        self.time=5  

    def next(self):
        self.state = (self.state * self.m + self.c) % self.n
        if(self.time!=0):
            print(self.state)
            self.time-=1
        return self.state

    def prime(self):
        p = self.next()
        while not isprime(p) or p.bit_length() < 256:
            p = self.next()
        q = self.next()
        while not isprime(q) or q.bit_length() < 256:
            q = self.next()
        return [p, q]


lcg = LCG(123456789)
[p, q] = lcg.prime()

n = p * q
e = 65537
phi = (p - 1) * (q - 1)
d = mod_inverse(e, phi)

public_key = rsa.PublicKey(n, e)
private_key = rsa.PrivateKey(n, e, d, p, q)

message = b'ctf{i_th0ught_LCG_was_s3cur3}'
cipher = pow(int.from_bytes(message, 'big'), e , n)
print(f"n:{n}")
print("Encrypted Flag:", cipher)
