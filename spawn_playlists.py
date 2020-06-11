#!/usr/bin/env python3
import sys
import os

from dirs_to_playlist import dir_to_playlist

################################################################################
# Writes the playlists below (composed of directories) to corresponding        #
# playlist files in the dir given in sys.argv[2]                               #
#                                                                              #
# What file type to add is based on on sys.argv[1]:                            #
#     "-a" for audio files ending with AUDIO_EXTENSIONS                        #
#     "-v" for video files ending with VIDEO_EXTENSIONS                        #
#     "-av" or "-va" for both audio and video files                            #
#                                                                              #
# Example usages:                                                              #
#     spawn_playlists.py -v where/you/want/the/playlists                       #
#     spawn_playlists.py -av .                                                 #
################################################################################
# Playlists, composed of one or more directories of video or audio files
# (Use full, not relative, paths without shell expansion vars like $HOME)
SCI_FI = [
    "example/shows/Star Trek",
    "example/shows/Sealab 2021",
]

GOOD_MUSIC = [
    "example/music/Clutch",
    "example/music/Smash Mouth/All Star.mp3",
    "example/music/02 Let's Go (feat. Lil' Jon & Twista).m4a",
]

ANOTHER_PLAYLIST = [
    # ...
]

AND_ANOTHER = [
    # ...
]

# All the playlists with their desired filenames
PLAYLISTS = {
    "sci_fi.m3u": SCI_FI,
    "good_music.m3u": GOOD_MUSIC,
    "another_playlist.m3u": ANOTHER_PLAYLIST,
    "and_another.m3u": AND_ANOTHER,
}

if (
    len(sys.argv) > 2 and
    (
        sys.argv[1] == "-a" or
        sys.argv[1] == "-v" or
        sys.argv[1] == "-av" or
        sys.argv[1] == "-va"
    )
):
    OUT_DIR = sys.argv[2]

    if not os.path.isdir(OUT_DIR):
        sys.exit("ERROR! No such output directory: " + OUT_DIR)

    for p in PLAYLISTS.items():
        playlist_str = ""

        for dir in p[1]:
            if not os.path.isdir(dir):
                sys.exit("ERROR! No such directory: " + dir)
            else:
                playlist_str += dir_to_playlist(dir, sys.argv[1])

        with open(OUT_DIR + "/" + p[0], "w") as playlist_file:
            playlist_file.write(playlist_str)
else:
    sys.exit(
"""Usage:\n\tspawn_playlists.py TYPE where/you/want/the/playlists
where TYPE is
\t\"-a\" for only audio files,
\t\"-v\" for only video files,
\t\"-av\" or \"-va\" for both audio and video files."""
    )
