from PySide6.QtWidgets import QApplication, QMainWindow, QMenu, QAction, QLabel
from PySide6.QtCore import Qt, QMimeData
from PySide6.QtGui import QIcon, QDrag

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Arrastrar y soltar")
        self.setGeometry(100, 100, 300, 200)

        # Crear el menú con los íconos
        menu = QMenu(self)
        icon1 = QIcon("icon1.png")  # Reemplaza "icon1.png" con la ruta de tu propio icono
        icon2 = QIcon("icon2.png")  # Reemplaza "icon2.png" con la ruta de tu propio icono
        action1 = QAction(icon1, "Icono 1", self)
        action2 = QAction(icon2, "Icono 2", self)
        menu.addAction(action1)
        menu.addAction(action2)

        # Conectar las acciones a un slot para iniciar el arrastre
        action1.triggered.connect(lambda: self.startDrag(action1.icon()))
        action2.triggered.connect(lambda: self.startDrag(action2.icon()))

        # Establecer el menú como menú contextual de la ventana
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(lambda pos: menu.exec_(self.mapToGlobal(pos)))

        # Crear la etiqueta donde se colocarán los íconos arrastrados
        self.label = QLabel(self)
        self.label.setGeometry(50, 50, 100, 100)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setAcceptDrops(True)

    def startDrag(self, icon):
        # Iniciar el arrastre de un ícono
        drag = QDrag(self)
        mime_data = QMimeData()
        mime_data.setImageData(icon.pixmap(64).toImage())
        drag.setMimeData(mime_data)
        drag.exec_()

    def dragEnterEvent(self, event):
        # Habilitar el evento de arrastre
        if event.mimeData().hasImage():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        # Manejar el evento de soltar el ícono
        if event.mimeData().hasImage():
            self.label.setPixmap(event.mimeData().imageData().scaled(64, 64))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
