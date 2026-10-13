import pytest
from lib.music_library import MusicLibrary

# Test that is initialized with an empty list
def test_init_empty_list():
    music_library = MusicLibrary()
    assert music_library.library == []

# Add track to library
def test_add_track():
    music_library = MusicLibrary()
    music_library.add("Mr Brightside")
    result = music_library.library
    assert result == ["Mr Brightside"]

# Add multiple tracks to library
def test_add_2_tracks():
    music_library = MusicLibrary()
    music_library.add("Karma Police")
    music_library.add("Creep")
    result = music_library.library
    assert result == ["Karma Police", "Creep"]

# List library of tracks 
def test_list_tracks():
    music_library = MusicLibrary()
    music_library.add("Mr Brightside")
    result = music_library.list_tracks()
    assert result == ["Mr Brightside"]

# test adding track and then viewing list of tracks
def test_adds_track_then_list():
    music_library = MusicLibrary()
    music_library.add("Mr Brightside")
    result = music_library.list_tracks()
    assert result == ["Mr Brightside"]

# throw error if empty track name 
def test_empty_track():
    music_library = MusicLibrary()
    with pytest.raises(Exception) as error:
        music_library.add("")
    error_message = str(error.value)
    assert error_message == "Can't add a track without a name."
