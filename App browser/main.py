from ctypes import alignment
import sys,os
import pickle 	

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *
#                                 Web Browser (HTML Frame)
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from os.path import expanduser, join


class Window(QMainWindow):
	

	def __init__(self, *args, **kwargs):
		super(Window, self).__init__(*args, **kwargs)
		self.browser = QWebEngineView()
		self.browser.setUrl(QUrl('http://10.0.0.2/'))
		self.browser.urlChanged.connect(self.update_AddressBar)
		self.setCentralWidget(self.browser)
		
	# setting status bar:
		self.status_bar = QStatusBar()
		self.setStatusBar(self.status_bar)

	# # setting nav bar :
	# 	self.navigation_bar = QToolBar('Navigation Toolbar')
	# 	self.addToolBar(self.navigation_bar)

	# # setting edit bar:	
	# 	self.edit_bar = QToolBar('edit bar')
	# 	self.addToolBar(self.edit_bar)


		
	

		
	# # back button:

	# 	back_button = QAction("", self)
	# 	back_button.setStatusTip('Go to previous page you visited')
	# 	back_button.triggered.connect(self.browser.back)
	# 	back_button.setIcon(QIcon('left.png'))
	# 	self.navigation_bar.addAction(back_button)
		
	# # next button:

	# 	next_button = QAction('', self)
	# 	next_button.setStatusTip('Go to next page')
	# 	next_button.triggered.connect(self.browser.forward)
	# 	next_button.setIcon(QIcon('next1.png'))
	# 	self.navigation_bar.addAction(next_button)

	# # refresh button:

	# 	refresh_button = QAction("", self)
	# 	refresh_button.setStatusTip('Refresh this page')
	# 	refresh_button.triggered.connect(self.browser.reload)
	# 	refresh_button.setIcon(QIcon('refresh.png'))
	# 	self.navigation_bar.addAction(refresh_button)
		
	# # home button:

	# 	home_button = QAction("Home", self)
	# 	home_button.setStatusTip('Go to home page (Google page)')
	# 	home_button.triggered.connect(self.go_to_home)
	# 	home_button.setIcon(QIcon('home.png'))
	# 	self.navigation_bar.addAction(home_button)
		
	# # search button:

	# 	search_button = QAction(" ", self)
	# 	search_button.triggered.connect(self.Enter_Url)
	# 	search_button.setIcon(QIcon('search.png'))
	# 	self.edit_bar.addAction(search_button)

	# # bookmark button:

	# 	book_btn =QAction('',self)
	# 	book_btn.setIcon(QIcon('bookmark.png'))
	# 	self.edit_bar.addAction(book_btn)
		

	# # minimize button:

	# 	minimize_button = QAction("", self)
	# 	minimize_button.setStatusTip('Minimize this page')
	# 	minimize_button.triggered.connect(self.browser.hide)
	# 	minimize_button.setIcon(QIcon('min.png'))
	# 	self.edit_bar.addAction(minimize_button)

	# # maximize button:

	# 	maximize_button = QAction("", self)
	# 	maximize_button.setStatusTip('Maximize this page')
	# 	maximize_button.triggered.connect(self.browser.show)
	# 	maximize_button.setIcon(QIcon('max.png'))	
	# 	self.edit_bar.addAction(maximize_button)

	# # close button :

	# 	close_button = QAction("", self)
	# 	close_button.setStatusTip('close the browser')
	# 	close_button.triggered.connect(self.close)
	# 	close_button.setIcon(QIcon('close.png'))
	# 	self.edit_bar.addAction(close_button)

		

		
		# self.navigation_bar.addSeparator()
		# self.edit_bar.addSeparator()

		self.browser.maximumSize()
		self.showMaximized()


		

			

		

		# Adding another toolbar which contains the bookmarks
		# bookmarks_toolbar = QToolBar('Bookmarks', self)
		# self.addToolBar(bookmarks_toolbar)

		# pythongeeks = QAction("PythonGeeks", self)
		# pythongeeks.setStatusTip("Go to PythonGeeks website")
		# pythongeeks.triggered.connect(lambda: self.go_to_URL(QUrl("https://pythongeeks.org")))
		# bookmarks_toolbar.addAction(pythongeeks)

		# facebook = QAction("Facebook", self)
		# facebook.setStatusTip("Go to Facebook")
		# facebook.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.facebook.com")))
		# bookmarks_toolbar.addAction(facebook)

		# linkedin = QAction("LinkedIn", self)
		# linkedin.setStatusTip("Go to LinkedIn")
		# linkedin.triggered.connect(lambda: self.go_to_URL(QUrl("https://in.linkedin.com")))
		# bookmarks_toolbar.addAction(linkedin)

		# instagram = QAction("Instagram", self)
		# instagram.setStatusTip("Go to Instagram")
		# instagram.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.instagram.com")))
		# bookmarks_toolbar.addAction(instagram)

		# twitter = QAction("Twitter", self)
		# twitter.setStatusTip('Go to Twitter')
		# twitter.triggered.connect(lambda: self.go_to_URL(QUrl("https://www.twitter.com")))
		# bookmarks_toolbar.addAction(twitter)
		
# defining things:

	def go_to_home(self):
		self.browser.setUrl(QUrl('http://10.0.0.2/vms/'))

	def go_to_URL(self, url: QUrl):
		if url.scheme() == '':
			url.setScheme('https://')
		self.browser.setUrl(url)
		self.update_AddressBar(url)

	def update_AddressBar(self, url):
		self.URLBar.setText(url.toString())
		self.URLBar.setCursorPosition(0)
		
	def Enter_Url(self):	
		self.URLBar = QLineEdit()
		self.URLBar.returnPressed.connect(lambda: self.go_to_URL(QUrl(self.URLBar.text())))  # This specifies what to do when enter is pressed in the Entry field
		self.navigation_bar.addWidget(self.URLBar)
  

		self.addToolBarBreak()




app = QApplication(sys.argv)
app.setApplicationName('COSAI')

window = Window()
app.exec_()

# url = self.URLBar.text()
# 		self.browser.setUrl(QUrl(url))