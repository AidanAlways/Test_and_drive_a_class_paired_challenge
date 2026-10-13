class MusicLibrary:
    def __init__(self):
        self.library = []

    def add(self, track):
        if track == "":
            raise Exception("Can't add a track without a name.")
        self.library.append(track)

    def list_tracks(self):
        return self.library