n = int(input())
dcount = list(map(int, input().strip().split()))
# самое короткое решение
#print(sum(dcount) - max(dcount))


def findmax(seq):
    ans = 0 # переменная - индекс
    for i in range (1, len(seq)):
        if seq[i] > seq[ans]:
            ans = i
    return seq[ans]

maxd = findmax(dcount)
seqsum = 0
#print(maxd)
for i in range(len(dcount)):
        seqsum += dcount[i]
print(seqsum - maxd)