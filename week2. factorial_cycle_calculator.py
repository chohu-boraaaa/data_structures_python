# 2주차 실습과제_팩토리얼 순환 함수 구현
# 2022-09-14 정보통계학과 2019015007 김지희

import time

# 팩토리얼 순환 함수 구현
def factorial_cycle(n):
    if n == 1: # 만약 1이라면
        return 1 # 1을 반환하여 순환 종료
    else: # 1이 아니라면
        return n * factorial_cycle(n-1) # n * (n-1) * ... 계산 가능하도록 구현

# 3! 출력 결과
start = time.time()
print('결과:', factorial_cycle(3))
end = time.time()
print('실행 시간 :', end - start)