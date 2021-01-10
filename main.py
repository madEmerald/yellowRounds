import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.draw = False
        self.pushButton.clicked.connect(self.rounds)

    def rounds(self):
        self.draw = True
        self.repaint()

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            self.draw_rounds(qp)
            qp.end()
        self.draw = False

    def draw_rounds(self, qp):
        qp.setBrush(QColor(255, 255, 0))

        for i in range(3):
            for j in range(3):
                r = random.randint(5, 20)
                qp.drawEllipse(75 * i + 40 - r, 75 * j + 40 - r, r * 2, r * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
