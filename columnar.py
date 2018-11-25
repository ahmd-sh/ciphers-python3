import numpy as np

def remove_spaces(lst):
    for space in lst:
        if space == " ":
            lst.remove(space)
    return lst

def order_key(key):
    key_numbered = ["$" for x in key]
    for i in range(len(key)):
        key[i] = alpha.index(key[i]) + 1
    for j in range(len(key)):
        min_index = key.index(min(key))
        key_numbered[min_index] = j+1
        key[min_index] = 999
    del key[:]
    return key_numbered

def insert_row_wise(text, grid, key):
    for j in range(len(key)):
        grid[0][j] = key[j]
    itr = 0
    for i in range(1, len(grid)):
        for j in range(len(key)):
            grid[i][j] = text[itr]
            itr+=1
    return grid

def insert_col_wise(text, grid, key):
    for j in range(len(key)):
        grid[0][j] = key[j]
    itr = 0
    for j in range(1, len(key)+1):
        j_index = grid[0].tolist().index(str(j))
        for i in range(1, len(grid)):
            grid[i][j_index] = text[itr]
            itr+=1
    return grid

def display_text(text, key, grid, cl):
    if cl == 'c':
        for j in range(1, len(key)+1):
            j_index = grid[0].tolist().index(str(j))
            for i in range(1, len(grid)):
                text.append(grid[i][j_index])
            text.append(" ")
    else:
        for i in range(1, len(grid)):
            for j in range(len(key)):
                text.append(grid[i][j])
        if cl == 'd_final':
            for x in range(len(text)-1, len(text)-X_counter-1, -1):
                text.remove(text[x])

    print("\nText:  ", ''.join(text), "\n")
    text = remove_spaces(text)


alpha = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
X_counter = 0
ciphertext1 = []
ciphertext2 = []
decrypt_text1 = []
decrypt_text2 = []

while True:
    key1 = order_key(list(input("Enter key 1.  ").upper()))
    key2 = order_key(list(input("Enter key 2.  ").upper()))
    if len(key1) == len(key2):
        break
    print("ERROR. Enter keys of same length.")

plaintext = remove_spaces(list(input("Enter the plaintext.  ").upper()))
while len(plaintext)%len(key1) != 0:
    plaintext.append('X')
    X_counter += 1


# encryption
# first
cipher_rows1 = int( len(plaintext) / len(key1) ) + 1
cipher_grid1 = np.empty(shape=(cipher_rows1, len(key1)), dtype=str)

cipher_grid1 = insert_row_wise(plaintext, cipher_grid1, key1)
print("\n\nCipher Grid 1:", cipher_grid1, sep='\n')

display_text(ciphertext1, key1, cipher_grid1, cl='c')

# second
cipher_rows2 = int(len(ciphertext1) / len(key2)) + 1
cipher_grid2 = np.empty(shape=(cipher_rows2, len(key2)), dtype=str)

while len(ciphertext1)%len(key1) != 0:
    plaintext.append('X')

cipher_grid2 = insert_row_wise(ciphertext1, cipher_grid2, key2)
print("Cipher Grid 2: ", cipher_grid2, sep='\n')

display_text(ciphertext2, key2, cipher_grid2, cl='c')




# decryption
# first
decrypt_rows2 = int(len(ciphertext2) / len(key2)) + 1
decrypt_grid2 = np.empty(shape=(decrypt_rows2, len(key2)), dtype=str)

decrypt_grid2 = insert_col_wise(ciphertext2, decrypt_grid2, key2)
print("Decryption Grid 2: ", decrypt_grid2, sep='\n')

display_text(decrypt_text2, key2, decrypt_grid2, cl='d')

# second
decrypt_rows1 = int(len(ciphertext1) / len(key1)) + 1
decrypt_grid1 = np.empty(shape=(decrypt_rows1, len(key1)), dtype=str)

decrypt_grid1 = insert_col_wise(ciphertext1, decrypt_grid1, key1)
print("Decryption Grid 1:", decrypt_grid1, sep='\n')

display_text(decrypt_text1, key1, decrypt_grid1, cl='d_final')