from sys import argv


def payments(a, b, c):
    return (int(a) * int(b)) + int(c)


script_name, hoursTotal, moneyInHour, reward = argv

print("Name script: ", script_name)
print("Выроботка в часах: ", hoursTotal)
print("Ставка в час: ", moneyInHour)
print("Премия: ", reward)

try:
    print("Расчет заработной платы:: ", payments(hoursTotal, moneyInHour, reward))
except ValueError:
    print("А можно цифрами?")
