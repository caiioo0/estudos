import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class BrowserWindow(QMainWindow):
    def __init__(self):
        super(BrowserWindow, self).__init__()

        self.setWindowTitle("Navegador Web Simples")
        self.setGeometry(100, 100, 800, 600)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://www.google.com"))

        self.setCentralWidget(self.browser)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BrowserWindow()
    window.show()

    sys.exit(app.exec_())
