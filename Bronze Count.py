import heapq
import sys

input = sys.stdin.readline

l = []
heap = set()
for i in range(int(input())):
    ipt = int(input())
    l.append(ipt)
    heap.add(-ipt)
heap = list(heap)
heapq.heapify(heap)
heapq.heappop(heap)
heapq.heappop(heap)
s = -heapq.heappop(heap)
print(s, l.count(s))