d = list(map(int, input().split()))
right = [0] * len(d)
left = [0] * len(d)
right = [0] * len(d)
shoppos = -20
for i in range(len(d)):
    if d[i] == 2:
        shoppos = i
    if d[i] == 1:
        left[i] = i - shoppos
#print(left)
ans = 0
shoppos = 30
for i in range(len(d) - 1, -1, -1):
    if d[i] == 2:
        shoppos = i
    if d[i] == 1:
        right[i] = shoppos - i
        mindist = min(shoppos - i, left[i])
        ans = max(ans, mindist)
print(ans)





