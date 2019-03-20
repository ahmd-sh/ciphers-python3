import re
# CAESAR CIPHER

# function to cipher plaintext and decipher ciphered text
"""
def de_cipher(ip_text, op_text, cl):
    for i in ip_text:

        # cl short for type, e is encrypt, other alphabets are decrypt
        if cl == 'e':
            op_text.append( alpha[(alpha.index(i) + key)%26] )
        else:
            op_text.append( alpha[(alpha.index(i) - key)%26] )
    return op_text



alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
plaintext = input("Enter the plaintext.  ").lower()
ciphertext = deciphertext = []


# do while emulation to enforce appropriate key input
while True:
    key = int(input("Enter a key value between 1 and 25 (inclusive).  "))
    if (key == 0 or key == 26):
        # shifting alphabets by 0 or 26 does not beneficially affect plaintext
        print("Cipher text for this key will be same as plaintext. Enter key again.")
    else:
        break


print("Ciphertext:  ", ''.join(de_cipher(plaintext, ciphertext, 'e')))
print("Deciphertext:  ", ''.join(de_cipher(ciphertext, deciphertext, 'd')))
"""


alpha = list("abcdefghijklmnopqrstuvwxyz")

while True:
    plaintext = list(input("Enter the plaintext.  ").lower())
    if not re.match("^[a-z]*$", ''.join(plaintext)):
        print("only a-z allowed!")
        
    key = int(input("Enter key (1-25 inclusive).  "))
    if not re.match("^[1-25]*$", str(key)):
        print("only vals 1-25 are effective! enter again.")
    else:
        break

def caesar(text, key, ty):
    if ty == "e":    
        return [alpha[  (alpha.index(x)+key) % 26  ] for x in text]
    else:
        return [alpha[  (alpha.index(x)-key) % 26  ] for x in text]

ciphertext = caesar(plaintext, key, "e")
print("\nCiphered text: ", ''.join(ciphertext))

deciphertext = caesar(ciphertext, key, "d")
print("Deciphered text: ", ''.join(deciphertext))