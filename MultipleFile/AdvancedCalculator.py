import sys
from PyQt5.QtWidgets import QApplication
from calculator import Calculator

if __name__ == "__main__":
    app = QApplication(sys.argv)
    calculator = Calculator()
    calculator.show()
    sys.exit(app.exec_())
