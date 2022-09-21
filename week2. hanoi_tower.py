# 2주차 실습과제_하노이탑 문제 구현
# 2022-09-14 정보통계학과 2019015007 김지희

# 하노이탑 순환함수
def hanoi_tower(n, fr, tmp, to):
    if (n == 1): # 종료 조건
        print('원판 1: %s --> %s' % (fr, to)) # 가장 작은 원판 옮김
    else:
        hanoi_tower(n-1, fr, to, tmp) # n-1개를 to를 이용해 tmp로
        print('원판 %d: %s --> %s' % (n, fr, to)) # 원판 하나 옮기기
        hanoi_tower(n-1, tmp, fr, to) # n-1개를 fr 이용해 to로
    
hanoi_tower(4, 'A', 'B', 'C') # 4개 원판 있는 경우 출력