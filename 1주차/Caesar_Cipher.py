# 1-1

chiper = "KHOOR"

for key in range(26):
    print("Key ", key, ": ", end='')

    for char in chiper:
        print(chr((ord(char) - ord("A") + key) % 26 + ord('a')), end="")
    print()