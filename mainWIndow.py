from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(471, 309)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(0, 0, 471, 51))
        
        # Fonts
        font14 = QtGui.QFont()
        font14.setPointSize(14)
        font15 = QtGui.QFont()
        font15.setPointSize(15)
        font11 = QtGui.QFont()
        font11.setPointSize(11)
        
        # Header Label
        self.title.setFont(font14)
        self.title.setStyleSheet("#title {background-color:grey;color: white;}")
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setObjectName("title")

        # Enumerate Label
        self.enumerate = QtWidgets.QLabel(self.centralwidget)
        self.enumerate.setGeometry(QtCore.QRect(390, 250, 81, 41))
        self.enumerate.setAlignment(QtCore.Qt.AlignCenter)
        self.enumerate.setObjectName("enumerate")

        # Next Button 
        self.nextButton = QtWidgets.QPushButton(self.centralwidget)
        self.nextButton.setGeometry(QtCore.QRect(230, 260, 141, 21))
        self.nextButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.nextButton.setObjectName("nextButton")

        # Stash Button
        self.stashButton = QtWidgets.QPushButton(self.centralwidget)
        self.stashButton.setGeometry(QtCore.QRect(60, 260, 141, 21))
        self.stashButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.stashButton.setObjectName("stashButton")

        # Title Label
        self.titleLabel = QtWidgets.QLabel(self.centralwidget)
        self.titleLabel.setGeometry(QtCore.QRect(20, 60, 151, 21))
        self.titleLabel.setFont(font15)
        self.titleLabel.setObjectName("titleLabel")

        # From Label
        self.fromLabel = QtWidgets.QLabel(self.centralwidget)
        self.fromLabel.setGeometry(QtCore.QRect(20, 90, 151, 31))
        self.fromLabel.setFont(font11)
        self.fromLabel.setObjectName("fromLabel")

        # Text Label
        self.textLabel = QtWidgets.QLabel(self.centralwidget)
        self.textLabel.setGeometry(QtCore.QRect(20, 160, 421, 81))
        self.textLabel.setFont(font11)
        self.textLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.textLabel.setWordWrap(True)
        self.textLabel.setOpenExternalLinks(False)
        self.textLabel.setObjectName("textLabel")

        # Subject  Label
        self.subjectLabel = QtWidgets.QLabel(self.centralwidget)
        self.subjectLabel.setGeometry(QtCore.QRect(20, 120, 151, 31))
        self.subjectLabel.setFont(font11)
        self.subjectLabel.setObjectName("subjectLabel")

        # Line Widget
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(20, 140, 421, 31))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")


        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.title.setText(_translate("MainWindow", "Demo Email reader"))
        self.enumerate.setText(_translate("MainWindow", "1/10"))
        self.nextButton.setText(_translate("MainWindow", "Read Next Email"))
        self.stashButton.setText(_translate("MainWindow", "Stash Email"))
        self.titleLabel.setText(_translate("MainWindow", "Title"))
        self.fromLabel.setText(_translate("MainWindow", "From:"))
        self.textLabel.setText(_translate("MainWindow", "..."))
        self.subjectLabel.setText(_translate("MainWindow", "Subject:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
