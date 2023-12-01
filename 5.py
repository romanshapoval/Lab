class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + 'company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)


employee = Employee('Teddy', 'Bear', 5000)
employee_s = Employee('Taylor', 'Twitch', 150)

print(employee)
print(employee_s)

# Classes
print('Name First employee -' + employee.first)
print('Surname Second Employee - ' + employee_s.last)
print('Full Info - ' + employee.first + ' ' + employee.last + ' ' + employee.email)

# Methods
print(employee.fullname())
print(Employee.fullname(employee))
print(employee.fullname())