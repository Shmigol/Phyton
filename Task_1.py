
with open("Text_1.txt", "w", encoding="utf-8") as content:
    d = input("Enter something. If ypu want to stop leave empty string ")
    while d:
        content.writelines(d + '\n')
        d = input("Enter something. If ypu want to stop leave empty string ")





