# 프로그램명 : priorityQueue.py
# 학과 작성자 : 정보통계학과 2019015007 김지희
# 작성일자 : 2022. 10. 05 (WED)
# 프로그램 설명 : 우선순위 큐 클래스를 구현하고 우선순위가 높은 항목이 순서대로 나오게 하는 프로그램

class PriorityQueue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return len(self.items) == 0
    def size(self):
        return len(self.items)
    def clear(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def findMaxIndex(self):
        if self.isEmpty():
            return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.items[i] > self.items[highest]:
                    highest = i
            return highest
    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items.pop(highest)
    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None:
            return self.items[highest]
 
q = PriorityQueue()
q.enqueue(34)
q.enqueue(18)
q.enqueue(27)
q.enqueue(45)
q.enqueue(15)

print('PQueue :', q.items)
while not q.isEmpty():
    print('Max Priority =', q.dequeue())
