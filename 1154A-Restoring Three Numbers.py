x,y,z,w = map(int,input().split())

if x > y and x > z and x > w:
    print(f'{x-y} {x-z} {x-w}')
elif y > x and y > z and y >w:
    print(f'{y-x} {y-z} {y-w}')
elif z > x and z > y and z > w:
    print(f'{z-x} {z-y} {z-w}')
else:
    print(f'{w-x} {w-y} {w-z}')
