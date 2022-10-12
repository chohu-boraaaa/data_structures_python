# 프로그램명 : depthSearchFirst.py
# 학과 작성자 : 정보통계학과 2019015007 김지희
# 작성일자 : 2022. 10. 05 (WED)
# 프로그램 설명 : 깊이 우선 탐색을 구현하는 프로그램

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


# (x,y)가 갈 수 있는 방인지 검사하는 함수
def isValidPos(x, y):
    if x<0 or y<0 or x>=MAZE_SIZE or y>=MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'
    
def DFS():
    stack = Stack()
    stack.push( (0, 1) )
    print('DFS: ')
    
    while not stack.isEmpty():
        here = stack.pop()
        print(here, end='->')
        (x, y) = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y-1): stack.push((x, y-1))
            if isValidPos(x, y+1): stack.push((x, y+1))
            if isValidPos(x-1, y): stack.push((x-1, y))
            if isValidPos(x+1, y): stack.push((x+1, y))
        print('현재 스택 :', stack)
        
    return False

# 미로
map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '0', '0', '0', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '1', '1', '0', '0', 'x'],
       ['1', '1', '1', '0', '1', '1'],
       ['1', '1', '1,' '1', '1', '1']]
MAZE_SIZE = 6

result = DFS()
if result :
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')