t = str(input())
if len(t) < 7:
    print('NO')
    exit()
else:
    z = 0
    o = 0
    for i in t:
        if z == 7 or o == 7:
            break
        elif i == '1':
            o += 1
            z = 0
        elif i == '0':
            z += 1
            o = 0
if z == 7 or o == 7:
    print('YES')
else:
    print('NO')
