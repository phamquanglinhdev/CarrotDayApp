from PyQt5 import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from VideoData import Data
from PyQt5.QtGui import *
import sys
import requests


class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.container = QHBoxLayout()
        self.setLayout(self.container)
        datas = Data().videos
        for video in datas:
            self.createBox(datas[video]['url'])

    def createBox(self, url):
        image = QImage()
        image.loadFromData(requests.get(url).content)
        image_label = QLabel()
        image_label.setPixmap(QPixmap(image))
        image_label.setBaseSize(300, 300)
        self.container.addWidget(image_label)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    test = Test()
    test.show()
    sys.exit(app.exec_())
