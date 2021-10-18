# Найти max число в последовательности длиной N.

seq = list(map(int, input().split()))

# def findmax(seq):
#     ans = seq[0] # переменная
#     for i in range(1, len(seq)):
#         if seq[i] > ans:
#             ans = seq[i]
#     return ans
#
# print(findmax(seq))


def findmax(seq):
    ans = 0 # переменная - индекс
    for i in range (1, len(seq)):
        if seq[i] > seq[ans]:
            ans = i
    return seq[ans]

print(findmax(seq))
