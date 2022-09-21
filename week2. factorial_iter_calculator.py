# 2주차 실습과제_팩토리얼 반복문 활용 함수 구현
# 2022-09-14 정보통계학과 2019015007 김지희

import time

# 팩토리얼 반복문 활용 함수 구현
def factorial_iter(n):
    result = 1 # 초깃값
    for i in range(n, 0, -1): # i가 n부터 감소하면서 반복하며
        result *= i # 곱해주기
    return result

# 3! 출력 결과
start = time.time()
print('결과:', factorial_iter(3))
end = time.time()
print('실행 시간 :', end - start)