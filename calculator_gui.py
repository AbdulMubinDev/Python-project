#All imports
from sympy import sympify
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QVBoxLayout, QPushButton, QGridLayout, QHBoxLayout, QLabel, QLineEdit, QWidget

#creating major parts
app = QApplication([])
main_window = QWidget()
main_window.setWindowTitle("Calculator App")
main_window.resize(300, 400)


def button_clicked():
    button = app.sender()
    text =  button.text()

    if text == "=":
        symbol = text_box.text()
        try: 
            exp = sympify(symbol)
            value = exp.evalf()
            res = f"{value:.2f}".rstrip('0').rstrip('.')
            text_box.setText(str(res))
        except Exception as e:
            text_box.setText("Error")
    elif text == "clear":
        text_box.clear()
    elif text == "del":
        curr_input = text_box.text()
        if curr_input == "Error":
            text_box.clear()
        else:
            text_box.setText(curr_input[:-1])
    elif text.isdigit:
        curr_input = text_box.text()
        if curr_input == '0':
            text_box.setText(text)
        else:
            text_box.setText(curr_input + text)
    else:
        curr_input = text_box.text()
        text_box.setText(curr_input + text)


#ready to assemble
text_box = QLineEdit()
grid = QGridLayout()
buttons = ["7", "8", "9", "/", "4", "5", "6", "*", "1", "2", "3", "-", "0", ".", "=", "+"]
clear = QPushButton("clear")
clear.clicked.connect(button_clicked)
delete = QPushButton("del")
delete.clicked.connect(button_clicked)

col = 0 
row = 0

for text in buttons:
    button = QPushButton(text)
    button.clicked.connect(button_clicked)
    grid.addWidget(button, row, col)
    col += 1

    if col > 3:
        col = 0 
        row +=1


#Assembling
master_layout = QVBoxLayout()
master_layout.addWidget(text_box)
master_layout.addLayout(grid)

button_row = QHBoxLayout()
button_row.addWidget(clear)
button_row.addWidget(delete)


#Decorate
master_layout.addLayout(button_row)
main_window.setLayout(master_layout)

#Burger
main_window.show()
app.exec_()
