class Animal:
    def __init__(self, name, weight, sound):
        self.name = name
        self.weight = weight
        self.sound = sound

    def feed(self):
        print(f"{self.name} покормлено.")

    def make_sound(self):
        print(f"{self.name} {self.sound}")

    def is_milking(self):
        return self.sound in ['мычит', 'мекает']

    def is_shearing(self):
        return self.sound == 'блеет'

    def is_collect_eggs(self):
        return self.sound in ['крякает', 'кукарекает', 'гогочет']


# Создаем каждое животное как отдельный объект
animals = [
    Animal('Серый', 5, 'гогочет'),  # гусь
    Animal('Белый', 6, 'гогочет'),  # гусь
    Animal('Манька', 400, 'мычит'),  # корова
    Animal('Барашек', 80, 'блеет'),  # овца
    Animal('Кудрявый', 85, 'блеет'),  # овца
    Animal('Ко-Ко', 2, 'кукарекает'),  # курица
    Animal('Кукареку', 2, 'кукарекает'),  # курица
    Animal('Рога', 50, 'мекает'),  # коза
    Animal('Копыта', 55, 'мекает'),  # коза
    Animal('Кряква', 4, 'крякает')  # утка
]

# 1. Кормим всех животных
for animal in animals:
    animal.feed()

# 2. Доим коров и коз
for animal in animals:
    if animal.is_milking():
        print(f"{animal.name} подоена.")

# 3. Стрижем овец
for animal in animals:
    if animal.is_shearing():
        print(f"{animal.name} пострижена.")

# 4. Собираем яйца у куриц, уток и гусей
for animal in animals:
    if animal.is_collect_eggs():
        print(f"{animal.name} яйца собраны.")

# 5. Подсчитываем общий вес
total_weight = sum(animal.weight for animal in animals)
print(f"Общий вес всех животных: {total_weight} кг.")


max_weight_animal = max(animals, key=lambda animal: animal.weight)
print(f"Максимальный вес: {max_weight_animal.weight} кг. {max_weight_animal.name}.")

for animal in animals:
    if animal.sound == 'мычит':
        print(f"{animal.sound} - корова")
    elif animal.sound == 'блеет':
        print(f"{animal.sound} - овца")
    elif animal.sound == 'гогочет':
        print(f"{animal.sound} - гусь")
    elif animal.sound == 'кукарекает':
        print(f"{animal.sound}  курица")
    elif animal.sound == 'мекает':
        print(f"{animal.sound} - коза")
    elif animal.sound == 'крякает':
        print(f"{animal.sound} - утка")
