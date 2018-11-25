alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

plaintext = list(input("Enter string to be ciphered. ").upper())
ciphertext = []
decryptext = []
keylist = []
repeat = "yes"
while repeat == "yes":
    key = list(input("Enter word. ").upper())
    if key == 'a':
        print("Invalid Key. Please enter again")
    else:
        break
sum = 0


for itr in range(0, len(key)):
    keylist.append(key[itr])
for jtr in range(0, (len(plaintext)-len(key))):
    if ord(plaintext[jtr]) in range(65, 91):
        keylist.append(plaintext[jtr])

jtr = 0
#encryption
for itr in plaintext:
    if ord(itr) in range(65,91):
        print(itr, " : ", keylist[jtr])
        sum = (alpha.index(itr) + alpha.index(keylist[jtr]))%26
        ciphertext.append(alpha[sum])
        jtr += 1
        
print("Encrypted text: ", ''.join(ciphertext))
jtr = 0

#decryption
for itr in (''.join(ciphertext)):
    if ord(itr) in range(65,91):
        sum = (alpha.index(itr) - alpha.index(keylist[jtr]))%26
        decryptext.append(alpha[sum])
        jtr += 1
                
print("Decrypted text: ", ''.join(decryptext).lower())