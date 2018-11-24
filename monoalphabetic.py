import random

def de_cipher(ip_text, op_text, mapping):
    del op_text[:]
    for i in ip_text:
        op_text.append(mapping[i])
    return op_text

letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
shuffletters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
random.shuffle(shuffletters)
key = dict(zip(letters, shuffletters))
ciphertext = deciphertext = []
inv_key = {v:k for k,v in key.items()}


print("The maps:\n")
for letter, key1 in key.items():
    print(letter, " : ", key1)

plaintext = list(input("\n\nEnter string:  ").upper())

print("Ciphertext:  ", ''.join(de_cipher(''.join(plaintext), ciphertext, key)))
print("Deciphertext:  ", ''.join(de_cipher(''.join(ciphertext), deciphertext, inv_key)))