"""
12% 틀렸습니다
"""

import heapq

buffer = []
m_buffer = []
heapq.heapify(buffer)
heapq.heapify(m_buffer)


#
def synchronize(heap, buffer):  # 데이터 힙과 삭제 버퍼 동기화
    while (heap and buffer) and heap[0] == buffer[0]:
        heapq.heappop(heap)
        heapq.heappop(buffer)


def erase(x):  # 임의의 값 삭제
    heapq.heappush(buffer, x*-1)


def pop(heap):  # 최솟값 조회 및 삭제
    x = heapq.heappop(heap)
    return x


min_pq = []
max_pq = []
heapq.heapify(min_pq)
heapq.heapify(max_pq)
for _ in range(int(input())):
    operation = []
    buffer = []
    for i in range(int(input())):
        operation = list(map(str, input().split()))
        if operation[0] == 'I':
            heapq.heappush(min_pq, int(operation[1]))
            heapq.heappush(max_pq, -int(operation[1]))
        else:
            if max_pq and min_pq:
                if int(operation[1]) == 1:
                    erase(pop(max_pq))
                else:
                    erase(pop(min_pq))
            synchronize(min_pq, buffer)
            synchronize(max_pq, buffer)
    print(f'{-max_pq[0]} {min_pq[0]}' if max_pq and min_pq else 'EMPTY')
