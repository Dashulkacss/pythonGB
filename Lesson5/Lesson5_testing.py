"""w - write
r - read
x - if exist -> nothing, else write
a - дозапись"""

"""seek - установи курсор 0 - начало. 1- сейчас 2- конец"""
"""tell - скажи где курсор """
""""r - чтобы всякие большие/маленькие буквы не мешали"""
# lolly = open(r"text.txt", "r", encoding="utf-8")

# lolly = open("text1.txt", "w", encoding="utf-8")
"""Read content"""
# content = lolly.readlines()
# print(content)

"""Read content"""
# for i in lolly:
#    print(i, end="")

"""Открыть, записать , закрыть"""
# lolly = open("text1.txt", "w", encoding="utf-8")
# lolly.write("76 df asd\nbla bla")
# lolly.close()


# lolly = open("text1.txt", "r", encoding="utf-8")
# print(lolly.read())
# lolly.close()

"""Правильный обработчик"""
# try:
#     with open("text2.txt", "a+", encoding="utf-8") as lolly:
#         print(lolly.read())
#         lolly.write("\nP")
# except IOError:
#     print("Error!")
# else:
#     print("Ok")

# print(lolly.name)
# print(lolly.mode)
# print(lolly.closed)
"""seek & tell"""
# try:
#     with open("text2.txt", "a+", encoding="utf-8") as lolly:
#         lolly.write("\nPythin")
#         lolly.seek(0)
#         print(lolly.read(7))
#         # print(lolly.tell())
#         # print(lolly.read())
#
# except IOError:
#     print("Error!")
# else:
#     print("Ok")

""""Print in file"""
# with open("text2.txt", "a", encoding="utf-8") as lolly:
#     print("\nha ha ha i can do it from print!!!", file=lolly)

"""модуль os"""

# os.remove("text.txt")
# os.rename("text1.txt", "newOne.txt")
# print(os.listdir())

import json

"""JSON"""

# data = {
#     "income": {
#         "salary": 50000,
#         "bonus": 20000
#     }
# }

# with open("my_file.json", "w", encoding="utf-8") as jolly:
#     json.dump(data, jolly)

# json_str = json.dumps(data)
# print(type(json_str))

with open("my_file.json", "r", encoding="utf-8") as jolly:
    data = json.load(jolly)

print(data)
print(type(data))

json_str = """{"income": {"salary": 50000, "bonus":20000}}"""
print()
print(type(json_str))
dataJson = json.loads(json_str)
print(dataJson)
print(type(dataJson))



try:
    with open("text_3.txt", "r", encoding="utf-8") as lolly:
        print(lolly.read())
except IOError:
    print("Error!")