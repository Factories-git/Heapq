import heapq, sys

input = sys.stdin.readline
print = sys.stdout.write

min_pq = []
max_pq = []
heapq.heapify(min_pq)
heapq.heapify(max_pq)


def pop(heap, deletes):
    while heap:
        v, n = heapq.heappop(heap)
        if n == deletes:
            break
    return heap


def Dual_Prioirity_queue(max_heap, min_heap, operations, deletes):
    for k in range(len(operations)):
        if operations[k][0] == 'I':
            heapq.heappush(min_heap, (int(operations[k][1]), k))
            heapq.heappush(max_heap, (-int(operations[k][1]), k))
        elif operations[k][0] == 'D':
            if min_heap and max_heap:
                if int(operations[k][1]) < 0:
                    d,deletes = heapq.heappop(min_heap)
                    max_heap = pop(max_heap, deletes)
                else:
                    d, deletes = heapq.heappop(max_heap)
                    min_heap = pop(min_heap, deletes)

    return f'{max_heap} {min_heap}' if max_heap and min_heap else 'EMPTY'


for _ in range(int(input())):
    operation = []
    delete = set()
    for i in range(int(input())):
        operation.append(list(map(str, input().split())))
    print(f'{Dual_Prioirity_queue(max_pq, min_pq, operation, delete)}\n')
