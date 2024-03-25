from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtNetwork import QNetworkCookie
import os, json


class QWebBrowser(QWebEngineView):
    COOKIE_PATH = "/usr/local/cookie.list"
    def __init__(self):
        self.cookieStore = self.page().profile().cookieStore()
        self.cookieStore.cookieAdded.connect(self.cookieAdded)
        ...

    def initCookies(self):
        if os.path.isfile(QWebBrowser.COOKIE_PATH):
            with open(QWebBrowser.COOKIE_PATH, "r") as f:
               dict_: dict[str,str] =  json.loads(f.read())
               for key, value in dict_.items():
                   self.cookieStore.setCookie(QNetworkCookie(key, value), self.url())
    
    