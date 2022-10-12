# 프로그램명 : stackFunction.py
# 학과 작성자 : 정보통계학과 2019015007 김지희
# 작성일자 : 2022. 10. 05 (WED)
# 프로그램 설명 : 스택의 기능을 구현하는 함수를 만들고 구현한 함수를 실행해보는 프로그램
    
top = [] # 스택 데이터 : 앞으로 요소들을 넣어줄 빈 리스트 top

def isEmpty(): # 스택이 비어 있는지 없는 지 확인
    return len(top) == 0 # 만약 스택이 비어있다면 True 반환

def push(item): # 요소를 넣기
    top.append(item) # 스택의 맨 뒤에 요소 item을 추가

def pop(): # 맨 뒤에서 요소를 하나 꺼내고 반환
    if not isEmpty(): # 만약 비어있지 않다면
        return top.pop(-1) # 맨 뒤의 요소를 꺼내고 반환

def peek(): # 맨 위의 요소를 삭제하지 않고 반환
    if not isEmpty(): # 만약 리스트가 비어있지 않다면
        return top[-1] # 맨 뒤의 요소를 반환

def size(): # 스택의 크기
    return len(top) # 리스트의 길이를 반환

def clear(): # 스택을 초기화
    global top # 전역변수 지정
    top = [] # 스택을 빈리스트로 초기화
    
for i in range(1,6): 
    push(i) # 1부터 5까지의 자연수 넣기
    
print('push 5회 :', top)
print('pop() -->', pop())
print('pop() -->', pop())
print('pop 2회 :', top)

push('홍길동')
push('이순신')

print('push+2회 :', top)
print('pop() -->', pop())
print('pop 1회 :', top)