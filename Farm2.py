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

    def __init__(self, name, weight, type='Гусь', voice='Га-га-га'):
        self.name = name
        self.weight = weight
        self.voice = voice
        self.type = type
        self.mood = 5
        print(f'Я {self.type} {self.name}, {self.voice}')


    def getting_eggs(self):
        if 0 < self.mood <= 5:
            self.mood -= 1
            print(f'Яйца Гуся {self.name} собраны', self.mood)
        else:
            print(f'Яиц у Гуся {self.name} больше нет, пора его кормить !')



class Cow(Animal):

    def __init__(self, name, weight, type='Корова', voice='Му-Му'):
         self.name = name
         self.weight = weight
         self.voice = voice
         self.type = type
         self.mood = 5
         print(f'Я {self.type} {self.name}, {self.voice}')

    def milking(self):
        if 0 < self.mood <= 5:
            self.mood -= 1
            print(f'Корова {self.name} подоена')
        else:
            print(f'Доить корову {self.name} бесполезно, пора ее кормить !')


class Sheep(Animal):

    def __init__(self, name, weight, type='Овца', voice='Бее-бее'):
        self.name = name
        self.weight = weight
        self.voice = voice
        self.type = type
        self.mood = 5
        print(f'Я {self.type} {self.name}, {self.voice}')


    def shaving(self):
        if 0 < self.mood <= 5:
            self.mood -= 1
            print(f'Овца {self.name} пострижена')
        else:
            print(f'Стричь овцу {self.name} бесполезно, пора ее кормить !')


class Goat(Animal):

    def __init__(self, name, weight, type='Коза', voice='Мее-Мее'):
        self.name = name
        self.weight = weight
        self.voice = voice
        self.type = type
        self.mood = 5
        print(f'Я {self.type} {self.name}, {self.voice}')

    def milking(self):
        if 0 < self.mood <= 5:
            self.mood -= 1
            print(f'Коза {self.name} подоена')
        else:
            print(f'Доить Козу {self.name} бесполезно, пора ее кормить !')


class Hens:
    def __init__(self, name, weight, type='Курица', voice='Ко-ко-ко'):
        self.name = name
        self.weight = weight
        self.voice = voice
        self.type = type
        self.mood = 5
        print(f'Я {self.type} {self.name}, {self.voice}')

    def getting_eggs(self):
        if 0 < self.mood <= 5:
            self.mood -= 1
            print(f'Яйца Курицы {self.name} собраны')
        else:
            print(f'Яиц у Курицы {self.name} больше нет, пора ее кормить !')


class Duck(Animal):

    def __init__(self, name, weight, type='Утка', voice='Кря-кря'):
        self.name = name
        self.weight = weight
        self.voice = voice
        self.type = type
        self.mood = 5
        print(f'Я {self.type} {self.name}, {self.voice}')

    def getting_eggs(self):
        if 0 < self.mood <= 5:
            self.mood -= 1
            print(f'Яйца Утки {self.name} собраны')
        else:
            print(f'Яиц у Утки {self.name} больше нет, пора ее кормить !')

#
# def animal_weight(animal_dict):
#     result_weight = 0
#     for animal in animal_dict.values():
#         result_weight += animal
#     return result_weight
#
#
# def biggest_animal(animal_dict):
#     max_weight = 0
#     name = ''
#     for name_animal, weight in animal_dict.items():
#         if weight > max_weight:
#             max_weight = weight
#             name = name_animal
#     return name
#

animals = []
seryi = Goose('Серый', 15)
animals.append(seryi)
belyi = Goose('Белый', 10)
animals.append(belyi)
manka = Cow('Манька', 180)
animals.append(manka)
barashek = Sheep('Барашек', 60)
animals.append(barashek)

# first_sheep = Sheeps('Барашек', 60)
# animals[first_sheep.name] = first_sheep.weight
# second_sheep = Sheeps('Кудрявый', 57)
# animals[second_sheep.name] = second_sheep.weight
# first_hen = Hens('Коко', 2)
# animals[first_hen.name] = first_hen.weight
# second_hen = Hens('Кукареку', 2)
# animals[second_hen.name] = second_hen.weight
# first_goat = Goats('Рога', 25)
# animals[first_goat.name] = first_goat.weight
# second_goat = Goats('Копыта', 26)
# animals[second_goat.name] = second_goat.weight
# first_duck = Ducks('Кряква', 7)
# animals[first_duck.name] = first_duck.weight
#
# first_goose.feeding()
# first_goose.getting_eggs()
# first_goose.getting_eggs()
# first_goose.getting_eggs()
# first_goose.getting_eggs()
# first_goose.getting_eggs()
# first_goose.getting_eggs()
# first_goose.getting_eggs()
# first_goose.feeding()
# first_goose.feeding()
# first_goose.feeding()
# first_goose.feeding()
# first_goose.feeding()
# first_goose.feeding()
#
# second_goose.feeding()
# second_goose.getting_eggs()
# first_cow.feeding()
# first_cow.milking()
# first_sheep.feeding()
# first_sheep.shaving()
# second_sheep.feeding()
# second_sheep.shaving()
# first_hen.feeding()
# first_hen.getting_eggs()
# second_hen.feeding()
# second_hen.getting_eggs()
# first_goat.feeding()
# first_goat.milking()
# second_goat.feeding()
# second_goat.milking()
# first_duck.feeding()
# first_duck.getting_eggs()
#
# print(f'Общий вес животных {animal_weight(animals)}')
for animal in animals:
    animal.feeding()
    animal.listen_to_the_voice()



