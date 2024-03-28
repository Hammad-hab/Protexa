"""
File implements the QSplashScreen class which is a customized dialog box.
The default splash screen from Qt is quite underwhelming
"""

from PyQt6.QtWidgets import QDialog, QLabel, QVBoxLayout, QWidget
from PyQt6.QtGui import QMouseEvent, QPixmap
from PyQt6.QtCore import Qt

class QCustomSplashScreen(QDialog):
    """
    A custom Qt splash screen shown when the browser starts
    """
    QFooterDimensionMargins = (50, 10, 10, 50)
    QSplashScreenImageSize = {"width": 500, "height": 323}

    def __init__(self) -> None:
        super().__init__()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)  # A window with no frame (i.e close buttons etc)
        self.__layout = QVBoxLayout()  # Top-To-Bottom 
        self.setObjectName("QCustomSpashScreen")
        self.setLayout(self.__layout)  # Setting the layout
        self.setStyleSheet("QDialog#QCustomSpashScreen { border-radius:100px }")
        self.__layout.setContentsMargins(0, 0, 0, 0)  # Prevent weird gaps around the edges of the layout

    def setImage(self, image: str) -> None:
        """
        Sets the image of the splash screen (a kind similar to the one blender has)
        """
        self.headerImage = QLabel(parent=self)  # Header
        image_src = QPixmap(image).scaled(
            QCustomSplashScreen.QSplashScreenImageSize["width"],  # Dimensions of the Image (See above)
            QCustomSplashScreen.QSplashScreenImageSize["height"],  # Dimensions of the Image (See above)
            Qt.AspectRatioMode.KeepAspectRatio,  # Ensure that the aspect ratio stays the same
            Qt.TransformationMode.SmoothTransformation  # Ensure that the pixel's don't get stretched out
        )
        self.headerImage.setPixmap(image_src)  # The header (Setting the actual image)
        self.__layout.addWidget(self.headerImage)  # Added the image to the dialog (Appears at the top)

        self.bottomWidget = QWidget(self)  # Footer
        self.bottomWidgetLayout = QVBoxLayout()  # Text will appear like a list (Top to Bottom)
        self.bottomWidget.setLayout(self.bottomWidgetLayout)  # Setting the layout defined above

        self.bottomWidgetLayout.setContentsMargins(*QCustomSplashScreen.QFooterDimensionMargins)  # Defined above
        self.__layout.addWidget(self.bottomWidget)  # Adding the footer to the layout. It will appear at the bottom

    def addWidget(self, widget: QWidget) -> None:
        # Adds a Widget to the Footer
        self.bottomWidgetLayout.addWidget(widget)
        return

    def mouseReleaseEvent(self, a0: QMouseEvent | None) -> None:
        # Overrides the default mouseReleaseEvent
        self.close()  # Closing the Splashscreen on click
        return super().mouseReleaseEvent(a0)
