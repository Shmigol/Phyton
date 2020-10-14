with open("Text_1.txt", "r",  encoding="utf-8") as salary:
    print(salary.read())
    salary.seek(0)
    c = salary.readline()
    # add_list = []
    d = 0
    e = 0
    while c:
        new_list = c.split()
        for i in range(len(new_list)):
            try:
                float(new_list[i])
                # add_list.append(float(new_list[i]))
                d += float(new_list[i])
                e += 1
                if float(new_list[i]) > 20000:
                    print(f"Зарплата сотрудника по фамилии {new_list[i - 1]} больше 20000 баксов")
                else:
                    print(f"Зарплата сотрудника по фамилии {new_list[i - 1]} меньше 20000 баксов")
            except:
                ValueError
                continue
        c = salary.readline()

    # print(add_list)
    print(f"Средняя зарплата на предприятии равна {d / e}")