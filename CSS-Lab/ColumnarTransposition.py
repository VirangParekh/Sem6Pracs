import math
import re


def encryption(key, pt):
    pt = re.sub(' ', '', pt)
    # print(pt)
    mat = ["" for i in range(int(math.ceil(len(pt)/len(key))))]
    c = 0
    for i in range(len(mat)):
        mat[i] = pt[c:c+len(key)]
        c += len(key)
    mat[-1] += "X"*(len(key) - len(mat[-1]))
    print(mat)
    key_d = [(x, i) for i, x in enumerate(key)]
    key_d = sorted(key_d)
    # print(key_d)
    ct = ""
    enc_mat = ["X"*len(key) for i in range(int(math.ceil(len(pt)/len(key))))]
    j = 0
    for i in key_d:
        for k in range(len(mat)):
            enc_mat[k] = enc_mat[k][:j] + mat[k][i[1]] + enc_mat[k][j+1:]
            ct += mat[k][i[1]]
        j += 1
    print("Encryption Matrix ")
    for i in enc_mat:
        for j in i:
            print(j, end=" ")
        print()
    return ct


def decryption(key, ct):
    ct = re.sub(' ', '', ct)
    # print(ct)
    mat = ["X"*len(key) for i in range(int(math.ceil(len(ct)/len(key))))]
    key_d = [(x, i) for i, x in enumerate(key)]
    key_d = sorted(key_d)
    i = 0
    j = 0
    while i < len(ct):
        col = key_d[j][1]
        for row in range(len(mat)):
            mat[row] = mat[row][:col] + ct[i] + mat[row][col+1:]
            i += 1
        j += 1
    pt = ""
    print('Decrypted Matrix is ')
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end=" ")
            pt += mat[i][j]
        print()
    return pt


print("B4 60004180121 Virang Parekh")
pt = input("Enter Plain Text ")
key = input("Enter Key ")
print("Encryped Text: ", encryption(key, pt))
ct = input("Enter Text to be Decrypted ")
key = input("Enter key ")
print("Decrypted Text: ", decryption(key, ct))
