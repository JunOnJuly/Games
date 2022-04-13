from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class RangeError(Exception):
    def __str__(self):
        return "올바른 범위의 수를 입력해 주세요"


class NonNumberError(Exception):
    def __str__(self):
        return "숫자를 입력해 주세요"


class Sudoku(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Sudoku')
        self.setWindowIcon(QIcon('rabbit.jpg'))
        self.move(300, 300)
        self.resize(400, 200)
        self.show()