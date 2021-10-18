# код заверщения
r = int(input())
# вердикт интерактора
i = int(input())
# вердикт чекера
c = int(input())
if i == 0:
    if r == 0:
        print(c)
    else:
        print(3)
if i == 1:
    print(c)
if i == 4:
    if r == 0:
        print(4)
    else:
        print(3)
if i == 6:
    print(0)
if i == 7:
    print(1)
if i in (2, 3, 5):
    print(i)



N, i, j = map(int, input().split())
p = 0
p = abs(i-j)
if p <= N // 2:
    p -= 1
else:
    p = N - p - 1
print(p)


x, y, z = map(int, input().split())
p = 0
if (x == y):
    p = 1
else:
    if (1 <= x <= 12) and (1 <= y <= 12):
        p = 0
    else:
        p = 1
print(p)

n = int(input())
s = list(map(int, input().split()))
if n == 0:
    print(0)
if n % 2 == 0:
    print(s[n // 2])
if n % 2 != 0:
    print(s[(n - 1) // 2])

d = int(input())
s = list(map(int, input().split()))
s1 = 0
s2 = 0
s3 = 0
k = 0
if (0 <= s[0] <= d) and (0 <= s[1] <= d):
    print(0)
else:
    s1 = (s[0] ** 2 + s[1] ** 2) ** (1 / 2)
    s2 = ((s[0] - d) ** 2 + s[1] ** 2) ** (1 / 2)
    s3 = (s[0] ** 2 + (s[1] - d) ** 2) ** (1 / 2)
    k = min(s1, s2, s3)
    print(k)
    if k == s1:
        print(1)
    elif k == s2:
        print(2)
    elif k == s3:
        print(3)

s = -1
smax = 0
snum = 0
while s != 0:
    s = int(input())
    if s > smax:
        smax = s
        snum = 1
    elif s == smax:
        snum += 1
print(snum)

s = list(map(int, input().split()))
d = 0
for i in range(len(s)):
    for j in range(len(s)):
        if s[i] == 1 and s[j] == 2:
            d = abs(i - j)
            print(d)

s = input()
if len(s) % 2 == 0:
    print(len(s) // 2)
else:
    print(len(s) // 2)

d = int(input())
x, y = map(int, input().split())
if (x >= 0) and (y >= 0) and (x + y <= d):
    print(0)
elif (y <= x) and (y > d - x):
    print(2)
elif (y > x):
    print(3)
elif (y <= 0.5):
    print(1)
elif (y > 0.5):
    print(3)
elif (x <= 0.5):
    print(1)
elif (x > 0.5):
    print(2)

s = list(map(int, input().split()))
d = 0
dmin = 10
for i in range(len(s)):
    for j in range(len(s)):
        if s[i] == 1 and s[j] == 2:
            d = abs(i - j)
            if d < dmin:
                dmin = d
    print(dmin)

def slow(seq):
    for start in range(len(seq)):
        i = start
        j = len(seq) - 1
        k = int(len(seq))
        while i < len(seq) and j >=0 and seq[i] == seq[j] and i <= j and i <= 2:
            i += 1
            j -= 1
        if i > j:
            ans = []
            for i in range(start - 1, -1, -1):
                ans.append(seq[i])
            return ans, k

seq = input()
for start in range(len(seq) // 2):
    i = start
    j = len(seq) - 1
    while i < (len(seq) // 2) and j >= (len(seq) // 2) and i <= j and seq[i] == seq[j]:
        i += 1
        j -= 1
    if i > j:
        ans = []
        for i in range(start - 1, -1, -1):
            ans.append(seq[i])
print(len(ans))

# for i in range(k):
#     if ans == -1 and pos[i] >= mid:
#         ans = pos[i]
#         if (ans >= mid and ans <= mid):
#             print(ans)
#         else:
#             ans = f'{pos[i - 1]} {pos[i]}'
#             print(ans)


if l % 2 == 0:  # точно будет два блока
    ans = f'{pos[i - 1]} {pos[i]}'
    print(ans)
else:  # если нечетное кол-во. то может быть один = середине
    if (pos[i] >= mid and pos[i] < mid + 1):
        print(pos[i])
    else:  # два, если нет блока совпадающего с серединой
        ans = f'{pos[i - 1]} {pos[i]}'
        print(ans)

