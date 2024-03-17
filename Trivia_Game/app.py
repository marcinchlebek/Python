#GUI imports
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QCursor
#function imports
#from functions import frame1, frame2, frame3, frame4, grid

#initiallize GUI application
app = QApplication(sys.argv)

window = QWidget()
window.setWindowTitle("Trivia Game")
window.setFixedWidth(1000)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()

#display Logo
image = QPixmap("trivia.png")
logo = QLabel()
logo.setPixmap(image)
logo.setAlignment(QtCore.Qt.AlignCenter) 
logo.setStyleSheet("margin-top: 100px;")

grid.addWidget(logo, 0, 0)

window.setLayout(grid)

window.show()
sys.exit(app.exec())