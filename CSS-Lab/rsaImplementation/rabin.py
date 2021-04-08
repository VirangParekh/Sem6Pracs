'''TODO:
        1. p and q of the form 4k+3
        2. n = pq --> public key
        3. (p,q) --> pvt key
        '''


def key_generation(p, q):
    public_key = p*q
    pvt_key = (p, q)
    return public_key, pvt_key


'''TODO:
        C = M^2 mod n
'''


def gcd(e, r):
    while(r != 0):
        e, r = r, e % r
    return e

# Extended Euclidean Algorithm


def eea(a, b):
    if(a % b == 0):
        return(b, 0, 1)
    else:
        gcd, s, t = eea(b, a % b)
        s = s-((a//b) * t)
        return(gcd, t, s)


def encryption(public_key, message):
    enc_text = list()
    n = public_key
    for i in message:
        index = ord(i)
        result = (index ** 2) % n
        enc_text.append(result)
    return enc_text


def decryption(public_key, pvt_key, enc_text):
    p, q = pvt_key
    R = list()
    S = list()
    for i in enc_text:
        R.append((i**((p+1)/4) % p))
        S.append((i**((q+1)/4) % q))
    # form an equation ap + bq = 1
    # a possible solution is 1/2p and 1/2q
    gcd, a, b = eea(p, q)
    m1 = "".join([chr(int((a*p*s)+(b*q*r)) % public_key)
                  for r, s in zip(R, S)])
    m2 = "".join([chr(public_key - ord(i)) for i in m1])
    m3 = "".join([chr(int((a*p*s)-(b*q*r)) % public_key)
                  for r, s in zip(R, S)])
    m4 = "".join([chr(public_key - ord(i)) for i in m3])
    return m1, m2, m3, m4


p = int(input("Enter p of the form 4k + 3: "))
q = int(input("Enter q of the form 4k + 3: "))
message = input("Input the message to be sent")
public_key, pvt_key = key_generation(p, q)
enc_text = encryption(public_key, message)
print("Encrypted text is:", "".join([chr(i) for i in enc_text]))
m1, m2, m3, m4 = decryption(public_key, pvt_key, enc_text)
print("The Decrypted texts are:")
print(m1, "\n", m2, "\n", m3, "\n", m4)
