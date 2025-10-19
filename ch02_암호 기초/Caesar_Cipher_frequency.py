# 카이사르 암호화 브루트포스 공격

from collections import Counter

chiper = "YMNX NX F XNRUQJ JCFRUQJ. KWJVBJD TZFQNXNX HFS MJQU YT GWJFP HNUMJWZX"

letters = [c for c in chiper if c.isalpha()]
freq = Counter(letters)
print("Letter frequencies:", freq)

target = ['E', 'A', 'R', 'I', 'O'] # most 5

for chi, _ in freq.most_common(5):
    print("Case :", chi)
    for tar in target:
        key = (ord(chi) - ord(tar)) % 26
        print("Key ", key, ": ", end='')

        for char in chiper:
            if char.isalpha():
                print(chr((ord(char) - ord("A") - key) % 26 + ord('a')), end="")
            else:
                print(char, end="")
        print()
    print()