import base64
from sys import argv

helpstr = f"usage: {argv[0]} [-h] PLAINTEXT CIPHER" 

if len(argv) != 3:
    print(f"Error: wrong arguments\n{helpstr}")
    exit(-1)
if "-h" in argv:
    print(helpstr)
    exit(0)

# XOR Plaintext wirth Cipher and convert result into a string
key = ''.join([ chr(ord(i) ^ ord(j)) for i, j in zip(argv[1], argv[2]) ])

# Encode cipher to base64
cph_base64 = base64.b64encode(argv[2].encode()).decode()
print(f"Key: {key}\nCipher Base64 encoded: {cph_base64}")