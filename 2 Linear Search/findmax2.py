# Дана последовательность чисел длиной N. Найти макс число в последовательности и второе по величие число.
# Такое, которое мы будем называть максимальным, если вычеркнуть из последовательности первого максимума.


seq = list(map(int, input().split()))

def findmax2(seq):
    max1 = max(seq[0], seq[1])
    max2 = min(seq[0], seq[1])
    for i in range (2, len(seq)):
        if seq[i] > max1:
            max2 = max1
            max1 = seq[i]
        elif seq[i] > max2:
            max2 = seq[i]
    return(max1, max2)

print(findmax2(seq))
