import queue
def solve():
    n = int(input())
    s = list(map(int,input().split()))
    q= queue.PriorityQueue()
    cnt = 0
    for i in s:
        if i > 0:
            q.put(-i)
        elif not q.empty():
            cnt -= q.get()
    print(cnt)

t = int(input())
for _ in range(t):
    solve()
