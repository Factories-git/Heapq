from collections import Counter

n, m = map(int, input().split())
student = []
for _ in range(n):
    k = int(input())
    students = list(map(int, input().split()))
    for i in students:
        student.append(i)
stu_ = Counter(student)
re = 0

for K,c in stu_.items():
    if c >= m:
        re += 1
print(re)