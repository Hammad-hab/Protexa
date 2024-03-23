from PyQt6.QtWidgets import *
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import Qt
from QCustomSpashScreen import QSpashScreen
from QPage import QPage
from _utils import readQSS
import qdarktheme
import sys


class Application(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.__layout_init()
        self.__init()
        self.setStyleSheet(readQSS("styles.css"))
        self.__widget_init()
        self.__main()
        
        
    def __init(self):
        self.setMinimumSize(1000,500)
        self.TOOLBAR = QToolBar()
        self.TOOLBAR.setFixedWidth(self.width()//4)
        self.TOOLBAR.setMovable(False)
        self.addToolBar(Qt.ToolBarArea.LeftToolBarArea, self.TOOLBAR)
        
        SETTINGS = QPushButton("Settings")
        SETTINGS.setObjectName("QToolbarPushButton")
        self.TOOLBAR.addWidget(SETTINGS)
        
        HISTORY = QPushButton("History")
        HISTORY.setObjectName("QToolbarPushButton")
        self.TOOLBAR.addWidget(HISTORY)
        
        RECENTS = QPushButton("Recents")
        RECENTS.setObjectName("QToolbarPushButton")
        self.TOOLBAR.addWidget(RECENTS)

    def __layout_init(self):
        self.central_widget = QWidget()
        self.central_widget.setObjectName("QWindowCentralWidget")
        self.setCentralWidget(self.central_widget)
        
        self.MainLayout = QHBoxLayout()
        self.MainLayout.setContentsMargins(0,0,0,0)
        
        self.tabedWidget = QStackedWidget(self.central_widget)
        self.MainLayout.addWidget(self.tabedWidget, 3)
        self.central_widget.setLayout(self.MainLayout)
        self.setWindowTitle("Protexa")
    
    def __widget_init(self):
        Page = QPage(self)
        Page.setObjectName("SpashScreen")
        Page.useVBoxLayout()
        Page.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        HEADING = QLabel("Welcome to Protexa")
        HEADING.setObjectName("H1")
        INTROTEXT = QLabel("A web-system dedicated to the distribution of encrypted\ninformation such that only authorized personnel who have\nthe specific has, can access the encrypted website.\nehtml (Encrypted Hyper Text Markup Language) websites \ncannot be opened by a regular browser")
        INTROTEXT.setObjectName("INTOTEXT")
        
        LOAD_FILE = QPushButton()
        LOAD_FILE.setObjectName("LoadFile")
        LOAD_FILE.setText("Load .ehtml")
        
        LOAD_URL = QPushButton()
        LOAD_URL.setObjectName("LoadURL")
        LOAD_URL.setText("Open Hosted e-website")
        
        Page.addWidgets(HEADING, INTROTEXT, LOAD_FILE, LOAD_URL)
        self.tabedWidget.addWidget(Page)
        ...     

    def __main(self):
        
        ...
        
    def show(self) -> None:
        self.__spashscreen()
        return super().show()
        
    def __spashscreen(self):
        self.splashScreen = QSpashScreen()
        self.splashScreen.setImage("assets/images/Spashscreen.jpeg")
        heading = QLabel("Protexav0.1.0 beta\nGeneration: CookieJar")
        content = QLabel()
        content.setText(f"Distribute encrypted educational reasorces over the \ninternet securely to actual students and not to Pirates\n\n")
        externalLink = QLabel()
        externalLink.setText("Read tutorial:<br/>       <a href='http://stackoverflow.com/'>Protexa Documentation</a>")
        externalLink.setOpenExternalLinks(True)
        externalLink.setTextFormat(Qt.TextFormat.MarkdownText)
        externalLink.show()
        heading.setObjectName("KapaSheildHeading")
        self.splashScreen.addWidget(heading)
        self.splashScreen.addWidget(content)
        self.splashScreen.addWidget(externalLink)
        heading.setStyleSheet("QLabel#KapaSheildHeading { font-size:15px; font-weight: 500; color: #757474;}")
        self.splashScreen.show()

if __name__ == "__main__":
    qapp = QApplication(sys.argv)
    qdarktheme.setup_theme()
    app = Application()
    app.showMaximized()
    app.show()
    # app.__spashscreen()
    sys.exit(qapp.exec())