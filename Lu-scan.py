import os
from PyQt5.QtGui import QFont, QPixmap
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QGridLayout

#创建窗口
app = QApplication([])
window = QWidget()
window.setWindowTitle("毕业设计-广西科技大学-网安Q191陆声壮")
window.setFixedSize(800, 600)

#设置窗口背景图片
background = QLabel(window)
pixmap = QPixmap("bg.jpg")
background.setPixmap(pixmap)
background.resize(800, 600)

#设置按钮样式和字体
button_font = QFont("Helvetica", 14)
button_style = """
QPushButton {
background-color: rgba(0, 255, 0, 0.7);
color: black;
border-style: solid;
border-width: 2px;
border-color: white;
border-radius: 10px;
padding: 20px;
font-size: 20px;
}
QPushButton:hover {
background-color: rgba(0, 191, 255, 0.8);
border-color: rgba(255, 255, 255, 0.8);
}
"""

button1 = QPushButton("目录扫描", window)
button1.setStyleSheet(button_style)
button1.setFont(button_font)
button1.clicked.connect(lambda: os.system("python 目录扫描/scanll.py"))

button2 = QPushButton("端口扫描", window)
button2.setStyleSheet(button_style)
button2.setFont(button_font)
button2.clicked.connect(lambda: os.system("python 端口扫描/protscan.py"))

button3 = QPushButton("链接爬虫", window)
button3.setStyleSheet(button_style)
button3.setFont(button_font)
button3.clicked.connect(lambda: os.system("python 链接爬虫/pachong.py"))

button4 = QPushButton("子域名爆破", window)
button4.setStyleSheet(button_style)
button4.setFont(button_font)
button4.clicked.connect(lambda: os.system("python 子域名爆破/ziyuming.py"))

button5 = QPushButton("Fofa查询", window)
button5.setStyleSheet(button_style)
button5.setFont(button_font)
button5.clicked.connect(lambda: os.system("python Fofa查询/FOFA_GUI.py"))

button6 = QPushButton("社工密码", window)
button6.setStyleSheet(button_style)
button6.setFont(button_font)
button6.clicked.connect(lambda: os.system("python 社工密码/mima.py"))

#button7 = QPushButton("历史解析", window)
#button7.setStyleSheet(button_style)
#button7.setFont(button_font)
#button7.clicked.connect(lambda: os.system("python lishi.py"))

button8 = QPushButton("Whois查询", window)
button8.setStyleSheet(button_style)
button8.setFont(button_font)
button8.clicked.connect(lambda: os.system("python Whois查询/whois_gui.py"))

button9 = QPushButton("编码工具", window)
button9.setStyleSheet(button_style)
button9.setFont(button_font)
button9.clicked.connect(lambda: os.system("python 编码工具/zhuanma.py"))

#布局按钮
layout = QGridLayout()
layout.addWidget(button1, 0, 0)
layout.addWidget(button2, 0, 1)
layout.addWidget(button3, 0, 2)
layout.addWidget(button4, 1, 0)
layout.addWidget(button5, 1, 1)
layout.addWidget(button6, 1, 2)
#layout.addWidget(button7, 2, 0)
layout.addWidget(button8, 2, 0)
layout.addWidget(button9, 2, 1)
window.setLayout(layout)

#显示窗口
window.show()
app.exec_()

#like lixin