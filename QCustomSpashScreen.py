from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout, QWidget, QHBoxLayout
from PyQt6.QtGui import QMouseEvent, QPixmap


class QSpashScreen(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.__layout = QVBoxLayout()
        self.setObjectName("QCustomSpashScreen")
        self.setLayout(self.__layout)
        self.setStyleSheet("QDialog#QCustomSpashScreen { border-radius:100px }")
        
    def setImage(self, image:str):
        self.headerImage = QLabel(parent=self)
        image_src = QPixmap(image)
        self.headerImage.setPixmap(image_src)
        self.__layout.addWidget(self.headerImage)
        self.__layout.setContentsMargins(0,0,0,0)
        self.bottomWidget = QWidget(self)
        self.bottomWidgetLayout = QVBoxLayout()
        self.bottomWidget.setLayout(self.bottomWidgetLayout)
        self.bottomWidgetLayout.setContentsMargins(50,10,10,50)
        
        self.__layout.addWidget(self.bottomWidget)
        
    def addWidget(self, widget: QWidget):
        self.bottomWidgetLayout.addWidget(widget)
        
        return
    
    def mouseReleaseEvent(self, a0: QMouseEvent | None) -> None:
        self.close()
        return super().mouseReleaseEvent(a0)
    
    