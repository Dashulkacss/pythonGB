sumSalary = 0
try:
    with open("text_3.txt", "r", encoding="utf-8") as lolly:
        associates = lolly.readlines()
        print(f"ЗП меньше 20 000 :")
        for data in associates:
            line = data.split()
            if float(line[1]) < 20000:
                print(line[0])
            sumSalary += float(line[1])
        print(f"Cредняя величина дохода сотрудников = {sumSalary/len(associates)}")
except IOError:
    print("Error!")

    """Полезные идеи после домашки"""

# line = lolly.read().split("\n")
