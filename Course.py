import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from Database import DataVideo
from PyQt5.QtGui import *
from Video import Video
import requests
import time
from PyQt5.QtCore import *


class Ui_Course(QWidget):
    def setupUi(self, Course,MainWindow):
        # self.centerScreen()
        # Course.setMaximumSize(QSize(1140, 400))
        Course.setObjectName("Course")
        Course.setStyleSheet("background:black")
        Course.setFixedWidth(399*3)
        Course.setFixedHeight(900)
        Course.setWindowFlags(Qt.WindowCloseButtonHint)
        self.container = QVBoxLayout(Course)
        self.content = QGridLayout()
        self.box = QGroupBox()
        self.box.setLayout(self.content)
        self.box.setStyleSheet("background:black")
        self.container.setObjectName("verticalLayout")
        self.refresh = QPushButton("Làm mới", clicked=lambda: self.refreshApp())
        self.refresh.setStyleSheet("background:#FFB6C1;color:white;font:12pt bold;border:none;padding:4")
        self.refresh.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        self.container.addWidget(self.refresh)
        self.scroller = QScrollArea()
        # self.scroller.setFixedWidth(1140)
        # self.scroller.setFixedHeight(600)
        self.scroller.setWidget(self.box)
        self.container.addWidget(self.scroller)
        self.scroller.setWidgetResizable(True)
        Course.setWindowTitle("Video của CarrotDay")
        Course.setWindowIcon(QIcon("favicon.png"))
        # self.setLayout(self.container)
        self.grixX = 1
        self.grixY = 1
        datas = DataVideo().videos
        for video in datas:
            self.createBox(video)
            # print(video)
        self.process = QProgressBar()
        # self.process.setText("Click vào video để mở nhé")
        self.container.addWidget(self.process)

    def createBox(self, video):
        image = QImage()
        image.loadFromData(requests.get(video['thumbnail']).content)
        # image_label = QLabel()
        # image_label.setPixmap(QPixmap(image))
        # image_label.setFixedSize(300, 300)
        # image_label.click.connect(self.OpenVideo(src))
        btn = QPushButton(clicked=lambda: self.OpenVideo(video['src']))
        # btn.setText("    " + video["name"])
        btn.setFixedSize(333, 200)
        btn.setStyleSheet("font: 18pt \"VL Selphia\";\n"
                          "color: black;\n"
                          # "background-color: rgb(255, 255, 255);\n"
                          "text-align:left;\n"
                          # "border:none\n"
                          "")
        btn.setCursor(QCursor(QtCore.Qt.PointingHandCursor))
        btn.setIcon(QIcon(QPixmap(image)))
        btn.setIconSize(QSize(333, 290))
        btn.setToolTip(video["name"])
        btn.setToolTipDuration(0)
        label = QLabel(video["name"])
        label.setFixedSize(333, 20)
        label.setStyleSheet("font: 12pt \"VL Selphia\";\n"
                            "color: white;\n"
                            # "background-color: rgb(255, 255, 255);\n"
                            "text-align:left;\n"
                            # "border:none\n"
                            "")
        box = QGroupBox()
        layout = QGridLayout()
        box.setFixedSize(360, 300)
        box.setStyleSheet("background:black")
        layout.addWidget(btn)
        layout.addWidget(label)
        box.setLayout(layout)
        self.content.addWidget(box, self.grixX, self.grixY)
        self.grixY += 1
        if self.grixY > 3:
            self.grixY = 1
            self.grixX += 1

    def OpenVideo(self, src):
        self.thread = QThread()
        self.worker = Worker(src, self.process)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()
        for x in range(100):
            time.sleep(0.1)
            self.process.setValue(x)
        self.container.setEnabled(False)
        self.thread.finished.connect(
            lambda: self.process.setValue(0)
        )
        self.thread.finished.connect(
            lambda: self.container.setEnabled(True)
        )

    def refreshApp(self):
        self.grixX = 1
        self.grixY = 1
        datas = DataVideo().videos
        for video in datas:
            self.createBox(video)
        self.msgBox = QMessageBox()
        self.msgBox.setIcon(QMessageBox.Information)
        self.msgBox.setText("Đã cập nhật lại")
        self.msgBox.setWindowTitle("Thành công")
        self.msgBox.show()

    def centerScreen(self):
        width = app.primaryScreen().size().width()
        height = app.primaryScreen().size().height()
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class Worker(QObject):
    def __init__(self, src, bar):
        super().__init__()
        self.src = src
        self.bar = bar

    finished = pyqtSignal()
    progress = pyqtSignal(int)
    print(progress)

    def run(self):
        """Long-running task."""
        # self.bar.setValue(progress)
        Video(self.src)
        self.finished.emit()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Course = QtWidgets.QWidget()
    ui = Ui_Course()
    ui.setupUi(Course)
    Course.show()
    sys.exit(app.exec_())
