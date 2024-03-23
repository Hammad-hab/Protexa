from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import Qt


class QPage(QWidget):
    def __init__(self, parent: QWidget | None) -> None:
        super().__init__(parent)
        self._layout = None
        
        
    def useVBoxLayout(self):
        self._layout = QVBoxLayout()
        self.setLayout(self._layout)
        
    def useHBoxLayout(self):
        self._layout = QVBoxLayout()
        self.setLayout(self._layout)
        
    def addWidget(self, widget: QWidget):
        widget.setParent(self)
        self._layout.addWidget(widget)
    
    def setAlignment(self, a0: Qt.AlignmentFlag):
        self._layout.setAlignment(a0)
        
        
    def addWidgets(self, *widgets: list[QWidget]):
        for widget in widgets:
            self.addWidget(widget)