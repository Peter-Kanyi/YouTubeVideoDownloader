import pytube
# we'll save the downloaded video in the current dir

download_loc = './'

# prompt the user to key in the url
video_url = input('Enter your YouTube Video: ')

#creating an instance of the YouTube video
video_instance = pytube.YouTube(video_url)

stream = video_instance.streams.get_highest_resolution()

# downloading

stream.download()