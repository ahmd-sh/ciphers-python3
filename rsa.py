from math import gcd

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

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


alpha = list("^ABCDEFGHIJKLMNOPQRSTUVWXYZ")

while True:
    second_prime = 4
    first_prime = int(input("Enter first prime number.  "))
    while is_prime(first_prime):
        second_prime = int(input("Enter second prime number.  "))
        if is_prime(second_prime):
            break
        print("Not a prime number.")
    if first_prime == second_prime:
        print("Numbers should not be equal.")
    else:
        if is_prime(second_prime):
            break
    if second_prime == 4:
        print("Not a prime number.")


product_of_primes = first_prime * second_prime
totient = (first_prime-1) * (second_prime-1)

while True:
    e = int(input("Enter 'e'.  "))
    if e in range(2, totient-1) and gcd(e,totient) == 1:
        break
    print("Invalid 'e' value. Enter 'e' value greater than 1 and less than", totient)

d = modinv(e, totient)

message = alpha.index(input("Enter character.  ").upper())

bob_signature = (message**d) % product_of_primes
print("Bob's signature:", bob_signature)

alice_signature = (bob_signature**e) % product_of_primes
print("Alice's signature:", alice_signature, "   which is:", alpha[alice_signature])

#verification
if alice_signature == message:
    print("Valid Signature.")
else:
    print("Invalid signature.")