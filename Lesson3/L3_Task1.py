def delimited(a, b):
    try:
        print(f"Delimited = {round(a / b, 2)}")
    except ZeroDivisionError:
        print("Ай яй яй. На 0 делить нельзя!")


delimited(int(input("Hey что будем делить? ")), int(input("На что? ")))
