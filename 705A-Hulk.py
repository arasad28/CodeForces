# 705A - Hulks

n = int(input())
txt = ''
for i in range(1,n+1):
    txt += 'that '
    if i%2 !=0:
        txt += 'I hate '
    elif i%2 ==0:
        txt += 'I love '

txt = txt+'it'
print(txt[5:])