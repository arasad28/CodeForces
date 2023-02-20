# 59A - Word
m = str(input())
x = (sum(1 for i in m if i.isupper()))
y = (sum(1 for i in m if i.islower()))
if x>y:
    print(m.upper())
else:
    print(m.lower())