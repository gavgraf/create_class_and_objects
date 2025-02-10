class Employee:
    vacation_days = 28

    def __init__(self,
                 first_name_value,
                 second_name_value,
                 gender_value
                 ):

        self.first_name = first_name_value
        self.second_name = second_name_value
        self.gender = gender_value


employee1 = Employee(
    first_name_value='Роберт',
    second_name_value='Крузо',
    gender_value='м'
    )

employee2 = Employee(
    first_name_value='Роберт',
    second_name_value='Крузо',
    gender_value='м'
    )

print(
    f'Имя: {employee1.first_name}, '
    f'Фамилия: {employee1.second_name}, '
    f'Пол: {employee1.gender}, '
    f'Отпускных дней в году: {employee1.vacation_days}.'
)

print(
    f'Имя: {employee2.first_name}, '
    f'Фамилия: {employee2.second_name}, '
    f'Пол: {employee2.gender}, '
    f'Отпускных дней в году: {employee2.vacation_days}.'
)
