class MushroomsCollector:
    def __init__(self):
        self.mushrooms = []

    def is_poisonous(self, mushroom_name):
        if mushroom_name in ('Мухомор', 'Поганка'):
            print('Нельзя добавить ядовитый гриб')
            return True
        return False

    def add_mushroom(self, mushrooms_name):
        if not self.is_poisonous(mushrooms_name):
            self.mushrooms.append(mushrooms_name)

    def __str__(self):
        return ", ".join(self.mushrooms)


collector_1 = MushroomsCollector()
collector_1.add_mushroom('Мухомор')
collector_1.add_mushroom('Подосиновик')
collector_1.add_mushroom('Белый')
print(collector_1)

collector_2 = MushroomsCollector()
collector_2.add_mushroom('Лисичка')
print(collector_1.__str__())
print(collector_2.__str__())
