alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

plaintext = list(input("Enter string to be ciphered.  ").upper())
ciphertext = []
decryptext = []
key = list(input("Enter word. ").upper())
sum = 0 #sum of index values of letters in encrption and decryption
jtr = 0 #loop iterator

#encryption
for itr in plaintext:
    if ord(itr) in range(65,91):
        if jtr == len(key):
            jtr =0
        print(itr, " : ", key[jtr])
        sum = (alpha.index(itr) + alpha.index(key[jtr]))%26
        ciphertext.append(alpha[sum])
        jtr += 1
        
print("Encrypted text: ", ''.join(ciphertext))
jtr = 0

#decryption
for itr in (''.join(ciphertext)):
    if ord(itr) in range(65,91):
        if jtr == len(key):
            jtr =0
        sum = (alpha.index(itr) - alpha.index(key[jtr]))%26
        decryptext.append(alpha[sum])
        jtr += 1
                
print("Decrypted text: ", ''.join(decryptext).lower())