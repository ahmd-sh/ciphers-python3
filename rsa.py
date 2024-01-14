from math import gcd


def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % m


def is_prime(num):
    # Optimzation: early return for small numbers
    if num < 2:
        return False
    if num < 4:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False

    divisor = 5
    while divisor * divisor <= num:
        if num % divisor == 0 or num % (divisor + 2) == 0:
            return False
        divisor += 6

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

    if second_prime == 4:
        print("Not a prime number.")
    else:
        if first_prime == second_prime:
            print("Numbers should not be equal.")
        else:
            if is_prime(second_prime):
                break


product_of_primes = first_prime * second_prime
totient = (first_prime - 1) * (second_prime - 1)

while True:
    public_exponent = int(input("Enter public exponent 'e'.  "))

    # 'e' should be coprime to the totient and within the range [2, totient-1]
    if public_exponent in range(2, totient - 1) and gcd(public_exponent, totient) == 1:
        break
    print(
        "Invalid public exponent value. Enter public exponent value greater than 1 and less than",
        totient,
    )

d = modinv(public_exponent, totient)

while True:
    character_input = input("Enter a single character: ").upper()

    if len(character_input) == 1 and character_input in alpha:
        message = alpha.index(character_input)
        break
    else:
        print(
            "Invalid input. Please enter a single character from the list:",
            "".join(alpha),
        )

bob_signature = (message**d) % product_of_primes
print("Bob's signature:", bob_signature)

alice_signature = (bob_signature**public_exponent) % product_of_primes
print("Alice's signature:", alice_signature, "   which is:", alpha[alice_signature])

# Verification
if alice_signature == message:
    print("Valid Signature.")
else:
    print("Invalid signature.")
