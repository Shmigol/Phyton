
with open("Text_1.txt",  encoding="utf-8") as content:
    print(c := content.readlines())
    d = 0
    for i in range(len(c)):
        d += 1
        e = 0
        numb_wrds = c[i].split()
        e = len(numb_wrds)
        print(f"В cтроке {d} {e} слов")
    print(f"В файле {d} строк")






