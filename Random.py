import sys

from PyQt5.QtGui import QPainter, QColor
from ui_file import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import randint


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btnOK.clicked.connect(self.run)
        self.flag = False

    def paintEvent(self, e):
        if not self.flag:
            return
        qp = QPainter(self)
        qp.begin(self)
        for i in range(randint(1, 10)):
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            qp.setPen(QColor(r, g, b))
            qp.setBrush(QColor(r, g, b))
            x = randint(0, 300)
            y = randint(0, 300)
            r = randint(10, 300)
            qp.drawEllipse(x, y, r, r)
        qp.end()

    def run(self):
        self.flag = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())