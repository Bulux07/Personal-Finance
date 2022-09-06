from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)
#optional dont need it to download the video
#just good to see the infortmation and make sure im downloading the right one
print("Title: ", yt.title)
print("View: ", yt.views)

yd = yt.streams.get_highest_resolution()

yd.download('the path where you wanted save')