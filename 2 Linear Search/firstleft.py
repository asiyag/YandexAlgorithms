# дана последовательность чисел длиной N. Найти первое (левое) вхождение положительного числа X или вывести -1,
# если число X не встретилось.

seq = list(map(int, input().split()))
x = 2
def findx(seq, x):
    ans = -1
    for i in range(len(seq)):
        if ans == -1 and seq[i] == x: # убеждаемся что мы нашли самое левое решение доп условием
            ans = i #если наше вхождение первое, перезаписываем ans и выходим из цикла
    return ans

print(findx(seq, x))