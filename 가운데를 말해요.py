import heapq
import sys

he = []
heapq.heapify(he)
for i in range(int(input())):
    heapq.heappush(he,int(sys.stdin.readline().split()[0]))
    heapq.heapify(he)
    if len(he) % 2 == 1:
        print(he[len(he)//2 : len(he)//2+1][0])
        heapq.heapify(he)

    elif len(he) % 2 == 0:
        f = len(he) / 2
        s1 = int(f) - 1
        m = int(f)
        answer = he[s1:m + 1]
        print(min(answer))
        heapq.heapify(he)
    heapq.heapify(he)
    print(he)