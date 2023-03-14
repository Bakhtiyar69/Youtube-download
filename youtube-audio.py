# Importing the necessary libraries
from pytube import YouTube
from moviepy.editor import *

# Asking the user for the YouTube video link
link = input("Enter the YouTube video link: ")

# Creating a YouTube object
yt = YouTube(link)

# Selecting the highest resolution available
stream = yt.streams.get_highest_resolution()

# Downloading the video
print("Downloading...")
stream.download()
print("Download completed!")

# Creating a video clip object from the downloaded file
video_clip = VideoFileClip(stream.default_filename)

# Extracting the audio from the video clip
audio_clip = video_clip.audio

# Setting the output file name
output_file = yt.title + ".mp3"

# # Saving the audio clip as an MP3 file
# print("Converting to MP3...")
# audio_clip.write_audiofile(output_file)
# print("Conversion completed!")

# Saving the audio clip as an MP3 file with a 320kbps codec
print("Converting to MP3 with 320kbps codec...")
audio_clip.write_audiofile(output_file, bitrate="320k")
print("Conversion completed!")