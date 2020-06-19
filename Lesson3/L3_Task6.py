
def int_func(text):
    return text.title()


def isCorrect(text):
    """Проверяем на корректный ввод"""
    global correctFlag
    i = 0
    while len(text) > i:
        if ord(text[i]) in range(97, 122):
            i += 1
        else:
            return False

    return True


def lotOfText(lotText):
    """Внутри проводим расследование на корректный ввод
    Если что то не так - выходим из программы. Если все ок - делаем общую строку и подсовываем в int_func"""
    finalStr = ""
    i = 0
    while i < (len(lotText)):
        if not isCorrect(lotText[i]):
            return print("Ай яй. Я же просил маленькие латинские буквы...")
            sys.exit
        else:
            finalStr += (lotText[i] + " ")
            i += 1
    print(int_func(finalStr))


lotOfText(input("Введите латинские маленькие буквы ").split())
