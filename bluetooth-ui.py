#Created By: Juan Carlos Guerra Velez
#Repo: https://github.com/Code-jc/bluetooth-ui
from PyQt5.QtWidgets import( QApplication, QWidget, QVBoxLayout, QLabel, QGridLayout, QGraphicsDropShadowEffect)
from PyQt5.QtGui import QPainter, QColor, QLinearGradient, QFont, QPixmap
from PyQt5.QtCore import Qt
import sys

devices = [
    {"name": "Audífonos", "icon": "headphones.png"},
    {"name": "Teléfonos", "icon": "smartphone.png"},
    {"name": "Vocinas", "icon": "speaker.png"},
    {"name": "Teclado", "icon": "Keyboard.png"}
]

class GlassUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dispositivos Bluetooth Conectados")
        self.setGeometry(300, 100, 600, 700)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.initUI()

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#0f2027"))
        gradient.setColorAt(0.5, QColor("#2c5364"))
        gradient.setColorAt(1.0, QColor("#4b1248"))
        painter.setBrush(gradient)
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.rect())

    def initUI(self):
        layout =QVBoxLayout()
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(20)
        title = QLabel("Dispositivos Bluetooth Conectados")
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: white; font-size: 28px; font-weight: bold;")        
        layout.addWidget(title)

        grid = QGridLayout()
        grid.setSpacing(20) 

        for i, device in enumerate(devices):
            grid.addWidget(self.deviceCard(device["name"], device["icon"]), i // 2, i % 2)   
        layout.addLayout(grid)
        self.setLayout(layout)

    def deviceCard(self, name, icon_path):
        card = QWidget()
        card.setFixedSize(220, 200)
        card.setStyleSheet("background-color: rgba(255, 255, 255, 0.15); border-radius: 20px;")
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(30)
        shadow.setOffset(0, 0)
        shadow.setColor(QColor(0, 0, 0, 120))
        card.setGraphicsEffect(shadow)

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignCenter)

        icon =QLabel()
        pixmap = QPixmap(icon_path).scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon.setPixmap(pixmap)
        vbox.addWidget(icon)

        label = QLabel(name)
        label.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        vbox.addWidget(label)

        status = QLabel("Conectado")
        status.setStyleSheet("color: lightgray; font-size: 14px;")                
        vbox.addWidget(status)

        card.setLayout(vbox)
        return card
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    glass_ui = GlassUI()
    glass_ui.show()
    sys.exit(app.exec_())
