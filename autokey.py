""" Doesn't work as intended. Will fix. """
# def de_cipher(ip_text, op_text, cl):
#     j = 0
#     for i in ''.join(ip_text):
#         if cl == 'e':
#             op_text.append( alpha[ (alpha.index(i) + alpha.index(keylist[j]))%26 ] )
#         else:
#             op_text.append( alpha[ (alpha.index(i) - alpha.index(keylist[j]))%26 ] )
#         j += 1
#     return op_text

# alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
# ciphertext = deciphertext = keylist = []
# plaintext = list(input("Enter string to be ciphered.  ").upper())
# key = list(input("Enter key.  ").upper())

# for i in range(0, len(key)):
#     keylist.append(key[i])
# for j in range(0, (len(plaintext)-len(key))):
#     keylist.append(plaintext[j])


# print("Ciphertext:  ", ''.join(de_cipher(plaintext, ciphertext, 'e')))
# print("Deciphertext:  ", ''.join(de_cipher(ciphertext, deciphertext, 'd')))