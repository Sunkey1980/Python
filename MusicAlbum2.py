class Album:

    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.track_list = []

    def __str__(self):
        s = ''
        for track in self.track_list:
            s += '\n       ' + str(track)
        return f'Name group: {self.artist} ' \
               f'\nName album: {self.title}' \
               f'\nTracks:' \
               f'{s}'

    def get_tracks(self):
        for track in self.track_list:
            print(track)

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

    def __str__(self):
        return f'{self.title}-{self.duration}min'

    def __repr__(self):
        return f'{self.title}-{self.duration}min'

    def show(self):
        print(f'<{self.title}-{self.duration}>')

    def __eq__(self, other):
        return self.duration == other.duration

    def __ne__(self, other):
        return self.duration != other.duration

    def __lt__(self, other):
        return self.duration < other.duration

    def __gt__(self, other):
        return self.duration > other.duration

    def __le__(self, other):
        return self.duration <= other.duration

    def __ge__(self, other):
        return self.duration >= other.duration


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
# first_album.get_tracks()
# first_album.get_duration()
second_album = Album('Oak', 'Druum IT!')
tr4 = Track('God', 18)
# tr4.show()
tr5 = Track('Litter', 14)
# tr5.show()
tr6 = Track('Beast', 18)
# tr6.show()
second_album.add_track(tr4)
second_album.add_track(tr5)
second_album.add_track(tr6)

# second_album.get_tracks()
# second_album.get_duration()

print(first_album)
print(tr4 == tr6)
print(tr4 != tr6)
print(tr4 > tr6)
print(tr4 < tr6)
print(tr4 >= tr6)
print(tr4 <= tr6)
