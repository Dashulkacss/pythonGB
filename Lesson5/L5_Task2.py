i = 1
try:
    with open("forhwtask1.txt", "r", encoding="utf-8") as lolly:
        line = lolly.readlines()
        print(f"в нашем файле {len(line)} строк")
        for str in line:
            print(f"в строке {i} слов {len(str.split())} ")
            i +=1


except IOError:
    print("Error!")
