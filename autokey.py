alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

plaintext = list(input("Enter string to be ciphered. ").upper())
ciphertext = []
decryptext = []
keylist = []
sum = 0
key = list(input("Enter key. ").upper())

for i in range(0, len(key)):
    keylist.append(key[i])
for j in range(0, (len(plaintext)-len(key))):
    keylist.append(plaintext[j])

#encryption
j = 0
for i in plaintext:
    print(i, " : ", keylist[j])
    sum = (alpha.index(i) + alpha.index(keylist[j]))%26
    ciphertext.append(alpha[sum])
    j += 1     
print("Encrypted text: ", ''.join(ciphertext))

#decryption
j = 0
for i in (''.join(ciphertext)):
    sum = (alpha.index(i) - alpha.index(keylist[j]))%26
    decryptext.append(alpha[sum])
    j += 1    
print("Decrypted text: ", ''.join(decryptext).lower())