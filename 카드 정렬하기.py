import heapq, sys

input = sys.stdin.readline
heap = []
heapq.heapify(heap)
for i in range(int(input())):
    heapq.heappush(heap,int(input()))

s = 0
while len(heap) >= 2:
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    re = a + b
    s += re
    heapq.heappush(heap, re)
print(s)