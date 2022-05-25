class Animal:

    def listen_to_the_voice(self):
        print(self.voice)

    def feeding(self):
        if 0 <= self.mood < 5:
            self.mood += 1
            print(f'{self.type} {self.name} покормлен(а)')
        else:
            print(f'{self.type} {self.name} сытый(а)')


class Goose(Animal):
    voice = 'Га-га-га'
    type = 'Гусь'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.mood = 5
        print(f'Я {self.type} {self.name}, {self.voice}')

    def getting_eggs(self):
        if 0 < self.mood <= 5:
            self.mood -= 1
            print(f'Яйца Гуся {self.name} собраны', self.mood)
        else:
            print(f'Яиц у Гуся {self.name} больше нет, пора его кормить !')


class Cow(Animal):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.voice = 'Му-Му'
        self.type = 'Корова'
        self.mood = 5
        print(f'Я {self.type} {self.name}, {self.voice}')

    def milking(self):
        if 0 < self.mood <= 5:
            self.mood -= 1
            print(f'Корова {self.name} подоена')
        else:
            print(f'Доить корову {self.name} бесполезно, пора ее кормить !')


class Sheep(Animal):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.voice = 'Бее-бее'
        self.type = 'Овца'
        self.mood = 5
        print(f'Я {self.type} {self.name}, {self.voice}')

    def shaving(self):
        if 0 < self.mood <= 5:
            self.mood -= 1
            print(f'Овца {self.name} пострижена')
        else:
            print(f'Стричь овцу {self.name} бесполезно, пора ее кормить !')


class Goat(Animal):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.voice = 'Мее-Мее'
        self.type = 'Коза'
        self.mood = 5
        print(f'Я {self.type} {self.name}, {self.voice}')

    def milking(self):
        if 0 < self.mood <= 5:
            self.mood -= 1
            print(f'Коза {self.name} подоена')
        else:
            print(f'Доить Козу {self.name} бесполезно, пора ее кормить !')


class Hens(Animal):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.voice = 'Ко-ко-ко'
        self.type = 'Курица'
        self.mood = 5
        print(f'Я {self.type} {self.name}, {self.voice}')


    def getting_eggs(self):
        if 0 < self.mood <= 5:
            self.mood -= 1
            print(f'Яйца Курицы {self.name} собраны')
        else:
            print(f'Яиц у Курицы {self.name} больше нет, пора ее кормить !')


class Duck(Animal):

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.voice = 'Кря-кря'
        self.type = 'Утка'
        self.mood = 5
        print(f'Я {self.type} {self.name}, {self.voice}')

    def getting_eggs(self):
        if 0 < self.mood <= 5:
            self.mood -= 1
            print(f'Яйца Утки {self.name} собраны')
        else:
            print(f'Яиц у Утки {self.name} больше нет, пора ее кормить !')


def animal_weight(animals):
    result_weight = 0
    for animal in animals:
        result_weight += animal.weight
    return result_weight


def biggest_animal(animals):
    max_weight = 0
    name = ''
    for animal in animals:
        if animal.weight > max_weight:
            max_weight = animal.weight
            name = animal.name
    return name


seryi = Goose('Серый', 15)
belyi = Goose('Белый', 10)
manka = Cow('Манька', 180)
barashek = Sheep('Барашек', 60)
kudryaviy = Sheep('Кудрявый', 57)
koko = Hens('Коко', 2)
kukareku = Hens('Кукареку', 2)
roga = Goat('Рога', 25)
kopita = Goat('Копыта', 26)
kryakva = Duck('Кряква', 7)
animals = [seryi, belyi, manka, barashek, kudryaviy, koko, kukareku, roga, kopita, kryakva]
print(f'Общий вес животных {animal_weight(animals)}')
print(f'Самое тяжелое животное зовут {biggest_animal(animals)}')

for animal in animals:
    animal.feeding()
    animal.listen_to_the_voice()
