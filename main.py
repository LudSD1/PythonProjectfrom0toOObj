import sys

from PySide6.QtWidgets import(
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QVBoxLayout
)
from PySide6.QtCore import Qt


class VentanaPrincipal(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Proyeto Pyhon")
        self.resize(600, 400)

        self.titulo = QLabel("¡Bienvenido a Pyside6!")
        self.titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.boton = QPushButton("Haz clic aqui!!")
        self.boton.clicked.connect(self.mostrar_mensaje)

        self.mensaje = QLabel("La App esta funcionando")
        self.mensaje.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QVBoxLayout(self)
        layout.addWidget(self.titulo)
        layout.addWidget(self.boton)
        layout.addWidget(self.mensaje)

    def mostrar_mensaje(self):
        self.mensaje.setText("Tu primeer boton")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    sys.exit(app.exec())