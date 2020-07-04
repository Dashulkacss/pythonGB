with open("forhwtask1.txt", "w", encoding="utf-8") as lolly:
    print("Введите строки. Когда надоест - оставь строку пустой")
    while True:
        quitProg = input()
        if quitProg == "":
            break
        lolly.write(quitProg + '\n')
    # lolly.write("\n")
