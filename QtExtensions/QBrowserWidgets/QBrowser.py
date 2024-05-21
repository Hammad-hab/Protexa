from PyQt6.QtWebEngineCore import QWebEngineSettings, QWebEngineFullScreenRequest
from PyQt6.QtWidgets import  QLineEdit, QWidget, QToolButton, QHBoxLayout
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtCore import QUrl, Qt
from .QPagePresets import ProtexaNetworkError
from ..QPage import QPage 
import qtawesome as qta
import asyncio 

class QUrlBar(QLineEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        
    def focusInEvent(self, a0) -> None:
        self.selectAll()
        return super().focusInEvent(a0)
    


class QBrowser(QPage):
    DEFAULT_PAGE = QUrl("https://www.google.com")
    SEARCH_BOX_PLACEHOLDER = 'Enter Search term or URL'
    
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)

        self.useVBoxLayout() # Using QVBoxLayout (See QPage.py)
        self._layout.setContentsMargins(0,0,0,0) # Removing spaces from around the widget
        self.ActionBar = QWidget(self) # The part where the URL bar and the bookmarks etc are
        self.ActionBar.setContentsMargins(0,0,0,0)
        ActionBarLayout = QHBoxLayout() # Layout
        self.ActionBar.setLayout(ActionBarLayout)
        
        ActionBarLayout.setSizeConstraint(QHBoxLayout.SizeConstraint.SetMinimumSize) # height: fit-contents
        ActionBarLayout.setContentsMargins(10,5,10,0) 
        
        self.SearchBox = QUrlBar(self.ActionBar) # The URL bar
        self.SearchBox.setPlaceholderText(QBrowser.SEARCH_BOX_PLACEHOLDER) # Setting the placeholder
        self.SearchBox.returnPressed.connect(lambda *args: asyncio.run(self.searchTerm(self.SearchBox.text())))
        
        self.PageRenderer = QWebEngineView() # The Webpage renderer (PageRenderer from chromium)
        self.PageRenderer.setUrl(QBrowser.DEFAULT_PAGE,) # Setting the default page
        self.PageRenderer.setContentsMargins(0,0,0,0) # Removing spacing
        
        self.ReloadButton = QToolButton()
        self.ReloadButton.setObjectName("ReloadTab")
        self.onTriggerReload = lambda : 0
        
        RELOAD_ICON = qta.icon("fa5s.redo")
        self.ReloadButton.setIcon(RELOAD_ICON)
        self.ReloadButton.clicked.connect(self.reload)
        self.ReloadButton.setStyleSheet("""
            QToolButton#ReloadTab {
                border-radius: 13px;
            }
            QToolButton#ReloadTab:hover { 
                background-color: #606060;
               
            }
        """)
        ActionBarLayout.addWidget(self.ReloadButton)
        ActionBarLayout.addWidget(self.SearchBox)
        self.ActionBar.setMaximumHeight(self.SearchBox.height())
        
        self.addWidgets(self.ActionBar, self.PageRenderer) # Adding the page
        self.onSearch = lambda: 0 # A hook for search functionality
        self.onFullScreen = lambda : 0
        self.onFullScreenExit = lambda : 0
        self.URL = ""
        # Setting the settings
        SETTINGS = self.PageRenderer.settings()
        SETTINGS.setAttribute(QWebEngineSettings.WebAttribute.AllowGeolocationOnInsecureOrigins, False)         
        SETTINGS.setAttribute(QWebEngineSettings.WebAttribute.FullScreenSupportEnabled, True)
        SETTINGS.setAttribute(QWebEngineSettings.WebAttribute.AutoLoadIconsForPage, True)         
        SETTINGS.setAttribute(QWebEngineSettings.WebAttribute.JavascriptEnabled, True)
        SETTINGS.setAttribute(QWebEngineSettings.WebAttribute.AutoLoadImages, True)         
        SETTINGS.setAttribute(QWebEngineSettings.WebAttribute.WebGLEnabled, True)
        
        self.PageRenderer.page().fullScreenRequested.connect(lambda *args: asyncio.run(self.goFullScreen(*args)))
        self.PageRenderer.page().urlChanged.connect(self.pageChanged)
        self.PageRenderer.page().loadFinished.connect(self.urlLoadError)
        
        self.status = "OK"
        
    def urlLoadError(self, connection_status:bool):
        if not connection_status:
            self.SearchBox.setText(self.URL)
            self.PageRenderer.setHtml(ProtexaNetworkError)
            self.status = "ERR"
        else:
            self.status = "OK"
        
    async def goFullScreen(self, event: QWebEngineFullScreenRequest):
        if event.toggleOn():
            event.accept()
            self.PageRenderer.showFullScreen()
            self.ActionBar.hide()
            self.onFullScreen()
        else :
            self.PageRenderer.showNormal()
            event.accept()
            self.ActionBar.show()
            self.onFullScreenExit()
            
    
    def pageChanged(self):
        
        if self.status == "OK":
            self.SearchBox.setText(self.PageRenderer.url().toString())
            self.URL = self.PageRenderer.url().toString()
        else:
            self.SearchBox.setText(self.URL)
        
    async def searchTerm(self, term:str) -> None:
        """
            Search for pages/stuff on the default search engine
        """
        if not self.status == "OK":
            return
        
        # URL Preprocessing
        if not term:
            # If string is None, exit but raise an error
            raise TypeError("Unexpected type of argument \"term\". Expected str, got NoneType")
        if term.startswith("www."):
            # Term is a URL but doesn't have the protocol
            URL = "https://" + term
        elif term.startswith("https://"):
            # Term is a complete URL
            URL = term
        else:
            # Term is not a url, therefore use the default search engine
            URL = f"https://www.google.com/search?q={term}"
        
        # Setting the URL
        self.PageRenderer.setUrl(QUrl(URL))
        self.SearchBox.clearFocus() # Removing focus from the search box
        self.onSearch() # Calling the hook
        self.URL = URL
        self.pageChanged()
        
    def reload(self):
        self.onTriggerReload()
        self.PageRenderer.setUrl(QUrl(self.SearchBox.text()))
        self.PageRenderer.reload()