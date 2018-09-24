class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    #__str__方法只在print的时候触发
    def __str__(self):
        return ",".join(self.employee)

    #__repr__方法在直接输出对象和print的时候触发，适合开发模式
    def __repr__(self):
        return ",,cd".join(self.employee)

company = Company(["tom", "bob", "jane"])
print(company)
# >>> company