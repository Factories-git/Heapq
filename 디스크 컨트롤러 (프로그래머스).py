import heapq
#미완성 버전

def solution(jobs):
    answer = 0
    rng = [i[1] for i in jobs]
    queue = []
    time_work = {i:[] for i in range(max(rng))}

    for s, e in jobs:
        time_work[s].append([s, e])
    print(time_work)
    for i in range(sum(rng)):
        pass
    return answer

print(solution(	[[7, 8], [3, 5], [9, 6]]))