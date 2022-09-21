# 2주차 실습과제_Bag ADT 구현
# 2022-09-14 정보통계학과 2019015007 김지희

# bag에 e가 있는지 여부 판단하는 함
def contains(bag, e):
    return e in bag

# bag에 e를 추가해주는 함수
def insert(bag, e):
    bag.append(e)

# bag에서 e를 제거해주는 함수
def remove(bag, e):
    bag.remove(e)

# bag에 있는 것들에 개수를 반환하는 함수    
def count(bag):
    return len(bag)

myBag = [] # 요소들을 넣어줄 빈리스트
insert(myBag, '휴대폰')
insert(myBag, '지갑')
insert(myBag, '손수건')
insert(myBag, '빗')
insert(myBag, '자료구조')
insert(myBag, '야구공')
print('가방 속의 물건 : ', myBag)

insert(myBag, '빗')
remove(myBag, '손수건')
print('가방 속의 물건 : ', myBag)

