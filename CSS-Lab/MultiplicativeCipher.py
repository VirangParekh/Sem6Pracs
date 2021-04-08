referenceList = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
                 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def encryption(pt, key):
    result = ''
    for x in pt:
        index = referenceList.index(x)
        result = result + referenceList[(index*key) % 36]
    print('Cipher text = '+result)


def decrypt(ct, key):
    result = ''
    for x in ct:
        index = referenceList.index(x)
        result = result + referenceList[(index*key) % 36]
    print('Plain text = '+result)

# To find multiplicative inverse of key


def inverse(a):
    a = a % 36
    for x in range(1, 36):
        if (a * x) % 36 == 1:
            return x
    return 1


def bruteForceAttack(ct):
    for i in range(1, 37):
        k = inverse(i)
        if k == 1:
            print('Multiplicative inverse for '+str(i)+' does not exist.')
        else:
            result = ''
            for x in ct:
                index = referenceList.index(x)
                result = result + referenceList[(index*k) % 36]
            print('Possible combination #'+str(i)+' : '+result)


print('VIRANG PAREKH B4 60004180121')
while True:
    Choice = int(input('\n*****************\n1. Encryption of Plain text\n2. Decryption of Plain text\n3. Brute Force attack on ct to reveal secret\n4. Exit\nEnter your choice : '))
    if Choice == 1:
        plain = input('Enter the plain text : ')
        key = int(input('Enter the key : '))
        encryption(plain, key)
    elif Choice == 2:
        cipher = input('Enter the cipher text : ')
        key = inverse(int(input('Enter the key : ')))
        decrypt(cipher, key)
    elif Choice == 3:
        cipher = input('Enter the cipher text : ')
        bruteForceAttack(cipher)
    elif Choice == 4:
        break
    else:
        print('Thank You.')
