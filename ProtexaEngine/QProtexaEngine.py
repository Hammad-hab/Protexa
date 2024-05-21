from PyQt6.QtWidgets import QWidget
from ..QtExtensions.QPage import QPage
from PyQt6.QtWebEngineWidgets import QWebEngineView


class ProtexaEngine(QPage):
    def __init__(self, parent: QWidget | None) -> None:
        super().__init__(parent)
        