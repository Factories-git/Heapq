import heapq

def solution(jobs):
    answer = 0
    queue = []
    now = []
    time_work = {i[0]:[] for i in jobs}

    for idx, i in enumerate(jobs):
        s, e = i[0], i[1]
        time_work[s].append([e, s, idx])
    ms = 0
    c = 0
    last = 0
    while True:
        if not time_work.get(ms) is None:
            for i in range(len(time_work[ms])):
                ms_work = time_work[ms][i]
                heapq.heappush(queue, (ms_work[0], ms_work[1], ms_work[-1]))
        if now:
            if now[0]+last == ms:
                answer += (now[0] + last) - now[1]
                now = []
                last = ms
                c += 1
        if queue:
            if not now:
                now = heapq.heappop(queue)

        if not now and len(jobs) == c:
            break
        ms += 1
        if not now:
            last += 1
    return answer//len(jobs)


print(solution(	[[7, 8], [3, 5], [9, 6]]))