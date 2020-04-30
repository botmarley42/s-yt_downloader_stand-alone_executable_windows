# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import youtube_dl
from PyQt5.QtCore import QRegExp, QThread, pyqtSignal
from PyQt5.QtGui import QRegExpValidator
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import webbrowser
import sys
import os
import youtube_downloader.yt_resources


#used 3 to prevent console for ffmeg to open up in the postprocessor, ffmpeg.py

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)


def build_messagebox(messagebox_icon, messagebox_text, messabox_window_title):

    msgBox = QMessageBox()
    msgBox.setWindowIcon(ui.window_icon)
    msgBox.setIcon(messagebox_icon)
    msgBox.setText(messagebox_text)
    msgBox.setWindowTitle(messabox_window_title)
    msgBox.setStandardButtons(QMessageBox.Ok)
    msgBox.deleteLater()
    msgBox.exec()


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 300)

        self.workerthread = ThreadClass()

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.youtube_btn = QtWidgets.QPushButton(self.centralwidget)
        self.youtube_btn.setText("")
        self.window_icon = QtGui.QIcon()
        self.window_icon.addPixmap(QtGui.QPixmap(':/ytdl_resources/youtube_dl_icon.ico'),
                                   QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(self.window_icon)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(':/ytdl_resources/youtube-logo.png'),
                       QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.youtube_btn.setIcon(icon)
        self.youtube_btn.setIconSize(QtCore.QSize(50, 50))
        self.youtube_btn.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.youtube_btn)
        self.soundcloud_btn = QtWidgets.QPushButton(self.centralwidget)
        self.soundcloud_btn.setText("")
        #TODO progessbar ausprobieren
        #self.progress = QtWidgets.QProgressBar(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap
                        (':/ytdl_resources/soundcloud-logo.png'),
                        QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.soundcloud_btn.setIcon(icon2)
        self.soundcloud_btn.setIconSize(QtCore.QSize(50, 50))
        self.soundcloud_btn.setObjectName("pushButton2")
        self.verticalLayout.addWidget(self.soundcloud_btn)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.start_btn)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setAcceptDrops(True)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText(
            "e.g https://www.youtube.com/watch?v=ExampleLink or https://soundcloud.com/interpret/track")
        self.verticalLayout.addWidget(self.lineEdit)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.statuslabel = QtWidgets.QLabel(self.centralwidget)
        self.statuslabel.setObjectName("statuslabel")
        self.verticalLayout.addWidget(self.statuslabel)
        MainWindow.setCentralWidget(self.centralwidget)

        self.youtube_btn.clicked.connect(self.open_youtube)
        self.soundcloud_btn.clicked.connect(self.open_soundcloud)
        self.start_btn.clicked.connect(self.thread_handler)
        self.lineEdit.returnPressed.connect(self.thread_handler)
        self.lineEdit.textChanged.connect(self.check_state)
        self.lineEdit.textChanged.emit(self.lineEdit.text())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def thread_handler(self):

        try:
            if self.lineEdit.text() != "":
                if self.workerthread.isRunning() is False:
                    self.workerthread.start()
                    # using lambda here because .connect expects a callable function!
                    self.workerthread.sucess_signal.connect(lambda: build_messagebox(QMessageBox.Information, "Your Download and Convertion was successfully finished!", "Success!"))
                else:
                    build_messagebox(QMessageBox.Critical, "\nA Process is already running!\nWait for it to finish!", "Error!")
            else:
                build_messagebox(QMessageBox.Critical, "No Link was found in the text field!", "Error!")
                self.lineEdit.setFocus()
        except Exception as e:
            build_messagebox(QMessageBox.Critical, str(e), "Error!")

    def check_state(self, state):
        reg_ex = QRegExp(
            "(https?://)?(www\.)?youtube\.(com|de)/watch\?v=([-\w])+|(https?://)?(www\.)?youtube\.(com|de)/watch\?v=.*|(https?://)?(www\.)?soundcloud\.(com|de)/(.*)/(.*)")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit)

        self.lineEdit.setValidator(input_validator)
        state = input_validator.validate(self.lineEdit.text(), 0)[0]
        if state == QtGui.QValidator.Acceptable:
            color = '#c4df9b'  # green
        elif state == QtGui.QValidator.Intermediate:
            color = '#fff79a'  # yellow
        else:
            color = '#f6989d'  # red
        self.lineEdit.setStyleSheet('QLineEdit { background-color: %s }' % color)

    def open_youtube(self):
        webbrowser.open('https://youtube.com')

    def open_soundcloud(self):
        webbrowser.open('https://soundcloud.com')

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "YouTube/Soundcloud Downloader by MAS"))
        self.label.setText(_translate("MainWindow", "YouTube/Soundcloud Downloader made by MAS"))
        self.statuslabel.setText(_translate("MainWindow", ""))
        self.youtube_btn.setToolTip(_translate("MainWindow", "Press this button to get to Youtube.com"))
        self.youtube_btn.setStatusTip(_translate("MainWindow", "Press this button to get to Youtube.com"))
        self.soundcloud_btn.setToolTip(_translate("MainWindow", "Press this button to get to Soundcloud.com"))
        self.soundcloud_btn.setStatusTip(_translate("MainWindow", "Press this button to get to Soundcloud.com"))
        self.start_btn.setToolTip(
            _translate("MainWindow", "Press this button to start the download and convertion into .mp3"))
        self.start_btn.setStatusTip(
            _translate("MainWindow", "Press this button to start the download and convertion into .mp3"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.lineEdit.setToolTip(_translate("MainWindow", "Paste your YouTube link  in here."))
        self.lineEdit.setStatusTip(_translate("MainWindow", "Paste your YouTube link  in here."))


class ThreadClass(QThread):

    # creating custom signals
    #exception_signal = pyqtSignal(str)
    sucess_signal = pyqtSignal()

    def __init__(self, parent=None):
        super(ThreadClass, self).__init__(parent)

    def run(self):
        try:

            # Download data and config

            # seems to work with pyinstaller but not in pycharm!
            # ytdl_resources if it should be tested in pycharm!
            #'cachedir': False seems to be required because it could cause a "Unable to download video data: HTTP Error 403: Forbidden" Error
            ffmpeg_loc = resource_path('.\\ffmpeg.exe')

            download_options = {
                'format': 'bestaudio/best',
                'format': 'bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'extractaudio': True,
                'nocheckcertificate': True,
                'prefer_ffmpeg': True,
                'addmetadata': True,
                'cachedir': False,
                'ffmpeg_location': ffmpeg_loc,
                #'ffmpeg location': r'C:\Users\Marty\PycharmProjects\python_youtube_downloader\youtube_downloader\ytdl_resource\ffmpeg.exe',
                'nopart': True,
                #'quiet': True,
                # FFmpegMetadata needs to be used after FFmpegExtractAudio
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '192'
                }, {
                    'key': 'FFmpegMetadata'
                }
                ],

            }

            with youtube_dl.YoutubeDL(download_options) as dl:
                try:
                    youtube_url = ui.lineEdit.text()
                    dl.download([youtube_url])
                    ui.statuslabel.setStyleSheet('color: green')
                    ui.statuslabel.setText("The Download and Convertion to .mp3 is finished!")
                    #https://stackoverflow.com/questions/33304203/pyqt-a-correct-way-to-connect-multiple-signals-to-the-same-function-in-pyqt-qs
                    # wenn man einmal erfolgreich abeschlossen hat kam jedes mal ein popup fenster mit benachrichtigung!
                    self.sucess_signal.emit()
                except Exception as ex:
                    ui.statuslabel.setStyleSheet('color: red')
                    ui.statuslabel.setText(str(ex))
                    #self.exception_signal.emit(str(ex))
        except Exception as e:
            pass

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    #app.aboutToQuit.connect(exitHandler)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())


