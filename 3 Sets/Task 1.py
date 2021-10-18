# Дана последовательность положительных чисел длиной N и число X
# найти два различных числа А и В из последовательности, таких что
# А + В = Х или вернуть пару 0, 0 если такой пары чисел нет
# Решение за О(N^2) Переберем число А за О(N) и переберем число В за О(N)
# Если из сумма равна Х, то вернем эту пару.
def twotermswithsumx(nums, x):
    for a in nums:
        for b in nums:
            if a + b == x: # два различных числа!
                return a, b
    return 0, 0

# перебираем не числа, а индексы
def twotermswithsumx(nums, x):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)): #перебираем от индекса на единицу больше
            if nums[i] + nums[j] == x: # два различных числа!
                return nums[i], nums[j]
    return 0, 0

# решение за O(N)
# Будем хранить все уже обработанные числа в множестве
# Если очередное nownum, a X - nownum есть в множестве,
# то мы нашли слагаемые
def twotermswithsumx(nums, x):
    prevnums = set() #пустое множество
    for nownum in nums: #идем по последовательности
        if x - nownum in prevnums: #если лежит во множестве, то возвращаем
            return nownum, x - nownum
        prevnums.add(nownum) #добавляем числа во множество
        return 0, 0