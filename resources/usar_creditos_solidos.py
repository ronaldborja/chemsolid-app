import sys
from PySide6 import QtCore as qtc
from PySide6 import QtWidgets as qtw
from PySide6 import QtGui as qtq
import sympy as sp

from creditos.creditos_solido import Ui_Form


class Form(qtw.QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app = qtw.QApplication(sys.argv)

    window = Form()
    window.open()
    sys.exit(app.exec())
    
