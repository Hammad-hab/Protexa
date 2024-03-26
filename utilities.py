from PyQt6.QtCore import pyqtBoundSignal

def readQSS(file:str):
    with open(file, "r") as f:
        return f.read()
    
def loadAsset(name:str, kind:str):
    PATH = f"assets/{kind}/{name}"
    return PATH
    ...
    
def addEventListener(event:pyqtBoundSignal):
    def wrapper(fn): 
        event.connect(fn)
    return wrapper