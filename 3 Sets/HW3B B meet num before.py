# Во входной строке записана последовательность чисел через пробел.
# Для каждого числа выведите слово YES (в отдельной строке),
# если это число ранее встречалось в последовательности или NO, если не встречалось.

#numbers = [int(s) for s in input().split()]
a = list(map(int, input().split()))
b = set() #пустое множество
for num in a:
    if num in b:
        print("YES")
    else:
        print("NO")
        b.add(num)