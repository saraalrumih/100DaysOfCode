txt=" Please, I want {} sandwishes and {} donutes "
txt=txt.replace("I","we")
txt=txt.format(5,7)
txt=txt.replace("a","a".upper())
print(txt)