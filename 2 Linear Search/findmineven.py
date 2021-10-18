# Дана последовательность чисел длинй N
# Найти минимальное четное число в последовательности или вывести -1, если такого числа не существует

seq = list(map(int, input().split()))

# def findmineven(seq):
#     ans = -1
#     for i in range(len(seq)):
#         if seq[i] % 2 == 0 and (ans == -1 or seq[i] < ans): #либо четное число первое в послед или меньше чем было раньше
#             ans = seq[i]
#     return ans
# универсальный способ, если нам нужно найти минимальное нечетное число
def findmineven(seq):
    flag = False
    ans = -1
    for i in range(len(seq)):
        if seq[i] % 2 == 0 and (not flag or seq[i] < ans):
            ans = seq[i]
            flag = True
    return ans


print(findmineven(seq))

# 1 4 3 2
#