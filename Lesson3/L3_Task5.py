result = 0
EndOfProgram = False;
iterations = 0;


def my_sum(*args):
    """Анализирует строку на сумму

    Берет список который мы ввели и проходится по нему.
    Попутно проверяет каждый символ на окончание работы программы.
    Если все ок, то суммирует в глобальной переменной result"""
    global result, EndOfProgram, iterations
    i = 0
    while i != (len(args[0])):

        if if_end(args[0][i]):
            result += int(args[0][i])
            i += 1
        else:
            EndOfProgram = True
            break
    print(result)


def if_end(a):
    """ Функция определяет является ли введеный символ спецсимволом"""
    if ord(a) in ((range(33, 47)) or (range(58 - 64)) or (range(91 - 96)) or (range(123 - 126))):
        return False
    else:
        return True


while not EndOfProgram:
    my_sum(input("введи числа через пробел ").split())

# my_sum(list(map(int, input("введи числа через пробел ").split())))
