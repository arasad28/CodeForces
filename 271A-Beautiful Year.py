a = int(input())
for i in range(8000):
    a = a+1
    b = str(a)
    if (b[0] != b[1]) and (b[0] != b[2]) and (b[0]!=b[3]) and (b[1]!= b[2]) and (b[1] != b[3]) and (b[2]!=b[3]):
        print(b)
        break