def index_finder(ele):
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j] == ele:
                return(str(i) + str(j))


alpha = list("ABCDEFGHIKLMNOPQRSTUVWXYZ")
ciphertext = []
deciphertext = []

key = list(dict.fromkeys(input("Enter key.\n").upper())) #Takes input and removes duplicates 

for i in key:
    if i in alpha:
        alpha.remove(i)
    else:
        pass

key = key + alpha

key_matrix = [
    key[:5],
    key[5:10],
    key[10:15],
    key[15:20],
    key[20:25]
]
print(key[:5],
    key[5:10],
    key[10:15],
    key[15:20],
    key[20:25], sep="\n")


plaintext = list(input("Enter plaintext.\n").upper())
plaintext2 = []


for i in range(len(plaintext)):
    try:    
        if plaintext[i] == plaintext[i+1]:
            if i%2 == 0:
                plaintext.insert(i+1, "X")
    except IndexError:
        pass

if len(plaintext)%2 != 0:
    plaintext.append("X")


#splitting plaintext in digraphs
for i in range(0, len(plaintext)-1, 2):
    try:
        plaintext2.append(''.join(plaintext[i:i+2]))
    except IndexError:
        pass
print(plaintext2)

#encryption
for i in plaintext2:
    fl = i[0]
    sl = i[1]

    l = int(index_finder(fl)[0])
    m = int(index_finder(fl)[1])

    x = int(index_finder(sl)[0])
    y = int(index_finder(sl)[1])

    #assuming next element of the row, if diagraph has 2 same letters
    if l == x and m == y:
        if m == 4:
            ciphertext.append(key_matrix[l][0] + key_matrix[x][0])

        else:
            ciphertext.append(key_matrix[l][m+1] + key_matrix[x][y+1])


    elif m == y:  
        if l == 4:
            ciphertext.append(key_matrix[0][m] + key_matrix[x+1][y])

        elif x == 4:
            ciphertext.append(key_matrix[l+1][m] + key_matrix[0][y])

        else:
            ciphertext.append(key_matrix[l+1][m] + key_matrix[x+1][y])


    elif l == x:
        if m == 4:
            ciphertext.append(key_matrix[l][0] + key_matrix[x][y+1])

        elif y == 4:
            ciphertext.append(key_matrix[l][m+1] + key_matrix[x][0])

        else:
            ciphertext.append(key_matrix[l][m+1] + key_matrix[x][y+1])

    else:
        ciphertext.append(key_matrix[l][y] + key_matrix[x][m])

print("Ciphertext: ", ' '.join(ciphertext))


#decryption
for i in ciphertext:
    fl = i[0]
    sl = i[1]

    l = int(index_finder(fl)[0])
    m = int(index_finder(fl)[1])

    x = int(index_finder(sl)[0])
    y = int(index_finder(sl)[1])

    #assuming previous element of the row, if diagraph has 2 same letters
    if l == x and m == y:
        if m == 0:
            deciphertext.append(key_matrix[l][4] + key_matrix[x][4])
        else:
            deciphertext.append(key_matrix[l][m-1] + key_matrix[x][y-1])

    elif m == y:
        if l == 0:
            deciphertext.append(key_matrix[4][m] + key_matrix[x-1][y])
        elif x == 0:
            deciphertext.append(key_matrix[l-1][m] + key_matrix[4][y])
        else:
            deciphertext.append(key_matrix[l-1][m] + key_matrix[x-1][y])

    elif l == x:
        if m == 0:
            deciphertext.append(key_matrix[l][4] + key_matrix[x][y-1])
        elif y == 0:
            deciphertext.append(key_matrix[l][m-1] + key_matrix[x][4])
        else:
            deciphertext.append(key_matrix[l][m-1] + key_matrix[x][y-1])

    else:
        deciphertext.append(key_matrix[l][y] + key_matrix[x][m])


deciphertext = list(''.join(deciphertext))
for i in range(len(deciphertext)):
    try:
        if deciphertext[i-1] == deciphertext[i+1]:
            deciphertext.remove(deciphertext[i])
    except IndexError:
        pass


print("Decrypted text: ", ''.join(deciphertext))