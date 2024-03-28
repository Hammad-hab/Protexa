from QtExtensions.QBrowserWidgets.QBrowserPage import QWebKitBrowserUI
from QtExtensions.QCustomSpashScreen import QCustomSplashScreen
from QtExtensions.QMisc import show_toast, ToastPreset
from utilities import readQSS, addEventListener
from QtExtensions.QPage import QPage
from PyQt6.QtWidgets import *
from PyQt6.QtCore import Qt
import info as appinfo
import qdarktheme
import sys


class Application(QMainWindow):
	def __init__(self) -> None:
		super().__init__()
		self.__layout_init()
		self.__init()
		self.setStyleSheet(readQSS("qss/styles.css"))
		self.__widget_init()


	def __init(self):
		self.setMinimumSize(1000,500)
		self.TOOLBAR = QToolBar()
		self.TOOLBAR.setFixedWidth(self.width()//4)
		self.TOOLBAR.setMovable(False)
		self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.TOOLBAR)
		HOME = QPushButton("Home")
		HOME.setObjectName("QToolbarPushButton")
		self.TOOLBAR.addWidget(HOME)

		SETTINGS = QPushButton("Settings")
		SETTINGS.setObjectName("QToolbarPushButton")
		self.TOOLBAR.addWidget(SETTINGS)

		HISTORY = QPushButton("History")
		HISTORY.setObjectName("QToolbarPushButton")
		self.TOOLBAR.addWidget(HISTORY)

		RECENTS = QPushButton("Recents")
		RECENTS.setObjectName("QToolbarPushButton")
		self.TOOLBAR.addWidget(RECENTS)

		@addEventListener(HOME.clicked)
		def changeTabHome():
			self.tabedWidget.setCurrentIndex(0)

	def __layout_init(self):
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

	def __widget_init(self):
		HomePage = QPage(self)
		HomePage.setObjectName("SpashScreen")
		HomePage.useVBoxLayout()
		HomePage.setAlignment(Qt.AlignmentFlag.AlignCenter)

		HEADING = QLabel(appinfo.PROTEXA_MAIN_HEADING)
		HEADING.setObjectName("H1")
		INTROTEXT = QLabel("A web-system dedicated to the distribution of encrypted\ninformation such that only authorized personnel who have\nthe specific has, can access the encrypted website.\nehtml (Encrypted Hyper Text Markup Language) websites \ncannot be opened by a regular browser")
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

		HomePage.addWidgets(HEADING, INTROTEXT, LOAD_FILE, LOAD_URL, RUN_STD_BROWSER)
		self.tabedWidget.addWidget(HomePage)
        
		@addEventListener(RUN_STD_BROWSER.clicked)
		def startBrowser():
			show_toast(ToastPreset.WARNING, 
              'Protexa Usage Warning (Consumer Edition)', 
              'Protexa Browser is quite scratchy and is NOT for everyday consumer use!',
              parent=self
              )
			self.tabedWidget.setCurrentIndex(1)
			self.TOOLBAR.hide()


		BrowserPage = QWebKitBrowserUI()
		self.tabedWidget.addWidget(BrowserPage)
		... 

	def show(self) -> None:
		self.__spashscreen()
		return super().show()

	def __spashscreen(self):
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

		heading.setObjectName("KapaSheildHeading")
		self.splashScreen.addWidget(heading)
		self.splashScreen.addWidget(content)
		self.splashScreen.addWidget(externalLink)
		heading.setStyleSheet("QLabel#KapaSheildHeading { font-size:15px; font-weight: 500; color: #757474;}")
		self.splashScreen.show()


def exec_app():
	qapp = QApplication(sys.argv)
	qdarktheme.setup_theme()
	app = Application()
	app.showMaximized()
	app.show()
	sys.exit(qapp.exec())

if __name__ == "__main__":
	exec_app()
