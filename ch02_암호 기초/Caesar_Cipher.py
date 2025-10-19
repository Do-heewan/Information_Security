# 카이사르 암호화

chiper = "KHOOR"

for key in range(26):
    print("Key ", key, ": ", end='')

    for char in chiper:
        print(chr((ord(char) - ord("A") + key) % 26 + ord('a')), end="")
    print()