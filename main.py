import os
import sys
import re
import subprocess
from pytube import YouTube, Playlist


def audio_downloader():
    DOWNLOAD_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)))

    try:
        url = input("Enter video or playlist URL: ")
        if url == "exit":
            sys.exit()
        else:
            format_choice = input("Enter 'mp3' or 'mp4' to choose the audio format: ")
            if 'playlist' in url:
                playlist = Playlist(url)
                # This fixes the empty playlist.videos list
                playlist._video_regex = re.compile(r"\"url\":\"(/watch\?v=[\w-]*)")
                print(len(playlist.video_urls))
                for url in playlist.video_urls:
                    print(url)
                for video in playlist.videos:
                    audioStream = video.streams.filter(only_audio=True).get_by_itag('251')
                    videoStream = video.streams.get_highest_resolution()
                    audio_file = audioStream.download(output_path=DOWNLOAD_DIR)
                    video_file = videoStream.download(output_path=DOWNLOAD_DIR)
                    # Merge the audio and video files into a single file
                    if format_choice == 'mp3':
                        output_file = os.path.splitext(video_file)[0] + '.mp3'
                        subprocess.run(['ffmpeg', '-i', audio_file, '-i', video_file, '-c:v', 'copy', '-c:a', 'libmp3lame', '-q:a', '2', output_file])
                    else:
                        output_file = os.path.splitext(video_file)[0] + '.mp4'
                        subprocess.run(['ffmpeg', '-i', audio_file, '-i', video_file, '-c:v', 'copy', '-c:a', 'copy', output_file])
                    # Delete the original audio and video files
                    os.remove(audio_file)
                    os.remove(video_file.replace('.mp4', '.webm'))
            else:
                video = YouTube(url)
                audioStream = video.streams.filter(only_audio=True).get_by_itag('251')
                videoStream = video.streams.get_highest_resolution()
                audio_file = audioStream.download(output_path=DOWNLOAD_DIR)
                video_file = videoStream.download(output_path=DOWNLOAD_DIR)
                # Merge the audio and video files into a single file
                if format_choice == 'mp3':
                    output_file = os.path.splitext(video_file)[0] + '.mp3'
                    subprocess.run(['ffmpeg', '-i', audio_file, '-i', video_file, '-c:v', 'copy', '-c:a', 'libmp3lame', '-q:a', '2', output_file])
                else:
                    output_file = os.path.splitext(video_file)[0] + '.mp4'
                    subprocess.run(['ffmpeg', '-i', audio_file, '-i', video_file, '-c:v', 'copy', '-c:a', 'copy', output_file])
                # Delete the original audio and video files
                os.remove(audio_file)
                os.remove(video_file.replace('.mp4', '.webm'))
    except:
        if url == "exit":
            print("Exiting program... ")
        else:
            print("Invalid Input, please input a valid Playlist or Video link.")


if __name__ == "__main__":
    while True:
        audio_downloader()
