# SHA-3 (Keccak) 해시 함수 구현

import hashlib

messages = ["hello", "hello!"]

# 각 문자열의 SHA3-256 해시 계산
for msg in messages:
    # SHA3-256 해시 계산
    hash_value = hashlib.sha3_256(msg.encode()).hexdigest()
    
    print(f"입력: {msg} -> SHA3-256 해시: {hash_value}")