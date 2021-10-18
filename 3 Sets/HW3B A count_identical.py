# Даны два списка чисел, которые могут содержать до 100 000 чисел каждый.
# Посчитайте, сколько чисел содержится одновременно как в первом списке, так и во втором.

#a1 = list(map(int, input().strip().split()))
#a2 = list(map(int, input().strip().split()))

#print(a1, a2)

#print(len(set(input().split()) & set(input().split())))
# пересечение двух множеств
print(len(set(input().split()) & set(input().split())))