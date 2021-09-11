# def slow(seq):
#     for start in range(len(seq)):
#         i = start
#         j = len(seq) - 1
#         while i < (len(seq) // 2) and j >= (len(seq) // 2) and seq[i] == seq[j] and i <= j:
#             i += 1
#             j -= 1
#         if i > j:
#             ans = []
#             for i in range(start - 1, -1, -1):
#                 ans.append(seq[i])
#             return ans


# seq = input()
# ans = slow(seq)
# k = slow(seq)
# print(len(k))
# print(len(seq))
# print(*ans)
# print(len(ans))

# def slow(seq):
#     for start in range(len(seq)):
#         i = start
#         j = len(seq) - 1
#         while i < (len(seq) // 2) and j >= (len(seq) // 2) and seq[i] == seq[j] and i <= j:
#             i += 1
#             j -= 1
#         if i > j:
#             ans = []
#             for i in range(start - 1, -1, -1):
#                 ans.append(seq[i])
#             return ans





seq = input()
for start in range(len(seq) // 2):
    i = start
    j = len(seq) - 1
    while i < (len(seq) // 2) and j >= (len(seq) // 2) and i <= j and seq[i] == seq[j]:
        i += 1
        j -= 1
    if i > j:
        ans = []
        for i in range(start - 1, -1, -1):
            ans.append(seq[i])
        print(len(ans))

# i = 0
# j = 4
# while i < int((len(seq) // 2)) and j >= (len(seq) // 2) and i <= j and seq[i] == seq[j]:
#     i += 1
#     j -= 1