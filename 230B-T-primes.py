limit = 1000000

def is_prime():
    prime_flag = [True] * limit
    prime_flag[0] = prime_flag[1] = False

    for i in range(2,limit):
        if prime_flag[i] == True:
            for j in range(i*i,limit,i):
                prime_flag[j] = False
    return prime_flag

def is_t_prime(n):
    if n == 4:
        return True
    if n < 4 or n % 2 == 0:
        return False
    sqrt_n = n**0.5
    if sqrt_n == int(sqrt_n):
        if prime_flag[int(sqrt_n)] == True:
            return True
    return False

prime_flag = is_prime()
n = int(input())
l = list(map(int,input().split()))
for i in l:
    if is_t_prime(i) == True:
        print('YES')
    else:
        print('NO')




