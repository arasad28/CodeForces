# 131A - cAPS lOCK

s = str(input())
if s[0].islower() and s[1:].isupper():
    print(s.capitalize())    
elif s.isupper():
    print(s.lower())
elif len(s) == 1:
    print(s.upper())
else:
    print(s)