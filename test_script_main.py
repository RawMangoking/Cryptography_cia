import Cryptography_cia

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