from app.models import User, Playlist, Track, PlaylistTrack, insert_playlists_tracks


def test_insert_user(session):

    u = User(email="test@test.com", username="tester", active=True)
    session.add(u)
    session.commit()

    assert User.query.count() == 1


def test_no_users():
    assert User.query.count() == 0


def test_add_playlist_tracks(session):

    playlists = [Playlist(spotify_id="0" * 22), Playlist(spotify_id="1" * 22)]
    session.add_all(playlists)
    tracks = [
        Track(spotify_id="0" * 22, name="0"),
        Track(spotify_id="1" * 22, name="1"),
        Track(spotify_id="2" * 22, name="2"),
        Track(spotify_id="3" * 22, name="3"),
    ]
    session.add_all(tracks)
    session.commit()

    playlist_tracks = [
        PlaylistTrack(playlist_id=1, track_id=1),
        PlaylistTrack(playlist_id=1, track_id=2),
        PlaylistTrack(playlist_id=2, track_id=3),
        PlaylistTrack(playlist_id=2, track_id=4),
    ]
    session.add_all(playlist_tracks)
    session.commit()

    assert PlaylistTrack.query.count() == 4


p_unique = {
    "id": "0" * 22,
    "tracks": [
        {"id": "0" * 22, "name": "track0"},
        {"id": "1" * 22, "name": "track1"},
        {"id": "2" * 22, "name": "track2"},
    ],
}

p_partial_overlap_1 = {
    "id": "1" * 22,
    "tracks": [
        {"id": "3" * 22, "name": "track3"},
        {"id": "4" * 22, "name": "track4"},
    ],
}

p_partial_overlap_2 = {
    "id": "2" * 22,
    "tracks": [
        {"id": "3" * 22, "name": "track3"},
        {"id": "5" * 22, "name": "track5"},
    ],
}

p_full_overlap = {
    "id": "3" * 22,
    "tracks": [
        {"id": "3" * 22, "name": "track3"},
        {"id": "5" * 22, "name": "track5"},
    ],
}


def test_insert_unique_playlist_tracks():

    insert_playlists_tracks(p_unique)

    assert PlaylistTrack.query.count() == 3


def test_insert_tracks_from_two_playlists():

    insert_playlists_tracks(p_unique)
    insert_playlists_tracks(p_partial_overlap_1)

    assert Track.query.count() == 5
    assert Playlist.query.count() == 2
    assert PlaylistTrack.query.count() == 5


def test_insert_overlapping_tracks():
    insert_playlists_tracks(p_partial_overlap_1)
    insert_playlists_tracks(p_partial_overlap_2)

    assert Track.query.count() == 3
    assert Playlist.query.count() == 2
    # assert PlaylistTrack.query.count() == 4
