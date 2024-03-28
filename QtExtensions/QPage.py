from PyQt6.QtWidgets import QWidget, QVBoxLayout, QFormLayout, QHBoxLayout
from PyQt6.QtCore import Qt


class QPage(QWidget):
    """
        A kind of an abstract class that builds on top 
        of the QWidget and provides additional control
        such as layout, alignment etc
    """
    
    def __init__(self, parent: QWidget | None) -> None:
        super().__init__(parent)
        self._layout = None
        
        
    def useVBoxLayout(self):
        """
            Use vertical alignment
        """
        self._layout = QVBoxLayout()
        self.setLayout(self._layout)
        
    def useFormLayout(self):
        """
            Use FormLayout (see Qt docs: https://doc.qt.io/qtforpython-5/PySide2/QtWidgets/QFormLayout.html)
        """
        self._layout = QFormLayout()
        self.setLayout(self._layout)
        
    def useHBoxLayout(self):
        self._layout = QHBoxLayout()
        self.setLayout(self._layout)
        
    def addWidget(self, widget: QWidget):
        widget.setParent(self)
        self._layout.addWidget(widget)
    
    def setAlignment(self, a0: Qt.AlignmentFlag):
        self._layout.setAlignment(a0)
        
        
    def addWidgets(self, *widgets: list[QWidget]):
        for widget in widgets:
            self.addWidget(widget)