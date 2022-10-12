# 프로그램명 : postFixCalculator.py
# 학과 작성자 : 정보통계학과 2019015007 김지희
# 작성일자 : 2022. 10. 05 (WED)
# 프로그램 설명 : 표기 방법이 후위수식일 때 계산을 수행하는 프로그램

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
            
def evalPostfix(expr):
    s = Stack()
    for token in expr:
        if token in '+-*/':
            val2 = s.pop()
            val1 = s.pop()
            if (token == '+'): s.push(val1 + val2)
            elif(token == '-'): s.push(val1 - val2)
            elif(token == '*'): s.push(val1 * val2)
            elif(token == '/'): s.push(val1 / val2)
        else:
            s.push(float(token))
    return s.pop()                

expr1 = ['8', '2', '/', '3', '-', '3', '2', '*', '+']
expr2 = ['1', '2', '/', '4', '*', '1', '4', '/', '*']
print(expr1, '-->', evalPostfix(expr1))
print(expr2, '-->', evalPostfix(expr2))