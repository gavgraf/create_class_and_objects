class Phone:
    line_type = 'проводной'

    def __init__(self, dial_type_value):
        self.dial_type = dial_type_value


rotary_phone = Phone(dial_type_value='дисковый')
print(f'Тип набора: {rotary_phone.dial_type}.')
