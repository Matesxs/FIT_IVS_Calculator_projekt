from app_ui import Ui_Calculator
from PyQt5 import QtWidgets, QtCore
from mathLib.entry_point import interpret_text_input

class CalculatorApp(QtWidgets.QMainWindow, Ui_Calculator):
  def __init__(self):
    super().__init__()
    self.setStyleSheet('QWidget {font: "Roboto Mono"}')

    self.setupUi(self)
    self.show()

    self.button_number_zero.clicked.connect(self.button_pressed)
    self.button_number_one.clicked.connect(self.button_pressed)
    self.button_number_two.clicked.connect(self.button_pressed)
    self.button_number_three.clicked.connect(self.button_pressed)
    self.button_number_four.clicked.connect(self.button_pressed)
    self.button_number_five.clicked.connect(self.button_pressed)
    self.button_number_six.clicked.connect(self.button_pressed)
    self.button_number_seven.clicked.connect(self.button_pressed)
    self.button_number_eight.clicked.connect(self.button_pressed)
    self.button_number_nine.clicked.connect(self.button_pressed)

    self.button_equal.clicked.connect(self.solve_input)
    self.button_del.clicked.connect(self.erase)
    self.button_c.clicked.connect(self.erase_last)
    self.button_factorial.clicked.connect(self.factorial_pressed)
    self.button_ln.clicked.connect(self.ln_pressed)
    self.abs_button.clicked.connect(self.abs_pressed)
    self.ten_power_button.clicked.connect(self.ten_power_pressed)
    self.e_power_button.clicked.connect(self.e_power_pressed)
    self.button_root.clicked.connect(self.root_pressed)

    self.button_plus.clicked.connect(self.button_pressed)
    self.button_minus.clicked.connect(self.button_pressed)
    self.button_multiply.clicked.connect(self.button_pressed)
    self.button_division.clicked.connect(self.button_pressed)
    self.button_power.clicked.connect(self.button_pressed)
    self.button_lbrac.clicked.connect(self.button_pressed)
    self.button_rbrac.clicked.connect(self.button_pressed)
    self.button_dot.clicked.connect(self.button_pressed)
    self.button_rand.clicked.connect(self.button_pressed)
    self.e_button.clicked.connect(self.button_pressed)

  def erase(self):
    self.input.setText("")
    self.input.setFocus()

  def erase_last(self):
    start_pos = self.input.cursorPosition()
    if start_pos > 0:
      start_string = self.input.text()
      self.input.setText(start_string[:start_pos - 1] + start_string[start_pos:])
      self.input.setFocus()
      self.input.setCursorPosition(start_pos-1)

  def solve_input(self):
    if self.input.text() == "Error":
      self.erase()

    self.input.setText(interpret_text_input(self.input.text()))

  def write_to_input(self, value):
    start_pos = self.input.cursorPosition()
    self.input.setText(self.input.text()[0:start_pos] + value + self.input.text()[start_pos:])
    self.input.setFocus()
    self.input.setCursorPosition(start_pos + len(value))

  def button_pressed(self):
    button = self.sender()
    if self.input.text() == "Error":
      self.erase()
    self.write_to_input(button.text())


  def factorial_pressed(self):
    if self.input.text() == "Error":
      self.erase()

    self.write_to_input("fact(")

  def ln_pressed(self):
    if self.input.text() == "Error":
      self.erase()

    self.write_to_input("ln(")

  def abs_pressed(self):
    if self.input.text() == "Error":
      self.erase()

    self.write_to_input("abs(")

  def ten_power_pressed(self):
    if self.input.text() == "Error":
      self.erase()

    self.write_to_input("10^")

  def e_power_pressed(self):
    if self.input.text() == "Error":
      self.erase()
    self.write_to_input("e^")

  def root_pressed(self):
    if self.input.text() == "Error":
      self.erase()
    self.write_to_input("√")

  def keyPressEvent(self, event):
    if event.key() == QtCore.Qt.Key_Enter or event.key() == QtCore.Qt.Key_Return:
      self.solve_input()

    if event.key() == QtCore.Qt.Key_Escape:
      self.close()