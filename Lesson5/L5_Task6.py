import re
dictSch = {}

with open("text_6.txt", "r", encoding="utf-8") as file:
    data = file.readlines()

    for stri in data:
        sumSub = 0
        line = list(stri.split(" "))
        for el in line:
            if any(map(str.isdigit, el)):
                sumSub += int(re.sub(r'\([^()]*\)','',el))
        dictSch.update({line[0][0:-1]: sumSub})
    print(dictSch)


        #
        # dictSch = dict(list[0], "")