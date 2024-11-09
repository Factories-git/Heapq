import heapq
buffer = []
heapq.heapify(buffer)


#
def synchronize(heap):  # 데이터 힙과 삭제 버퍼 동기화
    while (heap and buffer) and heap[0] == buffer[0]:
        heapq.heappop(heap)
        heapq.heappop(buffer)


def erase(heap, x):  # 임의의 값 삭제
    heapq.heappush(buffer, x*-1)
    synchronize(heap)


def pop(heap):  # 최솟값 조회 및 삭제
    x = heapq.heappop(heap)
    synchronize(heap)
    return x


def DualPriortyQueue(operations, min_heap, max_heap):
    for oper in range(len(operations)):
        if operations[oper][0] == 'I':
            heapq.heappush(min_heap, int(operations[oper][1]))
            heapq.heappush(max_heap, -int(operations[oper][1]))
        else:
            if max_heap and min_heap:
                if int(operations[oper][1]) == 1:
                    erase(min_heap, pop(max_heap))
                    synchronize(min_heap)
                else:
                    erase(max_heap, pop(min_heap))
                    synchronize(max_heap)

    return f'{-max_heap[0]} {min_heap[0]}' if max_heap and min_heap else 'EMPTY'


min_pq = []
max_pq = []
heapq.heapify(min_pq)
heapq.heapify(max_pq)
for _ in range(int(input())):
    operation = []
    buffer = []
    for i in range(int(input())):
        operation.append(list(map(str, input().split())))
    print(f'{DualPriortyQueue(operation, min_pq, max_pq)}')

