# 프로그램명 : linkedStackPalindrome.py
# 학과 작성자 : 정보통계학과 2019015007 김지희
# 작성일자 : 2022. 10. 19 (WED)
# 프로그램 설명 : 연결된 스택을 활용하여 회문인지 아닌지를 구별하는 프로그램

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

string = input('문자열 입력 : ')
ls = LinkedStack()
first = ''
result = ''

for i in string.lower():
    if i not in "@#\"$%^&/()~!?*,’'-+_\. ":
        first += i
        ls.push(i)

for _ in range(ls.size()):
    result += ls.pop()

if first == result:
    print('회문입니다.')
else:
    print('회문이 아닙니다.')