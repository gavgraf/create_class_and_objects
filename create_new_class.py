class Employee:
    vacation_days = 28
    # first_name = ''
    # second_name = ''
    # gender = ''

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

# developer = Employee(dial_type_value='разработчик')
print(f'Имя: {employee1.first_name}, Фамилия: {employee1.second_name}, Пол: {employee1.gender}, Отпускных дней в году: {employee1.vacation_days}.')
print(f'Имя: {employee2.first_name}, Фамилия: {employee2.second_name}, Пол: {employee2.gender}, Отпускных дней в году: {employee2.vacation_days}.')
