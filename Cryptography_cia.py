def clean_text(text):
    text = text.lower()
    result = ""
    for c in text:
        if 'a'<= c<= 'z':
            result += c
    return result


def load_key():
    with open("boyle.txt", "r", encoding="utf-8") as f:
        text1 = f.read()

    with open("kelvin.txt", "r", encoding="utf-8") as f:
        text2 = f.read()

    combined = (text1 + text2).lower()
    combined = clean_text(combined)  

    return combined


def xor_hash(text, mod_size=256):
    h = 0

    for c in text:
        h = (ord(c)^(h << 6)^(h << 16)) - h
        h &= 0xFFFFFFFF  

    return h % mod_size


def encrypt(plaintext, key):
    plaintext = plaintext.lower()
    plaintext = clean_text(plaintext)   

    cipher = []

    for i, char in enumerate(plaintext):
        p = ord(char)-ord('a')
        k = ord(key[i])-ord('a')

        c = (p + k) % 26
        cipher.append(chr(c+ord('a')))

    cipher_text = ''.join(cipher)

    hash_val = xor_hash(cipher_text)

    return cipher_text, hash_val


def decrypt(cipher_text, received_hash, key):
    computed_hash = xor_hash(cipher_text)

    if computed_hash != received_hash:
        print("Hash mismatch")
        return None

    print("Hash checked")

    plaintext = []

    for i, char in enumerate(cipher_text):
        c = ord(char) - ord('a')
        k = ord(key[i]) - ord('a')

        p = (c - k) % 26
        plaintext.append(chr(p + ord('a')))

    return ''.join(plaintext)

key = Cryptography_cia.load_key()

test_words = ["hello","crypto"]
while(1):
    print("1.Enter 'a' if you want to run the example words\n2.Enter 'b' if you want to run the example words\n3.Enter 'c' if you want to exit\n")
    op = input("Enter options: ")
    if(op == 'a'):
        for message in test_words: 
            print("\nOriginal:", message)

            cipher, hash_val = Cryptography_cia.encrypt(message, key)

            print("Encrypted text:", cipher)
            print("\nHash:", hash_val)

            decrypted = Cryptography_cia.decrypt(cipher, hash_val, key)

            if decrypted:
                print("\nDecrypted text:", decrypted)
    if(op == 'b'):
        message = input("Enter message: ")

        print("\nOriginal:", message)

        cipher, hash_val = Cryptography_cia.encrypt(message, key)

        print("Encrypted text:", cipher)
        print("\nHash:", hash_val)

        decrypted = Cryptography_cia.decrypt(cipher, hash_val, key)

        if decrypted:
            print("\nDecrypted text:", decrypted)
    if(op == 'c'):
        exit()

