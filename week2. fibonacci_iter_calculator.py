# 2주차 실습과제_피보나치 반복문 활용 함수 구현
# 2022-09-14 정보통계학과 2019015007 김지희

import time

# 피보나치 반복문 활용 함수
def fib_iter(n):
    if (n<2): # 만약 n이 2보다 작은 경우
        return n # 그대로를 반환
    last = 0
    current = 1
    for i in range(2, n+1): # 2부터 n까지 증가하며 반복
        tmp = current 
        current += last
        last = tmp
    
    return current

start = time.time()
print(fib_iter(30)) # 답 : 832040
end = time.time()
print('실행시간 :', end - start) # 실행 시간 : 0.0