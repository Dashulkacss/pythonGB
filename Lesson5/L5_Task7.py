import json
average_sum = 0
average_count = 0
dictFirm = {}
try:
    with open("text_7.txt", "r", encoding="utf-8") as file:
        data = file.readlines()
        for dataline in data:
            datalist = list(dataline.split(" "))
            profit = int(datalist[2]) - int(datalist[3])
            if profit > 0:
                average_sum += profit
                average_count += 1
            dictFirm.update({datalist[0]: profit})

except IOError:
    print("Error!")

finalList = [dictFirm, {"average_profit": average_sum / average_count}]

with open("text_7.json", "w", encoding="utf-8") as f:
    json.dump(finalList, f, sort_keys=False, indent=4, ensure_ascii=False, separators=(',', ': '))