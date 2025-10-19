# RSA 실습

from math import gcd

def egcd(a: int, b: int):
    if b == 0:
        return a, 1, 0
    
    g, x1, y1 = egcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return g, x, y

def modinv(a: int, m: int) -> int:
    g, x, _ = egcd(a, m)

    if g != 1:
        raise ValueError(f"역원이 존재하지 않습니다: a={a}, m={m}, gcd={g}")
    
    return x % m


def generate_keys(p: int, q: int, e: int = 7):
    if p == q:
        raise ValueError("p와 q는 서로 다른 소수여야 합니다.")
    
    n = p * q
    phi = (p - 1) * (q - 1)

    if gcd(e, phi) != 1:
        raise ValueError(f"e와 φ(n)은 서로소여야 합니다. (e={e}, φ={phi})")

    d = modinv(e, phi)

    return (n, e), (n, d)


def encrypt(m: int, public_key: tuple[int, int]) -> int:
    n, e = public_key

    if not (0 <= m < n):
        raise ValueError(f"메시지 m은 0 <= m < n 이어야 합니다. (m={m}, n={n})")

    c = m ** e % n # pow(m, e, n) 연산

    return c


def decrypt(c: int, private_key: tuple[int, int]) -> int:
    n, d = private_key

    if not (0 <= c < n):
        raise ValueError(f"암호문 c는 0 <= c < n 이어야 합니다. (c={c}, n={n})")
    
    m = c ** d % n

    return m


# ========================
# 데모 실행
# ========================

def demo_keygen():
    public_key, private_key = generate_keys(17, 11, e=7)
    print("공개키 (n, e):", public_key)
    print("개인키 (n, d):", private_key)


def demo_integer():
    public_key, private_key = generate_keys(17, 11, e=7)
    message = 88  # 0 <= m < n(=187) 범위 내
    cipher = encrypt(message, public_key)
    plain = decrypt(cipher, private_key)
    print(f"[정수] 원본={message}, 암호문={cipher}, 복호화={plain}")


def demo_text():
    public_key, private_key = generate_keys(17, 11, e=7)
    text = "HI"
    nums = [ord(ch) for ch in text]  # 문자열 → 아스키 코드 변환
    cipher_nums = [encrypt(m, public_key) for m in nums]
    plain_nums = [decrypt(c, private_key) for c in cipher_nums]
    decrypted_text = "".join(chr(x) for x in plain_nums)
    print(f"[문자열] 원문={text}")
    print(f"[문자열] 암호문={cipher_nums}")
    print(f"[문자열] 복호화={decrypted_text}")


def run_all():
    print("=== 1) 키 생성 ===")
    demo_keygen()
    print("\n=== 2) 정수 메시지 암/복호화 ===")
    demo_integer()
    print("\n=== 3) 문자열 암/복호화 ===")
    demo_text()


if __name__ == "__main__":
    run_all()
