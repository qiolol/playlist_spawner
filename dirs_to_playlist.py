#!/usr/bin/env python3
import sys
import os

# https://en.wikipedia.org/wiki/Audio_file_format#List_of_formats
AUDIO_EXTENSIONS = [
    #"3gp", Supports video streams; likely video
    "8svx",
    "aa",
    "aac",
    "aax",
    "act",
    "aiff",
    "alac",
    "amr",
    "ape",
    "au",
    "awb",
    "cda",
    "dct",
    "dss",
    "dvf",
    "flac",
    "gsm",
    "iklax",
    "ivs",
    "m4a",
    "m4b",
    "m4p",
    "mmf",
    "mp3",
    "mpc",
    "msv",
    "nmf",
    "nsf",
    "ogg",
    "oga",
    "mogg",
    "opus",
    "ra",
    "rm",
    "raw",
    "rf64",
    "sln",
    "tta",
    "voc",
    "vox",
    "wav",
    "webm",
    "wma",
    "wv",
]

# https://en.wikipedia.org/wiki/Video_file_format
VIDEO_EXTENSIONS = [
    "3g2",
    "3gp",
    "amv",
    "asf",
    "avi",
    "drc",
    "flv",
    "f4v",
    "f4p",
    "f4a",
    "f4b",
    #"gif",
    #"gifv",
    "mkv",
    "mng",
    "mov",
    "qt",
    "m4v",
    "mp4",
    "m4p",
    "m4v",
    "mpg",
    "mp2",
    "mpeg",
    "mpe",
    "mpv",
    "m2v",
    "mts",
    "m2ts",
    "ts",
    "mxf",
    "nsv",
    "ogv",
    "ogg",
    "rm",
    "rmvb",
    "roq",
    "svi",
    "vob",
    "webm",
    "wmv",
    "yuv",
]

################################################################################
# Determines if F looks like an audio file                                     #
################################################################################
def is_audio(F):
    for ext in AUDIO_EXTENSIONS:
        if F.lower().endswith("." + ext):
            return True
    return False

################################################################################
# Determines if F looks like a video file                                      #
################################################################################
def is_video(F):
    for ext in VIDEO_EXTENSIONS:
        if F.lower().endswith("." + ext):
            return True
    return False

################################################################################
# Determines if F looks like an audio or video file                            #
################################################################################
def is_audio_or_video(F):
    return is_audio(F) or is_video(F)

################################################################################
# Recursively walks in_dir, adding all audio and/or video files (by filename,  #
# alphanumerically) to a playlist string and then returns the playlist string  #
#                                                                              #
# What file type to add is based on the FILE_TYPE argument:                    #
#     "-a" for audio files ending with AUDIO_EXTENSIONS                        #
#     "-v" for video files ending with VIDEO_EXTENSIONS                        #
#     "-av" or "-va" for both audio and video files                            #
#                                                                              #
# Also, if IN_DIR contains a file named ".dontplaylist", all of its files and  #
# all files in any of its subdirectories will be excluded.                     #
################################################################################
def dir_to_playlist(IN_DIR, FILE_TYPE):
    playlist = ""
    if FILE_TYPE == "-a":
        CHECKER = is_audio
    elif FILE_TYPE == "-v":
        CHECKER = is_video
    else:
        CHECKER = is_audio_or_video

    for (dirpath, dirnames, filenames) in os.walk(IN_DIR):
        # Avoid dirs with extras, bonus content, etc. by placing a .dontplaylist
        # file
        if ".dontplaylist" in filenames:
            dirnames.clear()
            continue

        # Sorting dirnames will actually modify the order of the walk!
        # See: https://stackoverflow.com/a/18282602
        dirnames.sort()
        # And we also want to iterate through files in order
        filenames.sort()

        for file in filenames:
            if CHECKER(file):
                playlist += dirpath + "/" + file + "\n"

    return playlist

################################################################################
# Writes a playlist with all audio and/or video files in all dirs given in     #
# sys.argv to a file, ./playlist.m3u (wiped and then written anew if already   #
# exists)                                                                      #
#                                                                              #
# Example usages:                                                              #
#     dirs_to_playlist.py -v shows/Star\ Trek/ shows/Sealab\ 2021/             #
#     dirs_to_playlist.py -av .                                                #
#                                                                              #
# To systematically define multiple playlists with specific playlist           #
# filenames, use spawn_playlists.py                                            #
################################################################################
def main():
    if (
        len(sys.argv) > 2 and
        (
            sys.argv[1] == "-a" or
            sys.argv[1] == "-v" or
            sys.argv[1] == "-av" or
            sys.argv[1] == "-va"
        )
    ):
        OUT_DIR = os.getcwd()
        playlist_str = ""

        for i in range(2, len(sys.argv)):
            if not os.path.isdir(sys.argv[i]):
                sys.exit("ERROR! No such directory: " + sys.argv[i])
            else:
                playlist_str += dir_to_playlist(sys.argv[i], sys.argv[1])

        with open(OUT_DIR + "/" + "playlist.m3u", 'w') as playlist_file:
            playlist_file.write(playlist_str)
    else:
        sys.exit(
"""Usage:\n\tdirs_to_playlist.py TYPE directory/1/ directory/2/ ...
where TYPE is
\t\"-a\" for only audio files,
\t\"-v\" for only video files,
\t\"-av\" or \"-va\" for both audio and video files."""
        )

if __name__ == '__main__':
    main()
