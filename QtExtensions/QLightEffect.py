from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget, QGraphicsBlurEffect
from uuid import uuid4

class QLightEffect(QWidget):
    def __init__(self, color, radius: float, parent=None) -> None:
        super().__init__(parent=parent)
        # self.blrEffect = QGraphicsBlurEffect()
        # self.blrEffect.setBlurRadius(radius)
        # self.setObjectName("QLightEffect")
        self.id = "QWidget#QLightEffect"
        self.setStyleSheet("id { background: INSERT_COLOR }".replace("INSERT_COLOR", color).replace("id", self.id))
        # self.setGraphicsEffect(self.blrEffect)