import heapq

hep = []
heapq.heapify(hep)
for i in range(9):
    heapq.heappush(hep,int(input()))
    heapq.heapify(hep)
    print(hep)