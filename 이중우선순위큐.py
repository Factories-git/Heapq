import heapq,sys
from collections import Counter

input = sys.stdin.readline

min_pq = []
max_pq = []
heapq.heapify(min_pq)
heapq.heapify(max_pq)

def pop(heap,deletes):
    while True:
        s = heapq.heappop(heap)
        if s in deletes:
            heapq.heappush(heap, s)
        else:
            break
    return heap


def Dual_Prioirity_queue(max_heap,min_heap, operations, deletes):
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(min_heap, int(i[1]))
            heapq.heappush(max_heap, -int(i[1]))
        elif i[0] == 'D':
            if min_heap and max_heap:
                if int(i[1]) < 0:
                    d = heapq.heappop(min_heap)
                    deletes.append(d)
                    pop(max_heap, deletes)
                else:
                    d = -heapq.heappop(max_heap)
                    deletes.append(d)
                    pop(min_heap, deletes)
    print(max_heap, min_heap, deletes)
    return f'{max_heap[0]} {min_heap[0]}' if max_heap and min_heap else 'EMPTY'


for _ in range(int(input())):
    operation = []
    delete = []
    for i in range(int(input())):
        operation.append(list(map(str ,input().split())))
    print(Dual_Prioirity_queue(max_pq, min_pq, operation, delete))