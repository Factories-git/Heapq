import sys
import heapq

heap = []
heapq.heapify(heap)
for i in range(int(input())):
    ipt = int(sys.stdin.readline())
    if ipt != 0:
        heapq.heappush(heap, -int(ipt))
    else:
        if heap != []:
            max_val = -heapq.heappop(heap)
            print(max_val)
        else:
            print(0)

