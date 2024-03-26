from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import  QLineEdit, QWidget
from PyQt6.QtCore import QUrl
from QtExtensions.QPage import QPage


class QBrowser(QPage):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        
        self.useVBoxLayout()
        self.SearchBox = QLineEdit()
        self.SearchBox.setPlaceholderText('Enter Search term or URL')
        self.SearchBox.returnPressed.connect(lambda *args: self.searchTerm(self.SearchBox.text()))
        
        self.BlinkEngine =  QWebEngineView()
        self.BlinkEngine.setContentsMargins(0,0,0,0)
        self.BlinkEngine.setUrl(QUrl("https://www.google.com"))
        
        self.addWidgets(self.SearchBox, self.BlinkEngine)
        
    def searchTerm(self, string:str):
            if not string:
                return
            if string.startswith("www."):
                URL = "https://" + string
            elif string.startswith("https://"):
                URL = string
            else:
                URL = f"https://www.google.com/search?q={string}"
            self.BlinkEngine.setUrl(QUrl(URL))
            self.BlinkEngine.page().profile().cookieStore()
            self.SearchBox.clearFocus()
    