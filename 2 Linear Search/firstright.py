# дана последовательность длиной N. Найти последнее (правое) вхождение числа X или вывести -1, если число X не встретилось.
seq = list(map(int, input().split()))
x = 2
def findrightx(seq, x):
    ans = -1
    for i in range(len(seq)):
        if seq[i] == x: # убеждаемся что мы нашли самое левое решение доп условием
            ans = i # дойдем до конца последовательности и найдем последнее, перезаписываем ans и выходим из цикла
    return ans

print(findrightx(seq, x))