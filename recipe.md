# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So that I can keep track of my music listening
I want to add tracks I've listened to and see a list of them.

## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

Name class:
class MusicLibrary()



```python
# EXAMPLE

class MusicLibrary():
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        #   name: empty list
        # Side effects:
        #   None
        library = []
        pass # No code here yet

    def add(self, track):
        # Parameters:
        #   string: track name
        # Returns:
        #   Nothing
        # Side-effects
        #   Modifies the track list
        pass # No code here yet

    def list_tracks(self):
        # Returns:
        #   List of tracks strings
        # Side-effects:
        #   None
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python

def test_init_empty_list():
    music_library = MusicLibrary()
    assert music_library.library == []

def test_add_track():
    music_library = MusicLibrary()
    music_library.add("Mr Brightside")
    result = music_library.library[0]
    assert music_library.add() == ["Mr Brightside"]

def test_add_2_tracks():
    music_library = MusicLibrary()
    music_library.add("Karma Police")
    music_library.add("Creep")
    result = music_library.library[0]
    assert music_library.add() == ["Karma Police", "Creep"]

def test_list_tracks():
    music_library = MusicLibrary()
    music_library.add("Mr Brightside")
    result = music_library.list()
    assert result == ["Mr Brightside"]

def test_empty_track():
    music_library = MusicLibrary()
    with pytest.raises(Exception) as error:
        music_library.add("")
    error_message = str(error.value)
    assert error_message == "Can't add a track without a name."

def test_adds_track_then_list():
    music_library = MusicLibrary()
    music_library.add("Mr Brightside")
    result = music_library.list()
    assert result == ["Mr Brightside"]

# EXAMPLE

"""
Given a name and a task
#remind reminds the user to do the task
"""
reminder = Reminder("Kay")
reminder.remind_me_to("Walk the dog")
reminder.remind() # => "Walk the dog, Kay!"

"""
Given a name and no task
#remind raises an exception
"""
reminder = Reminder("Kay")
reminder.remind() # raises an error with the message "No task set."

"""
Given a name and an empty task
#remind still reminds the user to do the task, even though it looks odd
"""
reminder = Reminder("Kay")
reminder.remind_me_to("")
reminder.remind() # => ", Kay!"
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
