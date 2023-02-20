# 236A - Boy or Girl
a = input()
x = ''.join(set(a))
if len(x)%2 ==0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")