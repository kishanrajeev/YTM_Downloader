import os
import sys
import re
import subprocess
from pytube import YouTube, Playlist

def audio_downloader():

    YOUTUBE_STREAM_AUDIO = '140' # modify the value to download a different stream
    DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

    try:
        url = input("Enter video or playlist URL: ")
        if url == "exit":
            sys.exit()
        else:
            if 'playlist' in url:
                playlist = Playlist(url)
                # This fixes the empty playlist.videos list
                playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
                print(len(playlist.video_urls))
                for url in playlist.video_urls:
                    print(url)
                for video in playlist.videos:
                    audioStream = video.streams.filter(only_audio=True).get_by_itag(YOUTUBE_STREAM_AUDIO)
                    audioStream.download(output_path=DOWNLOAD_DIR)
                    # Convert the downloaded .mp4 file to .mp3 format
                    mp4_file = os.path.join(DOWNLOAD_DIR, audioStream.default_filename)
                    mp3_file = os.path.splitext(mp4_file)[0] + '.mp3'
                    subprocess.run(['ffmpeg', '-i', mp4_file, mp3_file])
                    # Delete the original .mp4 file
                    os.remove(mp4_file)
            else:
                video = YouTube(url)
                audioStream = video.streams.filter(only_audio=True).get_by_itag(YOUTUBE_STREAM_AUDIO)
                audioStream.download(output_path=DOWNLOAD_DIR)
                # Convert the downloaded .mp4 file to .mp3 format
                mp4_file = os.path.join(DOWNLOAD_DIR, audioStream.default_filename)
                mp3_file = os.path.splitext(mp4_file)[0] + '.mp3'
                subprocess.run(['ffmpeg', '-i', mp4_file, mp3_file])
                # Delete the original .mp4 file
                os.remove(mp4_file)
    except:
        if url == "exit":
            print("Exiting program... ")
        else:
            print("Invalid Input, please input a valid Playlist or Video link.")

if __name__ == "__main__":
    audio_downloader()