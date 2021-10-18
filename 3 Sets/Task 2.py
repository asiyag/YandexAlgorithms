# Дан словарь из N слов, длина каждого не превосходит K
# В записи каждого из M слов текста (каждое длиной до K)
# может быть пропущена одна буква. Для каждого слова сказать, входит ли оно (возможно с одной пропущенной буквой)
# в словарь

 def wordsindict(dictionary, text):
     goodwords = set(dictionary) # создаем словарь из множества слов в словаре
     for word in dictionary:     # для каждого слова из словаря
         for delpos in range(len(word)):  #
             # срезы, добавляем в словарь
             goodwords.add(word[:delpos] + word[delpos + 1:])
     ans = []
     for word in text:
         ans.append(word in goodwords) # True/False скажем если слово в словаре
     return ans
