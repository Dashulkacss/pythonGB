from datetime import datetime


class Data:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def line_to_number(cls, line):

        if cls.validation_of_number(line[:2],"day"):
            day = int(line[:2])
        else:
            print("Wrong date")
            exit(0)

        if cls.validation_of_number(line[3:5],"month"):
            month = int(line[3:5])
        else:
            print("Wrong date")
            exit(0)

        if cls.validation_of_number(line[-4:],"year"):
            year = int(line[-4:])
        else:
            print("Wrong date")
            exit(0)

        return cls(day, month, year)

    @staticmethod
    def validation_of_number(num, spec):
        """валидация номера на корректность"""
        if spec == "day":
            if not 0 < int(num) < 32:
                return False

        if spec == "month":
            if not 0 < int(num) < 13:
                return False

        if spec == "year":
            if not 0 < int(num):
                return False
        return True

    def __str__(self):
        return f"{self.day} {self.month} {self.year}"


date1 = Data.line_to_number("01-11-1995")
print(date1)
