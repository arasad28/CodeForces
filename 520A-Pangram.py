import string

def ispangram(str):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for char in alphabet:
        if char not in str.lower():
            return False
    return True
n = int(input())
string = str(input())
if (ispangram(string) == True):
    print('YES')
else:
    print('NO')


