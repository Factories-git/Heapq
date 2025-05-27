import heapq
import sys

input = sys.stdin.readline

t = int(input())
for i in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    heapq.heapify(s)
    re = 0
    while len(s) > 1:
        file1 = heapq.heappop(s)
        file2 = heapq.heappop(s)
        c_file = file1 + file2
        re += c_file
        heapq.heappush(s, c_file)
    print(re)