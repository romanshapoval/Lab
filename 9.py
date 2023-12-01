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

    def __repr__(self):
        return "Employee('{}', {}, {})".format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())


employee = Employee('Teddy', 'Bear', 5000)
employee_second = Employee('Alex', 'Snow', 1212)
# Printing REPR and STR Methods
print(repr(employee))
print(str(employee))
#  Add
print(f'Sum: {employee.pay} + {employee_second.pay} = ', employee + employee_second)
# Len
print(len(employee))


