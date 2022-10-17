# 프로그램명 : breadthFirstSearch.py
# 학과 작성자 : 정보통계학과 2019015007 김지희
# 작성일자 : 2022. 10. 05 (WED)
# 프로그램 설명 : 큐를 활용하여 너비 우선 탐색을 구현하여 미로를 탐색하는 프로그램

MAX_QSIZE = 10 # 원형 큐의 크기

class CircularQueue: # 원형 큐 클래스
    def __init__(self): # CircularQueue의 생성자
        self.front = 0 # 큐의 전단 위치
        self.rear = 0 # 큐의 후단 위치
        self.items = [None] * MAX_QSIZE # 항목 저장을 위한 리스트
    def isEmpty(self): # 원형 큐가 비어있는지 확인
        return self.front == self.rear # 전단 위치와 후단 위치가 같으면 큐가 비어있음
    def isFull(self): # 원형 큐가 차있는지 확인
        return self.front == (self.rear+1) % MAX_QSIZE 
    def clear(self): # 전단 위치와 후단 위치를 같게 만들어 원형 큐를 클리어
        self.front = self.rear
    def enqueue(self, item): # 삽입 연산
        if not self.isFull(): # 포화 상태가 아니면
            self.rear = (self.rear+1)%MAX_QSIZE # rear 회전
            self.items[self.rear] = item # rear 위치에 삽입
    def dequeue(self): # 삭제 연산
        if not self.isEmpty(): # 공백 상태가 아니면
            self.front = (self.front+1)%MAX_QSIZE # front 회전
            return self.items[self.front] # front 위치 항목 반환
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1)%MAX_QSIZE]
    def size(self):
        return (self.rear-self.front + MAX_QSIZE) % MAX_QSIZE
    def display(self):
        out = []
        if self.front < self.rear:
            out= self.items[self.front+1:self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE]\
                +self.items[0:self.rear+1]
        print('[f=%s, r=%d] ==> ' % (self.front, self.rear), out)

def isValidPos(x, y):
    if x < 0  or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def BFS():
    que = CircularQueue()
    que.enqueue((0,1))
    print('BFS: ')

    while not que.isEmpty():
        here = que.dequeue()
        print(here, end='->')
        x, y = here
        if(map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y-1):
                que.enqueue((x, y-1))
            if isValidPos(x, y+1):
                que.enqueue((x, y+1))
            if isValidPos(x-1, y):
                que.enqueue((x-1, y))
            if isValidPos(x+1, y):
                que.enqueue((x+1, y))
    return False    

# 미로
map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '1', '0', '0', '1'],
       ['1', '0', '0', '0', '1', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '0', '1', '0', '0', 'x'],
       ['1', '1', '1,' '1', '1', '1']]
MAZE_SIZE = 6

result = BFS()
if result :
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')