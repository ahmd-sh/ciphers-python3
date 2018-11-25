alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
plaintext = list(input("Enter string to be ciphered.  ").upper())
ciphertext = deciphertext = []
key = list(input("Enter word.  ").upper())

"""#encryption
for itr in plaintext:
    if ord(itr) in range(65,91):
        if jtr == len(key):
            jtr =0
        print(itr, " : ", key[jtr])
        summ = (alpha.index(itr) + alpha.index(key[jtr]))%26
        ciphertext.append(alpha[summ])
        jtr += 1
        
print("Encrypted text: ", ''.join(ciphertext))
jtr = 0

#decryption
for itr in (''.join(ciphertext)):
    if ord(itr) in range(65,91):
        if jtr == len(key):
            jtr =0
        summ = (alpha.index(itr) - alpha.index(key[jtr]))%26
        deciphertext.append(alpha[summ])
        jtr += 1
                
print("Decrypted text: ", ''.join(deciphertext))"""

def de_cipher(ip_text, op_text, cl):
    j = summ = 0
    for i in ip_text:
        if j == len(key):
            j = 0
        print(i, " : ", key[j])
        if cl == 'e':    
            summ = ( alpha.index(i) + alpha.index(key[j]) ) % 26
        else:
            summ = ( alpha.index(i) - alpha.index(key[j]) ) % 26
        op_text.append(alpha[summ])
        j += 1
    return ''.join(op_text)

print( "ENC:  ", de_cipher(plaintext, ciphertext, 'e'))
print("DEC:  ", de_cipher(''.join(ciphertext), deciphertext, 'd'))