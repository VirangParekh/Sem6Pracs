ref = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
       'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def encrypt(pt, key):
    result = ''
    for x in pt:
        index = ref.index(x)
        result = result + ref[(index+key) % 36]
    print('Cipher text = '+result)


def decrypt(ct, key):
    result = ''
    for x in ct:
        index = ref.index(x)
        result = result + ref[(index-key) % 36]
    print('Plain text = '+result)


def bruteForceAttack(ct):
    for i in range(1, 37):
        result = ''
        for x in ct:
            index = ref.index(x)
            result = result + ref[(index-i) % 36]
        print('Possible combination #'+str(i)+' : '+result)


print('VIRANG PAREKH B4 60004180121')
while True:
    Choice = int(input('\n*****************\n1. Encryption of Plain Text\n2. Decryption of Cipher Text\n3. Brute Force attack on ct to reveal secret\n4. Exit\nEnter your choice : '))
    if Choice == 1:
        plain = input('Enter the plain text : ')
        key = int(input('Enter the key : '))
        encrypt(plain, key)
    elif Choice == 2:
        cipher = input('Enter the cipher text : ')
        key = int(input('Enter the key : '))
        decrypt(cipher, key)
    elif Choice == 3:
        cipher = input('Enter the cipher text : ')
        bruteForceAttack(cipher)
    elif Choice == 4:
        break
    else:
        print('Invalid Choice')
