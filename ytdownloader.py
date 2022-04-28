from pytube import YouTube
yt=YouTube("https://youtu.be/zskVcTSVlLY")

x=yt.streams.filter(file_extension="mp4")
y=x.get_by_resolution("720p")
y.download("E:/tkinter")