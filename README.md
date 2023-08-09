# YouTube Downloader

This project is a simple script to download audio from YouTube videos or playlists. It uses the `pytube` library to fetch the video or playlist from YouTube and then uses `ffmpeg` to convert the video into the desired audio format.

## Installation

Before running the script, you need to install the required Python libraries. You can do this by running:

```bash
pip install pytube
```

You also need to have `ffmpeg` installed on your system. You can download it from the [official website](https://ffmpeg.org/download.html).

## Usage

To use the script, simply run it with Python:

```bash
python audio_downloader.py
```

The script will prompt you to enter a YouTube video or playlist URL. After entering the URL, you will be asked to choose the audio format (mp3 or mp4).

If you enter a playlist URL, the script will download all videos in the playlist and convert them to the chosen audio format.

The downloaded audio files will be saved in the same directory as the script.

## Note

The script uses a regular expression to fix an issue with the `pytube` library where the `Playlist.videos` list is empty. This may not be necessary in future versions of the library.

## Error Handling

If you enter an invalid URL or choose to exit the program, the script will print an error message and then prompt you to enter another URL. If any other error occurs during the download or conversion process, the script will print an error message and exit.

## Contact

* [Kishan Rajeev](https://kishan.knowledgeplatter.com/)

## License

Youtube Downloader is licensed under the MIT License.
