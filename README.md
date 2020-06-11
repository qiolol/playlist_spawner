# what
A little Linux m3u playlist generator

It makes m3u playlists of the video and/or audio files in the directories given.

# how
## basic way
Use `dirs_to_playlist.py` to make one playlist.

Say you want to make a playlist with all the episodes of your favorite, legally-acquired sci-fi shows:
- `example/shows/Star Trek`
- `example/shows/Sealab 2021`

Feed those two dirs to `dirs_to_playlist.py` with the `-v` flag for video:

```
python dirs_to_playlist.py -v shows/Star\ Trek/ shows/Sealab\ 2021/
```

A playlist file, `playlist.m3u`, will be in the current directory, populated with the episodes in those directories and in their subdirectories.

Playing this file with a player like mpv will play all those episodes in alphanumeric order (of the directories and their episode files -- so `S01` or `Season 1` episodes will be listed before `S02` or `Season 2` episodes; `s01e01.mkv` will be before `s01e02.mkv`, etc.).

But wait. The Star Trek folder has a bunch of extras, bonus content, behind-the-scenes stuff you didn't want in your episodes-only playlist! Say that stuff is in `example/shows/Star Trek/EXTRAS`.

Put a file named `.dontplaylist` in `example/shows/Star Trek/EXTRAS` to have all the files there (and in any subdirectories of `EXTRAS`) excluded, and re-generate the playlist by re-running the command.

For audio playlists, use the `-a` flag. For audio *and* video files, use `-av` or `-va`.

## galaxy brain way
Use `spawn_playlists.py` to make *multiple* playlists.

Specify the playlists in `spawn_playlists.py` with their constituent directories

```python
SCI_FI = [
    "example/shows/Star Trek",
    "example/shows/Sealab 2021",
]
```

and desired filenames

```python
PLAYLISTS = {
    "sci_fi.m3u": SCI_FI,
}
```

(see the file for examples).

Then execute the file with the directory where you want all of the defined playlists to appear (e.g., your media drive):

```
python spawn_playlists.py -v where/you/want/the/playlists
```

`spawn_playlists.py` uses `dirs_to_playlist.py`, so the same `-v`, `-a` flag and `.dontplaylist` rules above apply when running it.

# license
[Mozilla Public License 2.0](https://mozilla.org/MPL/2.0/)
