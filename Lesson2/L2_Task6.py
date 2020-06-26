index = 1


productName = input("Название товара: ")
cost = input("Цена: ")
count = input("Количество: ")
parm = input("единицы: ")
analytics_dict = {"название": set([productName]), "цена": set([cost]), "количество": set([count]),
                  "единицы": set([parm])}
tovari = [tuple((index, analytics_dict))]
again = bool(input("Если нужно еще напиши. Если нужно останивиться - жми энтер"))
if again:
    while again:
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
        again = bool(input("Если нужно еще напиши. Если нужно останивиться - жми энтер"))

print("Смотри какие данные мы собрали:")
i=0
while i < len(tovari):
    print(tovari[i])
    i+=1

print()
print("Смотри, какую аналитику мы собрали: ")
print(analytics_dict)


