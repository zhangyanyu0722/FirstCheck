# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FirstCheck.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#

import sys

from PyQt5 import QtCore, QtGui, QtWidgets

# Creating the GUI
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(542, 370)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.disasterLabel = QtWidgets.QLabel(self.centralwidget)
        self.disasterLabel.setObjectName("disasterLabel")
        self.gridLayout.addWidget(self.disasterLabel, 0, 0, 1, 1)
        self.locationLabel = QtWidgets.QLabel(self.centralwidget)
        self.locationLabel.setObjectName("locationLabel")
        self.gridLayout.addWidget(self.locationLabel, 2, 0, 1, 1)
        self.runButton = QtWidgets.QPushButton(self.centralwidget)
        self.runButton.setObjectName("runButton")
        self.gridLayout.addWidget(self.runButton, 4, 0, 1, 1)
        self.locationEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.locationEntry.setObjectName("locationEntry")
        self.gridLayout.addWidget(self.locationEntry, 3, 0, 1, 1)
        self.checkBoxArea = QtWidgets.QScrollArea(self.centralwidget)
        self.checkBoxArea.setWidgetResizable(True)
        self.checkBoxArea.setObjectName("checkBoxArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 522, 216))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.earthquakeBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.earthquakeBox.setObjectName("earthquakeBox")
        self.gridLayout_2.addWidget(self.earthquakeBox, 0, 0, 1, 1)
        self.floodBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.floodBox.setObjectName("floodBox")
        self.gridLayout_2.addWidget(self.floodBox, 1, 0, 1, 1)
        self.hurricaneBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.hurricaneBox.setObjectName("hurricaneBox")
        self.gridLayout_2.addWidget(self.hurricaneBox, 2, 0, 1, 1)
        self.checkBox = QtWidgets.QCheckBox(self.scrollAreaWidgetContents)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 3, 0, 1, 1)
        self.checkBoxArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.checkBoxArea, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 542, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
      
        self.runButton.clicked.connect(self.run_tweets)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "First Check"))
        self.disasterLabel.setText(_translate("MainWindow", "Choose a Disaster (Pick one)"))
        self.locationLabel.setText(_translate("MainWindow", "Enter a Location"))
        self.runButton.setText(_translate("MainWindow", "Check Tweets"))
        self.earthquakeBox.setText(_translate("MainWindow", "Earthquake"))
        self.floodBox.setText(_translate("MainWindow", "Flood"))
        self.hurricaneBox.setText(_translate("MainWindow", "Hurricane"))
        self.checkBox.setText(_translate("MainWindow", "Tornado"))

    #calling the API functions.
    def run_tweets(self):
      if self.earthquakeBox.check() == True:

      else if self.hurricaneBox.check() == True:

      else if self.floodBox.check() == True:

      else if self.checkBox.check() == True:



    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
