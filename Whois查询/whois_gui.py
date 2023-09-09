import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QPushButton, QTextEdit
from PyQt5.QtGui import QIcon, QFont, QColor
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
import whois

class WhoisGui(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Whois查询工具')
        self.setGeometry(100, 100, 800, 600)
        self.setWindowIcon(QIcon('icon.png'))

        self.titleLabel = QLabel('Whois查询工具')
        self.titleLabel.setAlignment(Qt.AlignCenter)
        self.titleLabel.setFont(QFont('Arial', 24, QFont.Bold))

        self.domainLabel = QLabel('查询域名：')
        self.domainLineEdit = QLineEdit()
        self.domainLineEdit.setFont(QFont('Arial', 18))

        self.resultTextEdit = QTextEdit()
        self.resultTextEdit.setReadOnly(True)
        self.resultTextEdit.setFont(QFont('Arial', 12))

        self.queryButton = QPushButton('查询')
        self.queryButton.setFont(QFont('Arial', 16))
        self.queryButton.setStyleSheet('QPushButton {background-color: #007acc; color: #ffffff; border-radius: 5px;} QPushButton:hover {background-color: #0061a7;}')
        self.queryButton.clicked.connect(self.queryWhois)

        vbox = QVBoxLayout()
        vbox.addWidget(self.titleLabel)

        hbox = QHBoxLayout()
        hbox.addWidget(self.domainLabel)
        hbox.addWidget(self.domainLineEdit)
        hbox.addWidget(self.queryButton)
        vbox.addLayout(hbox)

        vbox.addWidget(self.resultTextEdit)
        self.setLayout(vbox)

    def queryWhois(self):
        domain = self.domainLineEdit.text()
        w = whois.whois(domain)
        self.resultTextEdit.setText(str(w))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    palette = app.palette()
    palette.setColor(QPalette.Window, QColor('#f0f0f0'))
    palette.setColor(QPalette.WindowText, Qt.black)
    app.setPalette(palette)

    whoisGui = WhoisGui()
    whoisGui.show()
    sys.exit(app.exec_())
