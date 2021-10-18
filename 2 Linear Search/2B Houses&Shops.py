d = list(map(int, input().split()))
left = [0] * len(d)
shoppos = -20
for i in range(len(d)):
    if d[i] == 2:
        shoppos = i # запоминаем позицию магазина
    if d[i] == 1:
        left[i] = i - shoppos # записываем в список расст от дома до ближ магазина слева
ans = 0
shoppos = 30
for i in range(len(d) - 1, -1, -1): # обратный отсчет
    if d[i] == 2:
        shoppos = i
    if d[i] == 1:
        mindist = min(shoppos - i, left[i]) # выбираем минимальное расстояние
        ans = max(ans, mindist)
print(ans)