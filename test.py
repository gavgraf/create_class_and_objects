class Phone:
    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value

    def ring(self):
        print('Дзззззыыыыыыыынь')

    def call(self, phone_number):
        # Сначала в вывод подставляется значение параметра phone_number,
        # а затем - атрибута класса Phone.
        print(f'Звоню по номеру {phone_number}! Тип связи - {self.line_type}.')

    def get_missed_calls(self):
        print('Запрос количества пропущенных вызовов')


rotary_phone = Phone(dial_type_value='дисковый')
rotary_phone.call('555-2368')
# Вызов метода call(). Передаётся аргумент '555-2368'
# для параметра phone_number.
print(f'Тип набора: {rotary_phone.dial_type}.')
rotary_phone.ring()
rotary_phone.get_missed_calls()
