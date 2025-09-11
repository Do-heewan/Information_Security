# 2-3 코드북 암호

import random

codebook = {
    "attack" : 1234,
    "dawn" : 5678,
    "meet" : 9101,
    "secret" : 1121
}
plain = "attackdawnmeetsecret"
key = random.randint(0, 9999)
print("Key :", key)

cipher = []
for i, v in codebook.items():
    cipher.append(v + key)

print("Cipher :", cipher)

decrypt = []
dec = ''
for c in cipher:
    decrypt.append(c - key)

for d in decrypt:
    for k, v in codebook.items():
        if d == v:
            print(k, end='')