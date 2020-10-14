with open("Text_2.txt", "w", encoding="utf-8") as sum_num:
    sum_num.writelines(input("Введите строку из чисел, разделённых пробелами "))

with open("Text_2.txt", "r", encoding="utf-8") as sum_num:
    sum_num.seek(0)
    d = sum_num.read().split()
    c = 0
    for el in d:
        try:
            c += float(el)
        except:
            ValueError
            c = "Вы ввели не последовательность чисел"
            break
    print(c)










