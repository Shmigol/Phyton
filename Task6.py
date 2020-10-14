with open("text_6.txt", "r", encoding="utf-8") as lessons:
    c = lessons.readline()
    ind = []
    kek = []
    vspom = ""
    e = 0
    while c:
        d = c.split()
        # print(d)
        for el in d:
            for m in el:
                if 48 <= ord(m) <= 57:
                    vspom += m
            try:
                e += float(vspom)
            except:
                ValueError
                continue
            vspom = ""
        
        ind.append(e)
        kek.append((d[0].replace(":", "")))
        e = 0
        c = lessons.readline()
    # print(ind)
    # print(kek)
    for i in range(len(kek)):
        print(res :={kek[i]: ind[i]})





