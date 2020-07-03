with open("forhwtask1.txt", "w", encoding="utf-8") as lolly:

    print("Введите строки. Когда надоест - жми q")
    while True:
        quitProg = input()
        if quitProg == "q":
            break
        lolly.write(quitProg)
        lolly.write("\n")
