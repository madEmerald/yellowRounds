import sys
import random
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        qp.setBrush(QColor(r, g, b))

        for i in range(3):
            for j in range(3):
                r = random.randint(5, 20)
                qp.drawEllipse(75 * i + 40 - r, 75 * j + 40 - r, r * 2, r * 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
