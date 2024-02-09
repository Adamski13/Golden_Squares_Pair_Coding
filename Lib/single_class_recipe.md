# {{PROBLEM}} Class Design Recipe
## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class MusicTracker:
    def __init__(self):
        # Parameters:
        #   name: string
        # Side effects:
        #   Sets empty list containing tracks
        # Empty list
        pass 

    def add_track(self, track):
        # Parameters:
        #   string representing track
        # Returns:
        #   Nothing
        # Side-effects
        #   Adds the track to our list
        pass 

    def music_library(self):
        # Returns:
        #   A list of tracks that user listened to
        # Side-effects:
        #   None
        pass
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given an empty list. Music_library returns empty list.
"""
music_tracker = MusicTracker()
music_tracker.music_library() => []


"""
When we add one track. Music_library returns a list with one track.
"""
music_tracker = MusicTracker()
music_tracker.add_track("Rufus du Sol - Innerbloom")
music_tracker.music_library() => ["Rufus du Sol - Innerbloom"]


"""
When we add multiple tracks. Music_library returns a list with multiple tracks.
"""
music_tracker = MusicTracker()
music_tracker.add_track("Rufus du Sol - Innerbloom")
music_tracker.add_track("Nirvana - Team spirit")
music_tracker.add_track("Vivaldi - Four Seasons")
music_tracker.music_library() => ["Rufus du Sol - Innerbloom", "Nirvana- Team spirit", "Vivaldi - Four Seasons"]


"""
When we add empty string. Output raises an Exception: "Track cannot be an empty string."
"""
music_tracker = MusicTracker()
music_tracker.add_track("") => ["Track cannot be an empty string."]


"""
When we add a track that already exist. This raises exception: "Track already added."
"""
music_tracker = MusicTracker()
music_tracker.add_track("Rufus du Sol - Innerbloom")
music_tracker.add_track("Rufus du Sol - Innerbloom") => "Track already added."
music_tracker.music_library() => ["Rufus du Sol - Innerbloom"]


## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
