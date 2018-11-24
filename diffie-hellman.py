from math import gcd

def is_prime(num):
    if num < 2: 
         return False
    if num % 2 == 0:             
         return num == 2
    k = 3
    while k*k <= num:
         if num % k == 0:
             return False
         k += 2
    return True

a = int(input("Enter A's private key.  "))
b = int(input("Enter B's private key.  "))

while True:
    p = int(input("Enter the prime number.  "))
    if is_prime(p) == True:
        break
    print("Not a prime number.")

while True:
    g = int(input("Enter base.  "))
    if gcd(p,g) == 1:
        break
    print("GCD of prime number and base is not 1.")

pub_key_A = (g**a) % p
pub_key_B = (g**b) % p

#shared key calculation
shared_key_A = (pub_key_B**a) % p
shared_key_B = (pub_key_A**b) % p

if shared_key_A == shared_key_B:
    print("Shared key calculated by A:  ", shared_key_A)
    print("Shared key calculated by B:  ", shared_key_B)