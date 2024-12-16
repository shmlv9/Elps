import random
import sys
from PyQt6 import uic
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QMainWindow, QApplication


class Square1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.resize(800, 800)
        self.pushButton.clicked.connect(self.paint)
        self.color = QColor('yellow')
        self.do_paint = False

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw(self, qp):
        qp.setBrush(self.color)
        num = random.randint(1, 50)
        qp.drawEllipse(random.randint(30, 350), random.randint(30, 350), 10 * num, 10 * num)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square1()
    ex.show()
    sys.exit(app.exec())