from QtExtensions.QBrowserWidgets.QBrowserPage import QWebKitBrowserUI
from QtExtensions.QCustomSpashScreen import QCustomSplashScreen
from QtExtensions.QMisc import show_toast, ToastPreset
from utilities import readQSS, addEventListener
from QtExtensions.QPage import QPage
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import info as appinfo


class Application(QMainWindow):
        
	def __init__(self) -> None:
		# Initializing Base Application
		super().__init__()
		print("PROTEXA_LOG: instatiated base app class ")
		self.__main__layout__init()
		print("PROTEXA_LOG: initialized Layout")
  
		self.__init()
  
		self.setStyleSheet(readQSS("qss/styles.css"))
		self.__main__init()


	def __init(self):
		""" Initialises the base layout (mainly sidebar and window size)"""
		self.setMinimumSize(*appinfo.WINDOW_DIMENSIONS)  # Set the size of the window
  
  
		self.SIDEBAR = QToolBar()
		self.SIDEBAR.setFixedWidth(self.width()//4)
		self.SIDEBAR.setMovable(False)
		self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.SIDEBAR)
		HOME = QPushButton("Home")
		HOME.setObjectName("QToolbarPushButton")
		self.SIDEBAR.addWidget(HOME)

		SETTINGS = QPushButton("Settings")
		SETTINGS.setObjectName("QToolbarPushButton")
		self.SIDEBAR.addWidget(SETTINGS)

		HISTORY = QPushButton("History")
		HISTORY.setObjectName("QToolbarPushButton")
		self.SIDEBAR.addWidget(HISTORY)

		RECENTS = QPushButton("Recents")
		RECENTS.setObjectName("QToolbarPushButton")
		self.SIDEBAR.addWidget(RECENTS)

		@addEventListener(HOME.clicked)
		def changeTabHome():
			self.tabedWidget.setCurrentIndex(0)

	def __main__layout__init(self):
		"""Initializes the main layout of the central widget"""
		self.central_widget = QWidget()
		self.central_widget.setObjectName("QWindowCentralWidget")
		self.setCentralWidget(self.central_widget)

		self.MainLayout = QHBoxLayout()
		self.MainLayout.setContentsMargins(0,0,0,0)

		self.tabedWidget = QStackedWidget(self.central_widget)
		self.tabedWidget.setContentsMargins(0,0,0,0)
		self.MainLayout.addWidget(self.tabedWidget, 3)
		self.central_widget.setLayout(self.MainLayout)

		self.setWindowTitle("Protexa")

	def __main__init(self):
		HomePage, BrowserPage, OpenEHTMLPage = self.__init__tabs()
		"""
  			This method does the following things:

				(1) Init Splashscreen (Alignment Text et cetera)

				(2) Add content to the main page (Inserts Buttons and event handlers)

  		"""
		
		HEADING = QLabel(appinfo.PROTEXA_MAIN_HEADING)
		HEADING.setObjectName("H1")
		INTROTEXT = QLabel(appinfo.PROTEXA_MAIN_CONTENT)
		INTROTEXT.setObjectName("INTOTEXT")

		LOAD_FILE = QPushButton()
		LOAD_FILE.setObjectName("LoadFile")
		LOAD_FILE.setText("Load .ehtml")

		LOAD_URL = QPushButton()
		LOAD_URL.setObjectName("LoadURL")
		LOAD_URL.setText("Open Hosted e-website")

		RUN_STD_BROWSER = QPushButton()
		RUN_STD_BROWSER.setObjectName("RunBrowser")
		RUN_STD_BROWSER.setText("Browser (PageRenderer Chromium)")
		RUN_STD_BROWSER.setDisabled(True)

		HomePage.addWidgets(HEADING, INTROTEXT, LOAD_FILE, LOAD_URL, RUN_STD_BROWSER)
		
        
		@addEventListener(RUN_STD_BROWSER.clicked)
		def startBrowser():
			# Executed when the browser is opened
			show_toast(ToastPreset.WARNING, 
              'Protexa Usage Warning (Consumer Edition)', 
              'Protexa Browser is quite scratchy and is NOT for everyday consumer use!',
              parent=self
              )
			self.tabedWidget.setCurrentIndex(1)
			self.SIDEBAR.hide()

	
		@addEventListener(LOAD_URL.clicked)
		def showFileDialog():
			self.tabedWidget.setCurrentIndex(2)
		... 
	def __init__tabs(self):
		HomePage = QPage(self)
		HomePage.setObjectName("SpashScreen")
		HomePage.useVBoxLayout()
		HomePage.setAlignment(Qt.AlignmentFlag.AlignCenter)
	
		BrowserPage = QWebKitBrowserUI()
  
		OpenEHTMLPage = QPage(self)
		OpenEHTMLPage.useVBoxLayout()
		OpenEHTMLPage.setAlignment(Qt.AlignmentFlag.AlignTop)
		OpenEHTMLPage.setContentsMargins(100, 50, 100, 0)
		self.__init_ehtmlPage(OpenEHTMLPage)
  
		self.tabedWidget.addWidget(HomePage)
		self.tabedWidget.addWidget(BrowserPage)
		self.tabedWidget.addWidget(OpenEHTMLPage)
  
		return (HomePage, BrowserPage, OpenEHTMLPage)

	def __init_ehtmlPage(self, Page: QPage):
		Heading = QLabel("Open E-HTML Website")
		Heading.setAlignment(Qt.AlignmentFlag.AlignLeft)
		Heading.setObjectName("H1")
		Heading.setStyleSheet(""" 
            font-size: 20px;
            border: 10px double white;
            border-right: none;
            border-left: none;
            border-top: none;
            padding-bottom: 10px;
        """)
        
		Content = QLabel(Page, text=appinfo.OPENEHTML_INSTRUCTIONS)
		Content.setWordWrap(True)
		Content.setStyleSheet("font-size: 14px")
  
		InputURL = QLineEdit()
		InputURL.setPlaceholderText("Enter Website URL...")
  
		Page.addWidgets(Heading, Content, InputURL)

	def show(self) -> None:
		"""Starts the application by displaying the window and the splash screen"""
		self.__show__splashscreen()
		return super().show()

	def __show__splashscreen(self):
		"""Inits and displays the splash screen"""
		self.splashScreen = QCustomSplashScreen()
		self.splashScreen.setImage(appinfo.SPLASHSCREEN_IMAGE)
		heading = QLabel(f"Protexa {appinfo.PROTEXA_VERSION} {appinfo.PROTEXA_RELEASE_KIND}\nGeneration: {appinfo.PROTEXA_GEN}")
		content = QLabel()
		content.setText(appinfo.PROTEXA_APP_DESCRIPTION)

		externalLink = QLabel()
		externalLink.setObjectName("Hyperlink")
		externalLink.setText(appinfo.PROTEXA_EXTERNAL_DOCUMENTATION_LINK)
		externalLink.setOpenExternalLinks(True)
		externalLink.setTextFormat(Qt.TextFormat.MarkdownText)
		externalLink.show()

		heading.setObjectName("ProtexaHeading")
		self.splashScreen.addWidget(heading)
		self.splashScreen.addWidget(content)
		self.splashScreen.addWidget(externalLink)
		heading.setStyleSheet("QLabel#ProtexaHeading{ font-size:15px; font-weight: 500; color: #757474;}")
		self.splashScreen.show()


