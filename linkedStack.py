# 프로그램명 : linkedStack.py
# 학과 작성자 : 정보통계학과 2019015007 김지희
# 작성일자 : 2022. 10. 19 (WED)
# 프로그램 설명 : 연결된 스택을 구현하고 구현한 연결된 스택의 연산을 수행하는 프로그램
    
class Node:
    def __init__(self, elem, link=None):
        self.data = elem
        self.link = link
        
class LinkedStack:
    def __init__(self):
        self.top = None
    def isEmpty(self):
        return self.top == None
    def clear(self):
        self.top = None
    def push(self, item):
        n = Node(item, self.top)
        self.top = n
    def pop(self):
        if not self.isEmpty():
            n = self.top
            self.top = n.link
            return n.data
    def peek(self):
        if not self.isEmpty():
            return self.top.data
    def size(self):
        node = self.top
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count
    def display(self, msg='LinkedStack:'):
        print(msg, end='')
        node = self.top
        while not node == None:
            print(node.data, end = ' ')
            node = node.link
        print()

odd = LinkedStack()
even = LinkedStack()

for i in range(10):
    if i%2 == 0:
        even.push(i)
    else:
        odd.push(i)
    
even.display('even Linked Stack:')
odd.display('odd Linked Stack:')

print('Linked Stack even peek:', end = '')
print(even.peek())
print('Linked Stack odd peek:', end = '')
print(odd.peek())

for _ in range(2):
    even.pop()
for _ in range(3):
    odd.pop()

even.display('Linked Stack even pop 2회:')    
odd.display('Linked Stack odd pop 3회:')
