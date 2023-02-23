from pytube import YouTube
# YouTube('https://youtu.be/2lAe1cqCOXo').streams.first().download()
# YouTube('https://youtu.be/2lAe1cqCOXo').streams.get_highest_resolution().download()
# path="E:downloads\\"
YouTube('https://youtu.be/2lAe1cqCOXo').streams.get_highest_resolution().download()


