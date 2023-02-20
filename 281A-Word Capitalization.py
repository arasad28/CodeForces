# 281A - Word Capitalization
a = list(input()) 
x = a[0].upper()
l = [a[i] for i in range(1,len(a))]
l1 = list(x)+l
print(''.join(l1))