# 118A - String Task
l1 = input().lower()
l = list(l1)
vo = ['a','e','i','o','u','y']
new =[v for v in l if v not in vo]
for i in range(len(new)):
    print('.'+new[i],end='')