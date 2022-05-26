'''У класса Track есть поля:

Название;
Длительность в минутах(используется тип данных int). И метод show, выводящий информацию по треку в виде <Название-Длительность>.
У класса Album есть поля:

Название альбома
Группа
Список треков И три метода:
get_tracks - выводит информацию по всем трекам(используется метод show).
add_track - добавление нового трека в список треков.
get_duration - выводит длительность всего альбома.
Задание:
Создать 2 альбома с 3 треками. Для каждого вывести его длительность.'''


class Album:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.track_list = []

    def get_tracks(self):
        for track in self.track_list:
            track.show()

    def add_track(self, track):
        self.track_list.append(track)

    def get_duration(self):
        result_duration = 0
        for track in self.track_list:
            result_duration += track.duration
        print(result_duration)


class Track:

    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def show(self):
        print(f'<{self.title}-{self.duration}>')


first_album = Album('First', 'Gitarrrist')
tr1 = Track('Good', 2)
# tr1.show()
tr2 = Track('Better', 4)
# tr2.show()
tr3 = Track('Best', 9)
# tr3.show()
first_album.add_track(tr1)
first_album.add_track(tr2)
first_album.add_track(tr3)
first_album.get_tracks()
first_album.get_duration()
second_album = Album('Oak', 'Druum IT!')
tr4 = Track('God', 18)
# tr4.show()
tr5 = Track('Litter', 14)
# tr5.show()
tr6 = Track('Beast', 28)
# tr6.show()
second_album.add_track(tr4)
second_album.add_track(tr5)
second_album.add_track(tr6)

second_album.get_tracks()
second_album.get_duration()

