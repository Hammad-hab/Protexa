"""
Deprecated
"""

from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout, QWidget, QLineEdit
from PyQt6.QtCore import Qt

class LoadEWebsiteDialog(QDialog):
    @classmethod
    def create(cls):
        return cls
    """
    A custom Qt dialog shown when the user wants to load an hosted E-HTML website
    """
    QFooterDimensionMargins = (50, 10, 10, 50)
    QSplashScreenImageSize = {"width": 500, "height": 323}

    def __init__(self) -> None:
        super().__init__(None)
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)  # A window with no frame (i.e close buttons etc)
        self.__layout = QVBoxLayout()  # Top-To-Bottom 
        self.setObjectName("QCustomDialog")
        self.setLayout(self.__layout)  # Setting the layout
        self.setStyleSheet("QDialog#QCustomDialog { border-radius:100px }")
        self.__init__widgets()
    
    def addWidget(self, widget: QWidget) -> None:
        # Adds a Widget to the Dialog
        self.__layout.addWidget(widget)
        return
    
    def __init__widgets(self):
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
        
        Content = QLabel("Load an encrypted Website from the internet")
        
        InputURL = QLineEdit()
        InputURL.setPlaceholderText("Enter Website URL...")
        
        self.addWidget(Heading)
        self.addWidget(Content)
        self.addWidget(InputURL)
        ...

    def show(self):
        self.exec()
        super().show()

