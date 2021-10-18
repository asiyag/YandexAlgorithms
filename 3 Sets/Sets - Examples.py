# создаем (мульти)собственное множество
setsize = 10
myset = [[] for _ in range(setsize)] #создание двумерного списка в питоне: список списков

def add(x):
    # if not find(x):   # проверяем нет ли уже этого элемента в списке
    myset[x % setsize].append(x) # считаем остаток от деления и добавляем в список

def find(x):  #линейный поиск
    for now in myset[x % setsize]:
        if now == x:      #если нашли линейным поиском, то возвращаем True
            return True
    return False          # а если нет, то возвращаем False

def delete(x):
    xlist = myset[x % setsize]  #определяем номер списка
    for i in range(len(xlist)): #линейным поиском ищем список
        if xlist[i] = x:
            xlist[i], xlist[len(xlist) - 1] = xlist[len(xlist) - 1], xlist[i] #обмениваем элементы
            xlist.pop() # a, b = b, a (swap(a, b)) удаляем последний элемент (дублирующий элемент)
            return
        # xlist[i] = xlist[len(xlist) - 1]  # присваем последний элемент тому элементу, который ъотим удалить
