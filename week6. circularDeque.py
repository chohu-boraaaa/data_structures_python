# 프로그램명 : circularDeque.py
# 학과 작성자 : 정보통계학과 2019015007 김지희
# 작성일자 : 2022. 10. 05 (WED)
# 프로그램 설명 : 원형 덱 클래스를 구현하고 이를 이용하여 원형 덱의 연산들을 수행하고 출력하는 프로그램

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
        
class CircularDeque(CircularQueue):
    def __init__(self):
        super().__init__()
    def addRear(self, item):
        self.enqueue(item)
    def deleteFront(self):
        return self.dequeue()
    def getFront(self):
        return self.peek()
    def addFront(self, item):
        if not self.isFull():
            self.items[self.front] = item
            self.front = self.front - 1
            if self.front < 0:
                self.front = MAX_QSIZE-1
    def deleteRear(self):
        if not self.isEmpty():
            item = self.items[self.rear]
            self.rear = self.rear - 1
            if self.rear < 0:
                self.rear = MAX_QSIZE - 1
            return item
    def getRear(self):
        return self.items[self.rear]

dq = CircularDeque()
for i in range(9):
    if i%2 == 0: # 짝수는 후단에 삽입
        dq.addRear(i)
    else: # 홀수는 전단에 삽입
        dq.addFront(i)
dq.display()
for i in range(2):
    dq.deleteFront()
for i in range(3):
    dq.deleteRear()
dq.display()
for i in range(9,14):
    dq.addFront(i)
dq.display()