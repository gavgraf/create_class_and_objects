class Employee:
    vacation_days = 28

    def __init__(self, first_name_value, second_name_value, gender_value):
        self.first_name = first_name_value
        self.second_name = second_name_value
        self.gender = gender_value
        self.remaining_vacation_days = self.vacation_days

    def consume_vacation(self, consume_value):
        self.remaining_vacation_days = self.remaining_vacation_days - consume_value

    def get_vacation_details(self):
        return f'Остаток отпускных дней: {self.remaining_vacation_days}.'


employee = Employee('Роберт', 'Крузо', 'м')
employee.consume_vacation(7)

print(
    f'Имя: {employee.first_name}, \
    Фамилия: {employee.second_name}, \
    Пол: {employee.gender}, \
    Отпускных дней в году: {employee.vacation_days}.'
)
print(employee.get_vacation_details())
