# 프로그램명 : linkedDeque.py
# 학과 작성자 : 정보통계학과 2019015007 김지희
# 작성일자 : 2022. 10. 19 (WED)
# 프로그램 설명 : 연결된 덱 구현하고 구현한 연결된 덱의 연산을 수행하는 프로그램

class DNode:
    def __init__(self, elem, prev=None, next=None):
        self.data = elem
        self.prev = prev
        self.next = next

class DoublyLinkedDeque:
    def __init__(self):
        self.front = None
        self.rear = None
    def isEmpty(self):
        return self.front == None
    def clear(self):
        self.front = self.rear = None
    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            node = self.front.next 
            while not node == None:
                node = node.next
                count += 1
            return count
    def addFront(self, item):
        node = DNode(item, None, self.front)
        if(self.isEmpty()):
            self.front = self.rear = node
        else:
            self.front.prev = node
            self.front = node
    def addRear(self, item):
        node = DNode(item, self.rear, None)
        if(self.isEmpty()):
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node
    def deleteFront(self):
        if not self.isEmpty():
            data = self.front.data
            self.front = self.front.next
            if self.front == None:
                self.rear = None
            else:
                self.front.prev = None
            return data
    def deleteRear(self):
        if not self.isEmpty():
            data = self.rear.data
            self.rear = self.rear.prev
            if self.rear == None:
                self.front = None
            else:
                self.rear.next = None
            return data
    def display(self, msg='CircularLinkedDeque: '):
        print(msg, end='')
        if not self.isEmpty():
            node = self.front
            while not node == self.rear:
                print(node.data, end=' ')
                node = node.next
            print(node.data, end=' ')
        print()
        
dq = DoublyLinkedDeque()
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