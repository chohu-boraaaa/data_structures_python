# 프로그램명 : CircularLinkedQueue.py
# 학과 작성자 : 정보통계학과 2019015007 김지희
# 작성일자 : 2022. 10. 19 (WED)
# 프로그램 설명 : 연결된 큐 클래스를 구현하고 구현한 연결된 큐 연산을 수행하는 프로그램

class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link
        
class CircularLinkedQueue:
    def __init__(self):
        self.tail = None
    def isEmpty(self):
        return self.tail == None
    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data
    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            node.link = node
            self.tail = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node
    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data
    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            node = self.tail.link 
            while not node == self.tail:
                node = node.link
                count += 1
            return count
    def display(self, msg='CircularLinkedQueue: '):
        print(msg, end='')
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                print(node.data, end=' ')
                node = node.link
            print(node.data, end=' ')
        print()

q = CircularLinkedQueue()
for i in range(8):
    q.enqueue(i)
q.display()
for i in range(5):
    q.dequeue()
q.display()
for i in range(8, 14):
    q.enqueue(i)
q.display()
