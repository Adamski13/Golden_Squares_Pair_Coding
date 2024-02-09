from Lib.MusicTracker import *
import pytest

"""
#Given an empty list. Music_library returns empty list.
"""
def test_when_empty_list():
    music_tracker = MusicTracker()
    result = music_tracker.music_library()
    assert result == []

"""
When we add one track. Music_library returns a list with one track.
"""
def test_when_one_track_is_added():
    music_tracker = MusicTracker()
    music_tracker.add_track("Rufus du Sol - Innerbloom")
    assert music_tracker.music_library() == ["Rufus du Sol - Innerbloom"]

"""
When we add multiple tracks. Music_library returns a list with multiple tracks.
"""
def test_when_multiple_tracks_are_added():
    music_tracker = MusicTracker()
    music_tracker.add_track("Rufus du Sol - Innerbloom")
    music_tracker.add_track("Nirvana - Team spirit")
    music_tracker.add_track("Vivaldi - Four Seasons")
    assert music_tracker.music_library() == ["Rufus du Sol - Innerbloom", "Nirvana - Team spirit", "Vivaldi - Four Seasons"]


"""
When we add empty string. Output raises an Exception: "Track cannot be an empty string."
"""
def test_when_empty_string_raise_an_exception():
    music_tracker = MusicTracker()
    with pytest.raises(Exception) as e:
        music_tracker.add_track("")
    error_message = str(e.value)
    assert error_message == "Track cannot be an empty string."

"""
When we add a track that already exist. This raises exception: "Track already added."
"""
def test_when_adding_track_that_already_exists():
    music_tracker = MusicTracker()
    music_tracker.add_track("Rufus du Sol - Innerbloom")
    with pytest.raises(Exception) as e:
        music_tracker.add_track("Rufus du Sol - Innerbloom")
    error_message = str(e.value)
    assert error_message == "Track already added."