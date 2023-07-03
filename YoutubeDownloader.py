
# This script is a small snippet of code to use to download videos from youtube without Youtube Premium 
# Make sure you have pytube installed before this 
# pip install pytube3

from pytube import YouTube

def YoutubeDownload():
    print("Copy and paste the link here the video You'd like to download")
    link = input()

    if type(link) == str:
            yt = YouTube(link)

            download = yt.streams.get_highest_resolution()

            location = input("What directory you want to save to:")

            if type(location) == str:
                download.download(location)

                #Title of video
                print("Title: ",yt.title)

                #Length of the video
                print("Length of video: ",yt.length,"seconds")

                print("---------------------------------")
                print("Video downloaded successfuly")

            else: 
                print("Incorrect input for Directory")
                YoutubeDownload()

    else:
        print("Please enter a valid URL")
        YoutubeDownload()

YoutubeDownload()