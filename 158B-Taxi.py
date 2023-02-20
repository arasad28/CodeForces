n = int(input())
s = list(map(int,input().split()))

cnt1,cnt2,cnt3,cnt4 = s.count(1),s.count(2),s.count(3),s.count(4)

ans = cnt4

ans += cnt2//2

rcnt2 = cnt2 % 2
rcnt1 = 0

if cnt3:
    if cnt3 >= cnt1:
        ans += cnt3
        cnt1 = 0
    else:
        ans += cnt3
        rcnt1 = cnt1 - cnt3

if cnt1 and rcnt1 == 0:
   if cnt1 % 4 == 0:
        ans += cnt1//4
   elif cnt1 % 4 == 3:
        ans += cnt1//4 + 1
   else:
       rcnt1 += cnt1
       
       
if rcnt1>2:   
   if rcnt1 % 4 == 0:
        ans += rcnt1//4
        rcnt1 =0
   elif rcnt1 % 4 == 3:
        ans += rcnt1//4 + 1
        rcnt1 = 0
   else:
       ans += rcnt1//4
       rcnt1 = rcnt1 % 4

if rcnt2>0 or rcnt1>0:
    ans += 1
print(ans)

#https://codeforces.com/problemset/problem/158/B
#B. Taxi
