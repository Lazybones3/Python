class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return "{year}/{month}/{day}".format(year=self.year,month=self.month,day=self.day)

class User:
    def __init__(self, birthday):
        self.__birthday = birthday

    def get_age(self):
        return 2018 - self.__birthday.year


if __name__ == "__main__":
    user = User(Date(1990,2,1))
    # 访问私有属性的方法_Classname__attr
    print(user._User__birthday)
    print(user.get_age())