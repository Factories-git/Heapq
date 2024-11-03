import heapq,sys

input = sys.stdin.readline
print = sys.stdout.write

min_pq = []
max_pq = []
heapq.heapify(min_pq)
heapq.heapify(max_pq)

def pop(heap,deletes):
    back = []
    while heap:
        s = heapq.heappop(heap)
        if s not in deletes:
            heapq.heappush(back, s)
        else:
            break
    heap = back
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
                    deletes.add(d)
                    max_heap = pop(max_heap, deletes)
                else:
                    d = -heapq.heappop(max_heap)
                    deletes.add(d)
                    min_heap = pop(min_heap, deletes)

        deletes = set()
    return f'{-max_heap[0]} {min_heap[0]}' if max_heap and min_heap else 'EMPTY'


for _ in range(int(input())):
    operation = []
    delete = set()
    for i in range(int(input())):
        operation.append(list(map(str ,input().split())))
    print(f'{Dual_Prioirity_queue(max_pq, min_pq, operation, delete)}\n')