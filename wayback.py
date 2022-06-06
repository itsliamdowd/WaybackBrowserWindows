import PyQt5
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtCore, QtWidgets, QtGui
import os
import sys
import subprocess

import ctypes
myappid = 'skiingisfun123.waybackbrowser.application'
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
global year
class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()
        self.setWindowIcon(QtGui.QIcon('logo.png'))
        self.setGeometry(0, 0, 400, 300)
        self.show()
        self.setProperty('iconSize', 400)
        self.browser = QWebEngineView()
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "home.html"))
        local_url = QUrl.fromLocalFile(file_path)
        self.browser.setUrl(QUrl(local_url))
        self.setCentralWidget(self.browser)
        self.showMaximized()
        navbar = QToolBar()
        navbar.setIconSize(QtCore.QSize(64, 64))
        navbar.setFixedHeight(75)
        self.addToolBar(navbar)
        prevBtn = QAction('Prev',self)
        prevBtn.triggered.connect(self.browser.back)
        back = QtGui.QIcon('back.png')
        prevBtn.setIcon(back)
        navbar.addAction(prevBtn)
        nextBtn = QAction('Next',self)
        nextBtn.triggered.connect(self.browser.forward)
        navbar.addAction(nextBtn)
        next = QtGui.QIcon('forward.png')
        nextBtn.setIcon(next)
        homeBtn = QAction('Home',self)
        homeBtn.triggered.connect(self.home)
        navbar.addAction(homeBtn)
        home = QtGui.QIcon('home.png')
        homeBtn.setIcon(home)
        refreshBtn = QAction('Refresh',self)
        refreshBtn.triggered.connect(self.browser.reload)
        navbar.addAction(refreshBtn)
        reload = QtGui.QIcon('reload.png')
        refreshBtn.setIcon(reload)
        space = QLabel()
        space.setText("        ")
        navbar.addWidget(space)
        self.dateedit = QtWidgets.QDateEdit(calendarPopup=True)
        navbar.addWidget(self.dateedit)
        print(QtCore.QDateTime.currentDateTime())
        d = QDate(2000, 7, 11)
        self.dateedit.setDate(d)
        self.dateedit.dateChanged.connect(self.onDateChanged)
        location = QLabel()
        location.setText("            Location:     ")
        navbar.addWidget(location)
        self.searchBar = QLineEdit()
        self.searchBar.returnPressed.connect(self.loadUrl)
        navbar.addWidget(self.searchBar)
        self.browser.urlChanged.connect(self.updateUrl)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        connecting = QLabel()
        connecting.setText("  Connecting...")
        self.statusBar.addWidget(connecting)
    def home(self):
        file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "home.html"))
        local_url = QUrl.fromLocalFile(file_path)
        self.browser.setUrl(QUrl(local_url))
    def loadUrl(self):
        print(self.dateedit.dateTime())
        newDate = self.dateedit.dateTime()
        print("The new date is "+newDate.toString())
        print(newDate.toString().split(' ')[3])
        year = str(newDate.toString().split(' ')[3])
        month = str(newDate.toString().split(' ')[1])
        if month == 'Jan':
            month = '01'
        if month == 'Feb':
            month = '02'
        if month == 'Mar':
            month = '03'
        if month == 'Apr':
            month = '04'
        if month == 'May':
            month = '05'
        if month == 'Jun':
            month = '06'
        if month == 'Jul':
            month = '07'
        if month == 'Aug':
            month = '08'
        if month == 'Sep':
            month = '09'
        if month == 'Oct':
            month = '10'
        if month == 'Nov':
            month = '11'
        if month == 'Dec':
            month = '12'
        day = str(newDate.toString().split(' ')[2])
        print(year, month, day)
        urltoload = "http://127.0.0.1:5000/loadpage?url=" + self.searchBar.text() + '&year=' + year + "&month=" + month + "&day=" + day
        self.browser.setUrl(QUrl(urltoload))
    def updateUrl(self, url):
        originalurl = self.searchBar.text()
        self.searchBar.setText(originalurl)
    def onDateChanged(self,newDate):
        print("The new date is "+newDate.toString())
        print(newDate.toString().split(' ')[3])
        year = str(newDate.toString().split(' ')[3])
        month = str(newDate.toString().split(' ')[1])
        if month == 'Jan':
            month = '01'
        if month == 'Feb':
            month = '02'
        if month == 'Mar':
            month = '03'
        if month == 'Apr':
            month = '04'
        if month == 'May':
            month = '05'
        if month == 'Jun':
            month = '06'
        if month == 'Jul':
            month = '07'
        if month == 'Aug':
            month = '08'
        if month == 'Sep':
            month = '09'
        if month == 'Oct':
            month = '10'
        if month == 'Nov':
            month = '11'
        if month == 'Dec':
            month = '12'
        day = str(newDate.toString().split(' ')[2])
        print(year, month, day)
        urlforuse = self.searchBar.text()
        if urlforuse == "":
            urlforuse = "https://google.com"
        urltoload = "http://127.0.0.1:5000/loadpage?url=" + urlforuse + '&year=' + year + '&month=' + month + '&day=' + day
        print(urltoload)
        self.browser.setUrl(QUrl(urltoload))
        #print(newDate)
MyApp = QApplication(sys.argv)
QApplication.setApplicationName('Wayback Browser')
p = subprocess.Popen(['python', 'server.py'])
window = Window()
MyApp.exec_()
