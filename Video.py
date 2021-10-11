import sys
import urllib.request
import os


class Video():
    def __init__(self, video_url="https://www.w3schools.com/html/mov_bbb.mp4"):
        self.video_url = video_url
        dir = "C:/ProgramData/PQLdev/CarrotDay/video"
        if not os.path.exists(dir):
            os.makedirs(dir)
        save_path = dir + "/" + os.path.basename(self.video_url)
        if not os.path.exists(save_path):
            urllib.request.urlretrieve(self.video_url, save_path)
        os.startfile(save_path)
