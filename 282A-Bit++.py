# 282A - Bit++
n = int(input())
x = 0
 
for i in range(0,n):
    xx = input()
    if xx.count('+')==2:
        x +=1
    elif xx.count('-')==2:
        x -=1
print(x)