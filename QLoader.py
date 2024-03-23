from PyQt6.QtWidgets import QLabel, QWidget, QVBoxLayout
from PyQt6.QtGui import QMovie
from PyQt6.QtCore import Qt


class QLoader(QLabel):
    def __init__(self, gif_path:str) -> None:
        super().__init__()
        self.animation_path = gif_path
        self.target_movie = QMovie(self.animation_path)
        self.layout_ = QVBoxLayout()
        self.setLayout(self.layout_)
        self.setMovie(self.target_movie)
    
    def startLoading(self):
        self.target_movie.start()

    def addLabel(self, text):
        labelBottom = QLabel(parent=self)
        labelBottom.setAlignment(Qt.AlignmentFlag.AlignHCenter | Qt.AlignmentFlag.AlignBottom)
        labelBottom.setText(text)
        self.layout_.addWidget(labelBottom)
        return labelBottom