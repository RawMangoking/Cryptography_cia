# Cryptography_cia



Running Key Cipher + Modified SDBM-Based Hash Function\
Theory:\
Running Key Cipher\

The Running Key Cipher is a cipher that uses a long key derived from book.\

Encryption:\
C = (P + K) mod 26

Decryption:\
P = (C - K) mod 26

Hash Function (Modified SDBM-Based):\
The hash function used in this project is a modified version of the SDBM hash, enhanced using XOR and bit-shifting operations.\
Function:\
h = (ord(c) ^ (h << 6) ^ (h << 16)) - h\
h = h & 0xFFFFFFFF\
hash = h % 256

Explanation\

`ord(c)` → converts character to ASCII\
`(h << 6)` and `(h << 16)` → spread bit influence\
`^` (XOR) → improves randomness and mixing\
`- h` → maintains SDBM-style diffusion\
`& 0xFFFFFFFF` → keeps value within 32-bit\
`% 256` → produces fixed-size output

Instructions to Run\
1. Place files:
   boyle.txt
   kelvin.txt
2. Run:
   test_script_main.py
   
4. Enter the option and message when prompted\

Example 1\
Original:hello\
Key:jappl\
Encrypted text:qeaaz\
Hash:6\
Hash checked

Original:crypto\
Key:japplp\
Encrypted text:lrneed\
Hash:188\
Hash checked


Promts used for the CIA\
1)What is hash function\
2)List of books that  can be used for key\
3)can i use a temperature +pressure +coordinates as hash \
4)how does receiver know where ciphertext starts and ends when hash is appended\
5)Examples of simple hash functions \
6)Is crc is viable hash function
7)Like how to combine hash and cipher text\
8)Things that must be agreed upon earlier 
