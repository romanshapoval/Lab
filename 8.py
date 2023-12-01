class Employee:
    raise_amount = 2.55
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    def __init__(self, first, last, pay, language):
        super().__init__(first, last, pay)
        self.language = language


class Manager(Employee):
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, employ):
        if employ not in self.employees:
            self.employees.append(employ)

    def remove_employee(self, employ):
        if employ in self.employees:
            self.employees.remove(employ)

    def print_employee(self):
        for employ in self.employees:
            print('Workers: ', employ.fullname())


employee = Employee('Teddy', 'Bear', 5000)
developer = Developer('Alex', 'Snow', 1212, 'Python')
developer_Second = Developer('Olivier', 'Meek', 1212, 'C++')
manager_First = Manager('Alisa', 'Samon', 12443, [developer])


# Add developer
manager_First.add_employee(developer_Second)
# remove develop
manager_First.remove_employee(developer)
# print Data
manager_First.print_employee()

print(isinstance(manager_First, Employee))
print(issubclass(Developer, Employee))
