# All imports
from sympy import sympify
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QGridLayout, QHBoxLayout, QLineEdit, QWidget


class CalculatorApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator App")
        self.resize(300, 400)

        self.text_box = QLineEdit()
        self.text_box.setFont(QFont("Helvetica", 32)) 
        self.text_box.setStyleSheet("color: white; background-color: #222831; padding: 10px;")  

        self.create_buttons()
        self.setup_layout()

    def create_buttons(self):
        self.grid = QGridLayout()
        self.buttons = [
            "7", "8", "9", "/", 
            "4", "5", "6", "*", 
            "1", "2", "3", "-", 
            "0", ".", "=", "+"
        ]

        self.clear_btn = QPushButton("clear")
        self.clear_btn.setStyleSheet("QPushButton {font: 25px serif; padding:10px; background-color: #FFA673; color: #000000}")
        self.clear_btn.clicked.connect(self.button_clicked)

        self.delete_btn = QPushButton("del")
        self.delete_btn.setStyleSheet("QPushButton {font: 25px serif; padding:10px; background-color: #FFA673; color: #000000}")
        self.delete_btn.clicked.connect(self.button_clicked)

        col = 0 
        row = 0

        for text in self.buttons:
            button = QPushButton(text)  
            button.setStyleSheet("QPushButton {font: 25px serif; padding:10px; background-color: #FFA673; color: #000000}")
            button.clicked.connect(self.button_clicked)
            self.grid.addWidget(button, row, col)
            col += 1

            if col > 3:
                col = 0 
                row += 1

    def button_clicked(self):
        button = self.sender()
        text = button.text()

        if text == "=":
            symbol = self.text_box.text()
            try: 
                exp = sympify(symbol)
                value = exp.evalf()
                res = f"{value:.2f}".rstrip('0').rstrip('.')
                self.text_box.setText(str(res))
            except Exception as e:
                self.text_box.setText("Error")

        elif text == "clear":
            self.text_box.clear()

        elif text == "del":
            curr_input = self.text_box.text()
            if curr_input == "Error":
                self.text_box.clear()
            else:
                self.text_box.setText(curr_input[:-1])

        elif text.isdigit():  
            curr_input = self.text_box.text()
            if curr_input == '0':
                self.text_box.setText(text)
            else:
                self.text_box.setText(curr_input + text)

        else:
            curr_input = self.text_box.text()
            self.text_box.setText(curr_input + text)

    def setup_layout(self):
        # Assembling
        master_layout = QVBoxLayout()
        master_layout.addWidget(self.text_box)
        master_layout.addLayout(self.grid)

        button_row = QHBoxLayout()
        button_row.addWidget(self.clear_btn)
        button_row.addWidget(self.delete_btn)

        # Decorate
        master_layout.addLayout(button_row)
        master_layout.setContentsMargins(25, 25, 25, 25)
        self.setLayout(master_layout)

if __name__ == '__main__':
    app = QApplication([])
    window = CalculatorApp()
    window.setStyleSheet("QWidget {background-color: #222831}")
    window.show()
    app.exec_()
