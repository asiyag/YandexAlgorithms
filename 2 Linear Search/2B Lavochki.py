l, k = list(map(int, input().split()))
pos = list(map(int, input().strip().split()))
ans = 0
flag = -1
mid = l // 2
for i in range(k):
    if flag == -1 and pos[i] >= mid:
        flag = i        #запомним позиция самого большего блока после середины
        if l % 2 == 0:  # точно будет два блока
            ans = f'{pos[flag - 1]} {pos[flag]}'
            print(ans)
        else:  # если нечетное кол-во. то может быть один = середине
            if (pos[flag] >= mid and pos[flag] < mid + 1):
                print(pos[flag])
            else:  # два, если нет блока совпадающего с серединой
                ans = f'{pos[flag - 1]} {pos[flag]}'
                print(ans)