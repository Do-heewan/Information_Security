# 생일 공격 시뮬레이션

import random
import hashlib

def random_message(length: int=16) -> str:
    """
    길이가 length인 무작위 대소문자 문자열 생성
    """
    # word = ''
    # for _ in range(length):
    #     word += chr(random.randint(65, 90))
    word = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz', k=length))
    return word

def sha_256(msg: str) -> bytes:
    """
    SHA-256 해시 변환 함수.
    앞 2바이트만 반환.
    """
    return hashlib.sha256(msg.encode()).digest()[:2] # 해시 변환 후 앞 2바이트 반환

def birthday_attack(max_attempts: int=100000) -> int | None:
    """
    생일 공격 시뮬레이션 진행 함수
    새로운 메세지를 생성하고, 해시 변환값이 중복될 때까지 반복.
    최대 max_attempts번 시도 후 중단.
    해시 변환값이 중복되면, 그 때까지의 시도 횟수를 반환, 중복이 없으면 None 반환.
    """
    seen = {}
    attempts = 0
    while attempts < max_attempts:
        message = random_message() # 메세지 길이 설정 (기본값 16)
        sha_256_msg = sha_256(message) # 해시 변환값 (앞 2바이트)

        # print(f"원본 메세지 : {message}, 해시 변환값 : {sha_256_msg}")
        attempts += 1
        if sha_256_msg in seen:
            # print(seen)
            return attempts
        seen[sha_256_msg] = True
    return None

def run_simulation(trials: int=50):
    """
    trials 횟수만큼 생일 공격 시뮬레이션을 수행하고,
    각 시도에서 해시 충돌이 발생한 시도 횟수의 평균을 출력.
    기본값 50회 시도
    """
    result = []

    for i in range(1, trials+1):
        res = birthday_attack()
        if res is None:
            print(f"[Attempts {i}] 충돌 없음")
            continue

        result.append(res)
        # print(f"[Attempts {i}] {res}회 만에 중복 발견")

    if not result:
        print("시도 결과가 없습니다.")
        return None

    average = sum(result) / len(result)

    print("시도 횟수들 :", result)
    print(f"시도 횟수 평균: {average:.2f} (총 {len(result)}회 시도)")

if __name__ == "__main__":
    run_simulation(trials=50)
