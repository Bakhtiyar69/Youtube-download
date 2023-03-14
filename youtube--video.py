# Importing the necessary libraries
from pytube import YouTube

# Asking the user for the YouTube video link
link = input("Enter the YouTube video link: ")

# Creating a YouTube object
yt = YouTube(link)

# Displaying the video details
print("Video Title: ", yt.title)
print("Video Length: ", yt.length, "seconds")
print("Video Views: ", yt.views)

# Selecting the highest resolution available
stream = yt.streams.get_highest_resolution()

# Downloading the video
print("Downloading...")
stream.download()
print("Download completed!")