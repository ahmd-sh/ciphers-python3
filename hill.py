import numpy as np

def inverse_matrix(matrix):
    det = np.round((np.linalg.det(matrix))).astype(int)
    adjoint = (np.linalg.inv(matrix) * det) % 26
    if det < 0:
        det = det%26
    for i in range(1, 100):
        if (det*i) % 26 == 1:
            det_inverse = i
            break
    return((det_inverse * adjoint) % 26)


alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
order  = int(input("Provide order: "))
flag = 1
mat_elements = []
tobencrypt = []
plaintextmat = []
ciphertext = []
ciphertextmat = []
decryptext = []


while flag == 1:
    del mat_elements[:]
    for i in range(1, (order**2)+1):
        mat_elements.append(input("Enter element {}: ".format(i)))
        if i%order == 0 and i != order**2:
            mat_elements.append(";")
        mat_elements.append(" ")
    
    keymat = np.matrix(''.join(mat_elements))
    print(keymat)
    
    try:
        inverse = np.round(inverse_matrix(keymat)).astype(int)
        break
    except np.linalg.LinAlgError:
        print("Inverse doesnt exist. Try Again.")


plaintext = list(input("Enter plaintext. ").upper())
for space in plaintext:
    if space == ' ':
        plaintext.remove(space)


while True:
    if len(plaintext)%order == 0:
        break
    plaintext.append("X")

print("\nSPLITTED PLAINTEXT")
for i in range(0, len(plaintext)-1, order):
    try:
        print(np.transpose(np.column_stack(plaintext[i:i+order])))
        print()
    except IndexError:
        pass


#encryption
for i in range(len(plaintext)):
    plaintext[i] = alpha.index(plaintext[i])

for i in range(0, len(plaintext)-1, order):
    try:
        plaintextmat.append(plaintext[i:i+order])
    except IndexError:
        pass

#encryption actual process
for i in plaintextmat:
    tobencrypt = np.matrix(np.transpose(np.column_stack(i)))

    result = np.mod(np.matmul(keymat, tobencrypt), 26)

    ciphertext2 = np.array(result).flatten().tolist()
    
    for i in range(len(ciphertext2)):
        ciphertext.append(alpha[ciphertext2[i]])

print("CIPHER TEXT:  ", ''.join(ciphertext), "\n\n")


#decryption
for i in range(len(ciphertext)):
    ciphertext[i] = alpha.index(ciphertext[i])

for i in range(0, len(ciphertext)-1, order):
    try:
        ciphertextmat.append(ciphertext[i:i+order])
    except IndexError:
        pass
print("KEY MATRIX INVERSE\n", inverse, "\n")

#decryption actual process
for i in ciphertextmat:
    tobencrypt = np.matrix(np.transpose(np.column_stack(i)))

    result = np.mod(np.matmul(inverse, tobencrypt), 26)

    decryptext2 = np.array(result).flatten().tolist()

    for i in range(len(decryptext2)):
        decryptext.append(alpha[decryptext2[i]])

#removing X's from end
for i in range(len(decryptext)-1, -1, -1):
    if decryptext[i] == 'X':
        del decryptext[i]
    else:
        break

print("DECRYPTED TEXT:  ", ''.join(decryptext))