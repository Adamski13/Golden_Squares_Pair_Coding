class MusicTracker:
    def __init__(self):
        self.track_list = []

    def add_track(self, track):
        if track == "":
            raise Exception("Track cannot be an empty string.")
        if track in self.track_list:
            raise Exception("Track already added.")
        self.track_list.append(track)

    def music_library(self):
        return self.track_list