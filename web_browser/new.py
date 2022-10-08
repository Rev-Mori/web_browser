
from cgitb import text
import sys



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
  
		with open('test.txt', 'r') as f:
			lines = f.readlines()
			self.book_url = lines[0]
		
		
		self.browser.setUrl(QUrl(self.book_url))
		self.browser.urlChanged.connect(self.book_addressbar)
		
		self.setCentralWidget(self.browser)
		
	# setting status bar:
		self.status_bar = QStatusBar()
		self.setStatusBar(self.status_bar)

	# setting nav bar :
		self.navigation_bar = QToolBar('Navigation Toolbar')
		self.addToolBar(self.navigation_bar)

	
		


		
	

		
	# back button:

		back_button = QAction("", self)
		back_button.setStatusTip('Go to previous page you visited')
		back_button.triggered.connect(self.browser.back)
		back_button.setIcon(QIcon('left.png'))
		self.navigation_bar.addAction(back_button)
		
	# next button:

		next_button = QAction('', self)
		next_button.setStatusTip('Go to next page')
		next_button.triggered.connect(self.browser.forward)
		next_button.setIcon(QIcon('next1.png'))
		self.navigation_bar.addAction(next_button)

	# refresh button:

		refresh_button = QAction("", self)
		refresh_button.setStatusTip('Refresh this page')
		refresh_button.triggered.connect(self.browser.reload)
		refresh_button.setIcon(QIcon('refresh.png'))
		self.navigation_bar.addAction(refresh_button)
		
	# home button:

		home_button = QAction("Home", self)
		home_button.setStatusTip('Go to home page (Google page)')
		home_button.triggered.connect(self.go_to_home)
		home_button.setIcon(QIcon('home.png'))
		self.navigation_bar.addAction(home_button)
		
	
   
 
		self.URLBar = QLineEdit()
		self.URLBar.returnPressed.connect(lambda: self.go_to_URL(self.URLBar.text()))  # This specifies what to do when enter is pressed in the Entry field
		self.navigation_bar.addWidget(self.URLBar)
		
  
	# bookmark button:

		book_btn =QAction('',self)
		book_btn.setIcon(QIcon('bookmark.png'))
		book_btn.triggered.connect(self.update_home)
		self.navigation_bar.addAction(book_btn)

	# minimize button:

		minimize_button = QAction("", self)
		minimize_button.setStatusTip('Minimize this page')
		minimize_button.triggered.connect(self.showMinimized)
		minimize_button.setIcon(QIcon('min.png'))
		self.navigation_bar.addAction(minimize_button)

	# maximize button:

		maximize_button = QAction("", self)
		maximize_button.setStatusTip('Minimize this page')
		maximize_button.triggered.connect(self.showMaximized)
		maximize_button.setIcon(QIcon('max.png'))	
		self.navigation_bar.addAction(maximize_button)

	# close button :

		close_button = QAction("", self)
		close_button.setStatusTip('close the browser')
		close_button.triggered.connect(self.close)
		close_button.setIcon(QIcon('close.png'))
		self.navigation_bar.addAction(close_button)

		

		
		self.navigation_bar.addSeparator()
		# self.edit_bar.addSeparator()

		self.browser.maximumSize()
		self.showFullScreen()


		

			

		

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
	



	def go_to_URL(self, url):
		
		if not url.startswith("http"):
			url = "http://"+url
		
            
 
    
    
    
		self.URLBar.setText(url)
		self.browser.setUrl(QUrl(url))
        
        
		self.update_AddressBar(QUrl(url))
  

	def update_AddressBar(self, url):
		self.URLBar.setText(url.toString())
	
	def book_addressbar(self,book_url):
		self.URLBar.setText(book_url.toString())
	
	def go_to_home(self):
		with open('test.txt', 'r') as f:
			lines = f.readlines()
			self.book_url = lines[0]
			print(self.book_url)
			self.browser.setUrl(QUrl(self.book_url))
	
 # saving the url in txt file .	
  
	def update_home(self,book_url):
		self.book_url=self.URLBar.text()
		
			
		
  
		self.dict = self.book_url
		f= open('test.txt','w')
		f.write(str(self.dict))
	
		
		

		self.addToolBarBreak()




app = QApplication(sys.argv)
app.setApplicationName('COSAI Web Browser')

window = Window()
app.exec_()

# http://10.0.0.2/