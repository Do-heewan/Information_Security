# 2-1 이중 전위 암호

import numpy as np

plain = "attackatdawn"

cipher = np.array(list(plain)).reshape(3, 4)
cipher = cipher[[2, 1, 0], :]
cipher = cipher[:, [3, 1, 0, 2]]
print("암호화 :", end=' ')
print(''.join(cipher.flatten().tolist()))

decrypt = cipher[:, [2, 1, 3, 0]]
decrypt = decrypt[[2, 1, 0], :]
print("복호화 :", end=' ')
print("".join(decrypt.flatten().tolist()))