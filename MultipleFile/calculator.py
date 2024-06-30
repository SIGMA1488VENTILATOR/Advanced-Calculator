# calculator.py
from PyQt5.QtWidgets import QMainWindow, QVBoxLayout, QLineEdit, QPushButton, QWidget, QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt
from button_handler import handle_button_click

class Calculator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Advanced Calculator")
        self.setGeometry(100, 100, 300, 400)

        self.centralWidget = QWidget(self)
        self.setCentralWidget(self.centralWidget)

        self.gridLayout = QGridLayout()
        self.centralWidget.setLayout(self.gridLayout)

        self.resultDisplay = QLineEdit()
        self.resultDisplay.setReadOnly(True)
        self.resultDisplay.setAlignment(Qt.AlignRight)
        self.resultDisplay.setFixedHeight(50)
        self.gridLayout.addWidget(self.resultDisplay, 0, 0, 1, 4)

        buttons = [
            ("7", 1, 0),
            ("8", 1, 1),
            ("9", 1, 2),
            ("/", 1, 3),
            ("4", 2, 0),
            ("5", 2, 1),
            ("6", 2, 2),
            ("*", 2, 3),
            ("1", 3, 0),
            ("2", 3, 1),
            ("3", 3, 2),
            ("-", 3, 3),
            ("0", 4, 0),
            (".", 4, 1),
            ("+", 4, 2),
            ("=", 4, 3),
            ("C", 5, 0, 1, 4),
        ]

        for btnText, row, col, *span in buttons:
            button = QPushButton(btnText)
            button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            button.clicked.connect(lambda checked, btnText=btnText: handle_button_click(self, btnText))
            if span:
                self.gridLayout.addWidget(button, row, col, *span)
            else:
                self.gridLayout.addWidget(button, row, col)

        self.current_expression = ""
