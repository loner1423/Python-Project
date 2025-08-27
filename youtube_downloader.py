"""
YouTube Video Downloader
Requires: pip install pytube
Run: python youtube_downloader.py URL
"""
import sys
from pytube import YouTube
if __name__=="__main__":
    if len(sys.argv)<2: print("Usage: python youtube_downloader.py URL"); sys.exit(1)
    yt=YouTube(sys.argv[1])
    stream=yt.streams.get_highest_resolution()
    print("Downloading:",yt.title)
    stream.download()
    print("Done.")
