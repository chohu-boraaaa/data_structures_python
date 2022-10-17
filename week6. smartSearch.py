# 프로그램명 : smartSearch.py
# 학과 작성자 : 정보통계학과 2019015007 김지희
# 작성일자 : 2022. 10. 05 (WED)
# 프로그램 설명 : 우선순위 큐를 활용하여 미로를 탐색하는 프로그램

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
                if self.items[i][2] > self.items[highest][2]:
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

import math

(ox, oy) = (5,4)
def dist(x,y):
    (dx, dy) = (ox-x, oy-y)
    return math.sqrt(dx*dx+dy*dy)

def isValidPos(x, y):
    if x < 0  or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
        return False
    else:
        return map[y][x] == '0' or map[y][x] == 'x'

def MySmartSearch():
    q = PriorityQueue()
    q.enqueue((0,1,-dist(0,1)))
    print('PQueue: ')

    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2], end='->')
        x,y,_ = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y-1):
                q.enqueue((x,y-1,-dist(x,y-1)))
            if isValidPos(x, y+1):
                q.enqueue((x,y+1,-dist(x,y+1)))
            if isValidPos(x-1, y):
                q.enqueue((x-1,y,-dist(x-1,y)))
            if isValidPos(x+1, y):
                q.enqueue((x+1,y,-dist(x+1,y)))
        print('우선순위큐:', q.items)
    return False

# 미로
map = [['1', '1', '1', '1', '1', '1'],
       ['e', '0', '1', '0', '0', '1'],
       ['1', '0', '0', '0', '1', '1'],
       ['1', '0', '1', '0', '1', '1'],
       ['1', '0', '1', '0', '0', 'x'],
       ['1', '1', '1,' '1', '1', '1']]
MAZE_SIZE = 6

result = MySmartSearch()
if result :
    print(' --> 미로탐색 성공')
else:
    print(' --> 미로탐색 실패')