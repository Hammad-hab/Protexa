from PyQt6.QtGui import QIcon, QMouseEvent
from PyQt6.QtWidgets import QWidget, QStackedWidget, QPushButton, QLayout, QToolButton
from ..QPage import QPage
from .QBrowser import QBrowser
import qtawesome as qta

class QTab(QPushButton):
    QZeroMargins = (0,0,0,0) # No Margins
    """
        An implementation of the QPushButton that acts like a chromium tab
    """
    def __init__(self, title:str="New Tab", MAX_WIDTH=0):
        super().__init__()
        self.title: str = title
        self.selected: bool = False
        self.BrowserInstance: QBrowser = QBrowser() # See QBrowser.py
        self.dblclick = lambda : 0 # OnDoubleClick Event
        self.index = 0
        # Initalization functions
        self.staticStyles = ""
        self.setStyleSheet("background-color:none;") # Setting the background color
        self.setTitle(title)
        self.setMaximumWidth(MAX_WIDTH)
        self.setObjectName("QTab") # Setting the name of the object
        self.setContentsMargins(*QTab.QZeroMargins) # No Margins for the Button
        self.BrowserInstance.setContentsMargins(*QTab.QZeroMargins) # No Margins for the Browser
        self.BrowserInstance._layout.setContentsMargins(*QTab.QZeroMargins) # No Margins for the Browser's Layout
        self.BrowserInstance.PageRenderer.loadFinished.connect(self.onDoneLoading)
        self.BrowserInstance.PageRenderer.loadProgress.connect(self.onPageLoad)
        self.PageIsLoading = False
    
    def setStyleSheet(self, styleSheet: str | None) -> None:
        styleSheet += self.staticStyles
        return super().setStyleSheet(styleSheet)
    
    def mouseDoubleClickEvent(self, a0: QMouseEvent | None) -> None:
        self.dblclick()
        return super().mouseDoubleClickEvent(a0)
    
    def setTitle(self, title:str):
        """A thin wrapper over the setText method"""
        self.setText("  " + title)
    
    def onDoneLoading(self, connection_status:bool):
        self.BrowserInstance.urlLoadError(connection_status)
        if connection_status:
            self.BrowserInstance.PageRenderer.iconChanged.connect(self.setIcon)
        else:
            self.setIcon(None)
        self.PageIsLoading = False
       
    def setIcon(self, icon: QIcon) -> None:
        if not icon:
            Icon = qta.icon('fa5s.wrench', color='grey')
            return super().setIcon(Icon)
        else:
            return super().setIcon(icon)
            
    
    def onPageLoad(self):
        if not self.PageIsLoading:
            animation = qta.Spin(self, autostart=True, step=10)
            spin_icon = qta.icon('mdi.loading', color='grey', animation=animation)
            self.setIcon(spin_icon)
            self.PageIsLoading = True
    
class QWebKitBrowserUI(QPage):
    def __init__(self, parent: QWidget | None = None) -> None:
        super().__init__(parent)
        self.useVBoxLayout()
        self._layout.setContentsMargins(*QTab.QZeroMargins)
        self.tabsArea = QPage(self)
        self.tabsArea.useHBoxLayout()
        self.insertionIndex = 0
        self.tabsArea._layout.setSizeConstraint(QLayout.SizeConstraint.SetMaximumSize)
        self.tabsArea.setContentsMargins(*QTab.QZeroMargins)
        self.tabsArea._layout.setContentsMargins(10,10,10,0)
        self.tabs: list[QTab] = []
        
        newTabButton = QToolButton()
        newTabButton.clicked.connect(self.addTab)
        newTabButton.setText("\uFF0B") # A rather slim yet large Plus sign
        
        self.tabsArea.addWidget(newTabButton)
        self.selectedTab = None
        
        self.tabingArea = QStackedWidget(self)
        self.tabingArea.setContentsMargins(*QTab.QZeroMargins)
        self.tabingArea.setStyleSheet("background-color: rgb(54,54,54)")
        self.tabsArea.setStyleSheet("background: rgb(54,54,54)")
        
        self.setStyleSheet("background-color: rgb(54,54,54)")
        self.addWidgets(self.tabsArea, self.tabingArea)         
        self.addTab()
        
    
    def addTab(self):
        TAB = QTab("New tab", self.width()//3)
        TAB.BrowserInstance.onFullScreen = lambda : self.tabsArea.hide()
        TAB.BrowserInstance.onFullScreenExit = lambda : self.tabsArea.show()
        TAB.BrowserInstance.PageRenderer.urlChanged.connect(lambda : TAB.setTitle(TAB.BrowserInstance.PageRenderer.page().title()))
        TAB.BrowserInstance.onSearch = lambda : TAB.setText(TAB.BrowserInstance.PageRenderer.page().title())
        TAB.dblclick = lambda : self.removeTab(TAB)
        self.tabingArea.addWidget(TAB.BrowserInstance)
        self.tabsArea.addWidget(TAB)
        TAB.index = int(self.insertionIndex)
        # RELOAD_ICON = qta.icon("fa5s.redo")
            
            
        # TAB.BrowserInstance.PageRenderer.loadProgress.connect(loadPage)
        # TAB.BrowserInstance.PageRenderer.load.connect(loadPage)
        def select(*args):
            if self.selectedTab:
                self.selectedTab.setStyleSheet("background-color:none;")
            self.tabingArea.setCurrentIndex(TAB.index)
            self.selectedTab = TAB
            TAB.setStyleSheet("background-color:rgb(54,54,54);")
            
        TAB.clicked.connect(select) 
        select()
        self.tabs.append(TAB)
        self.insertionIndex += 1
        
    def removeTab(self, TAB: QTab):
        if TAB is None:
            raise TypeError("Expected TAB to be an instance of QtExtensions.QTab, not NoneType")
        if self.insertionIndex - 1 > 0:
            self.tabingArea.removeWidget(TAB.BrowserInstance)
            TAB.BrowserInstance.deleteLater()
            self.tabsArea._layout.removeWidget(TAB)
            TAB.setParent(None)
            if self.insertionIndex < 0:
                self.insertionIndex = 0
            else:
                self.insertionIndex -= 1 
            # current_index = self.tabingArea.currentIndex() - 1
            # if current_index == 0:
            #     self.tabingArea.setCurrentIndex(current_index + 1)
            # elif current_index >= (self.insertionIndex - 1):
            #     self.tabingArea.setCurrentIndex(current_index - 1)
            # else:
            #     self.tabingArea.setCurrentIndex(current_index - 1)`
            self.tabs.pop(TAB.index)
            for tab in self.tabs:
                tab.index = tab.index - 1 if tab.index > 0 else 0
        else:
            self.addTab()
            self.removeTab(TAB)
        
        TAB = None
        