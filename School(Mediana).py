# нахождение медианы
n = int(input())
# координаты домов - списком, в возрастающем порядке
houses = list(map(int, input().split()))
print(houses[n // 2])

# n = int(input())
# s = list(map(int, input().split()))
# if n == 0:
#     print(0)
# if n % 2 == 0:
#     print(s[n // 2])
# if n % 2 != 0:
#     print(s[(n - 1) // 2])
