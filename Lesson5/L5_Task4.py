from googletrans import Translator
translator = Translator()

try:
    with open("text_4.txt", "r", encoding="utf-8") as file:
        fileTxt = file.readlines()
        print(fileTxt)
        with open("translate_text4.txt","w", encoding="utf-8") as newFile:
            for str in fileTxt:
                transLine = translator.translate(str, src='en', dest='ru')
                newFile.writelines(transLine.text + "\n")

except IOError:
    print("Error!")