# 479A - Expression

a,b,c = int(input()),int(input()),int(input())
c1 = a+b*c
c2 = a*(b+c)
c3 = (a+b)*c
c4 = a*b+c
c5 = a*b*c
c6 = a+b+c
print(max(c1,c2,c3,c4,c5,c6))