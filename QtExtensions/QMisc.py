from pyqttoast import Toast, ToastPreset, ToastPosition
from PyQt6.QtGui import QFont


def show_toast(preset: ToastPreset, title:str, content:str, *, duration=3000, fontsize=10, bold=True, position=ToastPosition.TOP_RIGHT, parent=None):
    toast = Toast(parent)
    toast.setDuration(duration)  # Hide after 5 seconds
    toast.setTitle(title)
    toast.setText(content)
    toast.applyPreset(preset)  # Apply style preset
    font = QFont()
    font.setPointSize(fontsize)
    font.setBold(bold)

    toast.setTitleFont(font)
    toast.setTextFont(font)
    toast.show()
    toast.setPosition(position)
    