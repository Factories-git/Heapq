import heapq

n = int(input())
heap = []
for _ in range(n):
    nums = list(map(int, input().split()))
    for i in nums:
        if len(heap) < n:
            heapq.heappush(heap, i)
        else:
            if heap[0] < i:
                heapq.heappushpop(heap, i)
print(heap[0])