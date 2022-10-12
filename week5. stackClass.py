# 프로그램명 : stackClass.py
# 학과 작성자 : 정보통계학과 2019015007 김지희
# 작성일자 : 2022. 10. 05 (WED)
# 프로그램 설명 : 스택의 기능을 구현하는 클래스를 만들고 구현한 클래스의 객체를 만들어 연산을 실행해보는 프로그램

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

print('방법 1. 리스트 객체 출력-------------------------')
odd = Stack()
even = Stack()

for i in range(10):
    if i%2 == 0:
        even.push(i)
    else:
        odd.push(i)
print('스택 even push 5회 :', even.top)
print('스택 odd push 5회 :', odd.top)
print('스택 even peek :', even.peek())
print('스택 odd peek :', odd.peek())

for _ in range(2):
    even.pop()
for _ in range(3):
    odd.pop()

print('스택 even pop 2회 :', even.top)    
print('스택 odd pop 3회 :', odd.top)

print('')
print('방법 2. 연산자 중복 + 슬라이싱 기법-------------------------')

odd = Stack()
even = Stack()

for i in range(10):
    if i%2 == 0:
        even.push(i)
    else:
        odd.push(i)

print('스택 even push 5회 :', even)
print('스택 odd push 5회 :', odd)
print('스택 even peek :', even.peek())
print('스택 odd peek :', odd.peek())

for _ in range(2):
    even.pop()
for _ in range(3):
    odd.pop()

print('스택 even pop 2회 :', even)    
print('스택 odd pop 3회 :', odd)