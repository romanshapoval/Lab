import datetime

class Employee:
    raise_amount = 2.55
    num_of_employees = 0

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'company.com'

        Employee.num_of_employees += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, employee_sting):
        first, last, pay = employee_sting.split('-')
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


employee = Employee('Teddy', 'Bear', 5000)
employee_s = Employee('Taylor', 'Twitch', 150)

# classMethod
employee_Data = 'Jon-Deer-123456'
new_employee_data = Employee.from_string(employee_Data)
print(new_employee_data.email)
print(new_employee_data.pay)

# staticMethod

my_date = datetime.date(2015, 5, 12)
print(Employee.is_workday(my_date))