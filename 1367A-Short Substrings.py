n = int(input())
for i in range(n):
    t = str(input())
    rst = t[0:2]
    for j in range(3,len(t),2):
        rst += t[j]
    print(rst)
