# 2주차 실습과제_피보나치 순환 함수 구현
# 2022-09-14 정보통계학과 2019015007 김지희
import time

# 피보나치 순환 함수
def fib_cycle(n):
    if n == 0: # 0 이라면
        return 0 # 0을 반환
    elif n == 1: # 1이라면
        return 1 # 1을 반환
    else: # 그 외
        return fib_cycle(n-1) + fib_cycle(n-2) # 직전 두 숫자 더하기

start = time.time()
print(fib_cycle(30)) # 답 : 832040
end = time.time()
print('실행시간 =', end - start) # 실행시간 =  0.3437159061431885
