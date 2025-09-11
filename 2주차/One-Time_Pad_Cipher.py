# 2-2 일회성 암호

plain = 'heilhitler'

mapping_dict = {
    "e" : 0b000,
    "h" : 0b001,
    "i" : 0b010,
    "k" : 0b011,
    "l" : 0b100,
    "r" : 0b101,
    "s" : 0b110,
    "t" : 0b111
}
mapping_list = ["e", "h", "i", "k", "l", "r", "s", "t"]

key = [0b111, 0b101, 0b110, 0b101, 0b111, 0b100, 0b000, 0b101, 0b110, 0b000]

cipher = []
for i in range(len(plain)):
    cipher.append(mapping_dict[plain[i]] ^ key[i])

print("암호문 :", end=' ')
for c in cipher:
    print(mapping_list[c], end='')
print()

decrypt = []
for i in range(len(cipher)):
    decrypt.append(mapping_list[cipher[i] ^ key[i]])

print("복호문 :", end=' ')
for d in decrypt:
    print(d, end='')