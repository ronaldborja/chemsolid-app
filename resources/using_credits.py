import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtq
import sympy as sp
from PySide6.QtCore import Qt
from creditos.credits import Ui_Dialog


class creditos_solidos2(qtw.QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        #self.setAttribute(Qt.WA_TranslucentBackground)
        #self.widget.setStyleSheet("background-color: red;")
        self.closed.clicked.connect(self.close)


if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    form = creditos_solidos2()
    form.open()
    sys.exit(app.exec())