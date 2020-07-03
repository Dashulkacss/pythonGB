index = 1

tovari = {"название": "", "цена": "", "количество": "", "единицы": ""}
analytics_dict = {"название": [], "цена": [], "количество": [], "единицы": []}

while True:
    if input("Для выхода из программы нажмите Q. Для продолжения энтер").upper() == "Q":
        break

    index += 1
    productName = input("Название товара: ")
    analytics_dict["название"].add(productName)
    cost = input("Цена: ")
    analytics_dict["цена"].add(cost)
    count = input("Количество: ")
    analytics_dict["количество"].add(count)
    parm = input("единицы: ")
    analytics_dict["единицы"].add(parm)
    tovari.append(tuple((index, dict({"название": productName, "цена": cost, "Количество": count, "единицы": parm}))))

print("Смотри какие данные мы собрали:")
i = 0
while i < len(tovari):
    print(tovari[i])
    i += 1
    index = 1
