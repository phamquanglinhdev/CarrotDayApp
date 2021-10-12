from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *


class Loading:
    def __init__(self):
        self.loadbox = QMessageBox()
        # self.loadbox.setFixedSize(300, 300)
        # # loadbox.setWindowFlags(Qt.FramelessWindowHint)
        # self.loadbox.setText("Xin chờ")
        self.loadbox.setWindowTitle("Wait...")
