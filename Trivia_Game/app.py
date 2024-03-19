#GUI imports
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
#function imports
from functions import frame1, frame2, frame3, frame4, grid


#initiallize GUI application
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Trivia Game")
window.setFixedWidth(1000)
window.setStyleSheet("background: #161219;")


frame2()

window.setLayout(grid)

window.show()
sys.exit(app.exec())