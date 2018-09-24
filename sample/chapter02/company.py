class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    # 调用__getitem__方法就变成可迭代对象，item是下标
    def __getitem__(self, item):
        return self.employee[item]

    def __len__(self):
        return len(self.employee)

company = Company(["tom", "bob", "jane"])
for em in company:
    print(em)

company1 = company[:2]

print(len(company))