# 프로그램명 : palindrome.py
# 학과 작성자 : 정보통계학과 2019015007 김지희
# 작성일자 : 2022. 10. 05 (WED)
# 프로그램 설명 : 실습문제 2. 회문인지 아닌지 판별하는 프로그램

class Stack: # 스택 클래스
    def __init__(self): # 생성자
        self.top = [] # top이 클래스의 멤버변수가 됨
        
    def isEmpty(self): # 스택이 비어있는지 여부
        return len(self.top) == 0
    
    def size(self): # 스택의 크기
        return len(self.top) # 리스트의 길이를 반환

    def clear(self): # 스택을 초기화
        self.top = [] # 스택을 빈리스트로 초기화

    def push(self, item): # 요소를 넣기
        self.top.append(item) # 스택의 맨 뒤에 요소 item을 추가

    def pop(self): # 맨 뒤에서 요소를 하나 꺼내고 반환
        if not self.isEmpty(): # 만약 비어있지 않다면
            return self.top.pop(-1) # 맨 뒤의 요소를 꺼내고 반환

    def peek(self): # 맨 위의 요소를 삭제하지 않고 반환
        if not self.isEmpty(): # 만약 리스트가 비어있지 않다면
            return self.top[-1] # 맨 뒤의 요소를 반환
    
    def __str__(self):
        return str(self.top[::-1])

string = input('문자열 입력 : ')
s = Stack()
result = []


for i in string.lower():
    if i not in "@#\"$%^&()~!?*,’'-+_\. ":
        s.push(i)
        
first = s.top.copy()
    
for _ in range(s.size()):
    if s.peek() in "@#$%\"^&()~!?*,’'-+_\. " :
        s.pop()
    else:
        result += s.pop()

if ''.join(first) == ''.join(result):
    print('회문입니다.')
else:
    print('회문이 아닙니다.')
