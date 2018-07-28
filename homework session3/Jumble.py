wordlist = ("communism", "capitalism", "forest chimpanzee", "red bull", "annamite")

from random import randint, choice
word = choice(wordlist)
res = [""]
sap = [""]
pos = 0
l = len(word)
for i in range (l):
    sap.append(word[i])
sap.pop(0)
while l > 0:
    pos = randint(1,l)
    res.append(sap[pos-1])
    del sap[pos-1]
    l = len(sap)
print(*res)
ans = input("Your answer: ")
if ans == word:
    print("hura")
else: print("idiot")