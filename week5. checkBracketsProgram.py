# 프로그램명 : checkBracketsProgram.py
# 학과 작성자 : 정보통계학과 2019015007 김지희
# 작성일자 : 2022. 10. 05 (WED)
# 프로그램 설명 : 가장 가까운 거리에 있는 괄호들끼리 서로 짝을 이루는지 확인하는 괄호 검사 프로그램

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
        
def checkBrackets(statement): # 괄호 검사하는 함수
    stack = Stack() # 객체 생성
    
    for ch in statement: 
        if ch in ('{', '[', '('): # 만약 문자열에 '{', '[', '('이 포함되어 있다면
            stack.push(ch) # 해당 괄호를 넣기
    
        elif ch in ('}', ']', ')'): # 만약 문자열에 '}', ']', ')'이 포함되어 있으나
            if stack.isEmpty(): # 만약 스택이 비어있다면
                return False # False를 반환
        
            else: # 스택이 비어있지 않다면 서로 다른 형태의 괄호가 짝을 이루는 경우 False를 반
                left = stack.pop()
                if (ch == '}' and left != '{') or (ch == ']' and left != '[') or (ch == ')' and left != '('):
                   return False
    
    return stack.isEmpty()

string = ('{ A[(i+1)] = 0; }', 'if( (i==0) && (j==0)', 'A[ (i+1]) = 0;')

for s in string:
    m = checkBrackets(s)
    print(s, '-->', m)