seq = list(map(int, input().split()))
# переменная, в которую мы запишем максимум
if len(seq) == 0:
    print('-inf')
else:
    seqmax = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > seqmax:
            seqmax = seq[i]
print(seqmax)