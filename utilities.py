from PyQt6.QtCore import pyqtBoundSignal

def readQSS(file:str):
    """
        Just a simple file reader, nothing special..
    """
    with open(file, "r") as f:
        return f.read()
    
def loadAsset(name:str, kind:str):
    """
        Automatically generates the path
    """
    PATH = f"assets/{kind}/{name}"
    return PATH
    ...
    
def addEventListener(event:pyqtBoundSignal):
    """
        Just a helper utility for making 
        event handling more convenient
    """
    def wrapper(fn): 
        event.connect(fn)
    return wrapper