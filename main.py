import random
import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.circle_button = QtWidgets.QPushButton(self.centralwidget)
        self.circle_button.setGeometry(QtCore.QRect(300, 80, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.circle_button.setFont(font)
        self.circle_button.setStyleSheet("border-radius: 3px;\n"
                                         "background-color: #A7A916;\n"
                                         "color: white;")
        self.circle_button.setObjectName("circle_button")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.circle_button.setText(_translate("MainWindow", "НАЖМИ МЕНЯ"))


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Кружочки 2')
        self.circle_button.clicked.connect(self.run)
        self.is_paint = False

    def run(self):
        self.is_paint = True
        self.update()

    def paintEvent(self, event) -> None:
        qp = QPainter()
        qp.begin(self)
        self.draw_random_ellipses(qp)
        qp.end()

    def draw_random_ellipses(self, qp):
        try:
            if self.is_paint:
                print('asdasd')
                r, g, b, a = [random.randint(0, 255) for _ in range(4)]
                qp.setBrush(QColor(r, g, b, a))
                radius = random.randint(50, 200)
                x, y = random.randint(0, 600), random.randint(0, 600)
                qp.drawEllipse(x, y, radius, radius)
                self.is_paint = False
        except Exception as e:
            print(e.__repr__())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec())
