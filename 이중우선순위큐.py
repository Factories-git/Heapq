import heapq
import sys
def solution(operations):
    que = []
    max_que = []
    heapq.heapify(que)
    heapq.heapify(max_que)
    for i in operations:
        if i[0] == 'I':
            l = list(i)
            heapq.heappush(que,int(i[2:]))
            heapq.heappush(max_que,-int(i[2:]))
        elif i == 'D -1\n':
            if que != []:
                heapq.heappop(que)
                heapq.heappop(max_que)
        elif i == 'D 1\n':
            heapq.heappop(max_que)
            heapq.heapify(que)
    if que != []:
        return f'{max(max_que)} {min(que)}'
    else:
        return 'EMPTY'
operations = []
for i in range(int(input())):
    for j in range(int(input())):
        operations.append(sys.stdin.readline())

    sys.stdout.write(solution(operations))

'''
2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
'''