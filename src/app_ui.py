from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QFont


class Ui_Calculator(object):
  def setupUi(self, MainWindow):
    MainWindow.setObjectName("MainWindow")
    MainWindow.setEnabled(True)

    MainWindow.resize(361, 381)
    MainWindow.setMinimumSize(QtCore.QSize(361, 381))
    MainWindow.setMaximumSize(QtCore.QSize(361, 381))

    MainWindow.setWindowTitle("Calculator")

    self.centralWidget = QtWidgets.QWidget(MainWindow)
    self.centralWidget.setObjectName("centralWidget")
    self.centralWidget.setWindowTitle("Calculator")

    self.button_number_zero = QtWidgets.QPushButton(self.centralWidget)
    self.button_number_zero.setGeometry(QtCore.QRect(0, 320, 121, 61))
    self.button_number_zero.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                          "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                          "stop: 0 #f0f0f0, stop: 1 #e3e3e3); }")
    self.button_number_zero.setObjectName("button_number_zero")
    self.button_number_zero.setText("0")
    self.button_number_zero.setFont(QFont("Swis721 Ex BT", 12))

    self.button_number_one = QtWidgets.QPushButton(self.centralWidget)
    self.button_number_one.setGeometry(QtCore.QRect(0, 260, 61, 61))
    self.button_number_one.setToolTipDuration(0)
    self.button_number_one.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed "
                                         "{ background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                         "stop: 0 #f0f0f0, stop: 1 #e3e3e3); }")
    self.button_number_one.setObjectName("button_number_one")
    self.button_number_one.setText("1")
    self.button_number_one.setFont(QFont("Swis721 Ex BT", 12))

    self.button_number_two = QtWidgets.QPushButton(self.centralWidget)
    self.button_number_two.setGeometry(QtCore.QRect(60, 260, 61, 61))
    self.button_number_two.setToolTipDuration(0)
    self.button_number_two.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                         "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                         "stop: 0 #f0f0f0, stop: 1 #e3e3e3); }")
    self.button_number_two.setObjectName("button_number_two")
    self.button_number_two.setText("2")
    self.button_number_two.setFont(QFont("Swis721 Ex BT", 12))

    self.button_number_three = QtWidgets.QPushButton(self.centralWidget)
    self.button_number_three.setGeometry(QtCore.QRect(120, 260, 61, 61))
    self.button_number_three.setToolTipDuration(0)
    self.button_number_three.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                           "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                           "stop: 0 #f0f0f0, stop: 1 #e3e3e3); }")
    self.button_number_three.setObjectName("button_number_three")
    self.button_number_three.setText("3")
    self.button_number_three.setFont(QFont("Swis721 Ex BT", 12))

    self.button_number_four = QtWidgets.QPushButton(self.centralWidget)
    self.button_number_four.setGeometry(QtCore.QRect(0, 200, 61, 61))
    self.button_number_four.setToolTipDuration(0)
    self.button_number_four.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                          "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                          "stop: 0 #f0f0f0, stop: 1 #e3e3e3); }")
    self.button_number_four.setObjectName("button_number_four")
    self.button_number_four.setText("4")
    self.button_number_four.setFont(QFont("Swis721 Ex BT", 12))

    self.button_number_five = QtWidgets.QPushButton(self.centralWidget)
    self.button_number_five.setGeometry(QtCore.QRect(60, 200, 61, 61))
    self.button_number_five.setToolTipDuration(0)
    self.button_number_five.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                          "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                          "stop: 0 #f0f0f0, stop: 1 #e3e3e3); }")
    self.button_number_five.setObjectName("button_number_five")
    self.button_number_five.setText("5")
    self.button_number_five.setFont(QFont("Swis721 Ex BT", 12))

    self.button_number_six = QtWidgets.QPushButton(self.centralWidget)
    self.button_number_six.setGeometry(QtCore.QRect(120, 200, 61, 61))
    self.button_number_six.setToolTipDuration(0)
    self.button_number_six.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                         "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                         "stop: 0 #f0f0f0, stop: 1 #e3e3e3); }")
    self.button_number_six.setObjectName("button_number_six")
    self.button_number_six.setText("6")
    self.button_number_six.setFont(QFont("Swis721 Ex BT", 12))

    self.button_number_seven = QtWidgets.QPushButton(self.centralWidget)
    self.button_number_seven.setGeometry(QtCore.QRect(0, 140, 61, 61))
    self.button_number_seven.setToolTipDuration(0)
    self.button_number_seven.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                           "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                           "stop: 0 #f0f0f0, stop: 1 #e3e3e3); }")
    self.button_number_seven.setObjectName("button_number_seven")
    self.button_number_seven.setText("7")
    self.button_number_seven.setFont(QFont("Swis721 Ex BT", 12))

    self.button_number_eight = QtWidgets.QPushButton(self.centralWidget)
    self.button_number_eight.setGeometry(QtCore.QRect(60, 140, 61, 61))
    self.button_number_eight.setToolTipDuration(0)
    self.button_number_eight.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                           "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                           "stop: 0 #f0f0f0, stop: 1 #e3e3e3); }")
    self.button_number_eight.setObjectName("button_number_eight")
    self.button_number_eight.setText("8")
    self.button_number_eight.setFont(QFont("Swis721 Ex BT", 12))

    self.button_number_nine = QtWidgets.QPushButton(self.centralWidget)
    self.button_number_nine.setGeometry(QtCore.QRect(120, 140, 61, 61))
    self.button_number_nine.setToolTipDuration(0)
    self.button_number_nine.setStyleSheet("QPushButton { border: 1px solid gray; } QPushButton:pressed { "
                                          "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                          "stop: 0 #f0f0f0, stop: 1 #e3e3e3); }")
    self.button_number_nine.setObjectName("button_number_nine")
    self.button_number_nine.setText("9")
    self.button_number_nine.setFont(QFont("Swis721 Ex BT", 12))

    self.button_del = QtWidgets.QPushButton(self.centralWidget)
    self.button_del.setGeometry(QtCore.QRect(0, 80, 61, 61))
    self.button_del.setToolTipDuration(0)
    self.button_del.setStyleSheet("QPushButton { background-color: rgb(214, 214, 214); border: 1px solid gray;} "
                                  "QPushButton:pressed { background-color: qlineargradient(x1: 0, y1: 0, x2: 0, "
                                  "y2: 1, stop: 0 #c9c9c9, stop: 1 #c7c7c7); }\n")
    self.button_del.setIconSize(QtCore.QSize(16, 16))
    self.button_del.setObjectName("button_del")
    self.button_del.setText("DEL")
    self.button_del.setFont(QFont("Swis721 Ex BT", 12))

    self.button_c = QtWidgets.QPushButton(self.centralWidget)
    self.button_c.setGeometry(QtCore.QRect(60, 80, 61, 61))
    self.button_c.setToolTipDuration(0)
    self.button_c.setStyleSheet("QPushButton { background-color: rgb(214, 214, 214); "
                                "border: 1px solid gray;\n"
                                "} QPushButton:pressed { background-color: qlineargradient("
                                "x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #c9c9c9, stop: 1 #c7c7c7); }\n")
    self.button_c.setObjectName("button_c")
    self.button_c.setText("C")
    self.button_c.setFont(QFont("Swis721 Ex BT", 12))

    self.button_lbrac = QtWidgets.QPushButton(self.centralWidget)
    self.button_lbrac.setGeometry(QtCore.QRect(120, 80, 61, 61))
    self.button_lbrac.setToolTipDuration(0)
    self.button_lbrac.setStyleSheet("QPushButton { background-color: rgb(214, 214, 214); "
                                    "border: 1px solid gray; } QPushButton:pressed { "
                                    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, "
                                    "y2: 1, stop: 0 #c9c9c9, stop: 1 #c7c7c7); }")
    self.button_lbrac.setObjectName("button_lbrac")
    self.button_lbrac.setText("(")
    self.button_lbrac.setFont(QFont("Swis721 Ex BT", 12))

    self.button_rbrac = QtWidgets.QPushButton(self.centralWidget)
    self.button_rbrac.setGeometry(QtCore.QRect(180, 80, 61, 61))
    self.button_rbrac.setToolTipDuration(0)
    self.button_rbrac.setStyleSheet("QPushButton { background-color: rgb(214, 214, 214); "
                                    "border: 1px solid gray; } QPushButton:pressed { "
                                    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, "
                                    "y2: 1, stop: 0 #c9c9c9, stop: 1 #c7c7c7); }")
    self.button_rbrac.setObjectName("button_rbrac")
    self.button_rbrac.setText(")")
    self.button_rbrac.setFont(QFont("Swis721 Ex BT", 12))

    self.button_power = QtWidgets.QPushButton(self.centralWidget)
    self.button_power.setGeometry(QtCore.QRect(180, 140, 61, 61))
    self.button_power.setToolTipDuration(0)
    self.button_power.setStyleSheet("QPushButton { background-color: rgb(214, 214, 214); "
                                    "border: 1px solid gray; } QPushButton:pressed { "
                                    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, "
                                    "y2: 1, stop: 0 #c9c9c9, stop: 1 #c7c7c7); }")
    self.button_power.setObjectName("button_power")
    self.button_power.setText("^")
    self.button_power.setFont(QFont("Swis721 Ex BT", 12))

    self.button_ln = QtWidgets.QPushButton(self.centralWidget)
    self.button_ln.setGeometry(QtCore.QRect(180, 200, 61, 61))
    self.button_ln.setToolTipDuration(0)
    self.button_ln.setStyleSheet("QPushButton { background-color: rgb(214, 214, 214); "
                                 "border: 1px solid gray; } QPushButton:pressed { "
                                 "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                 "stop: 0 #c9c9c9, stop: 1 #c7c7c7); }")
    self.button_ln.setObjectName("button_ln")
    self.button_ln.setText("ln")
    self.button_ln.setFont(QFont("Swis721 Ex BT", 12))

    self.button_factorial = QtWidgets.QPushButton(self.centralWidget)
    self.button_factorial.setGeometry(QtCore.QRect(180, 260, 61, 61))
    self.button_factorial.setToolTipDuration(0)
    self.button_factorial.setStyleSheet("QPushButton { background-color: rgb(214, 214, 214); "
                                        "border: 1px solid gray; } QPushButton:pressed { "
                                        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                        "stop: 0 #c9c9c9, stop: 1 #c7c7c7); }")
    self.button_factorial.setObjectName("button_factorial")
    self.button_factorial.setText("x!")
    self.button_factorial.setFont(QFont("Swis721 Ex BT", 12))

    self.button_dot = QtWidgets.QPushButton(self.centralWidget)
    self.button_dot.setGeometry(QtCore.QRect(120, 320, 61, 61))
    self.button_dot.setToolTipDuration(0)
    self.button_dot.setStyleSheet("QPushButton { background-color: rgb(214, 214, 214); "
                                  "border: 1px solid gray; \n"
                                  "} QPushButton:pressed { background-color: qlineargradient("
                                  "x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 #c9c9c9, stop: 1 #c7c7c7); }")
    self.button_dot.setObjectName("button_dot")
    self.button_dot.setText(".")
    self.button_dot.setFont(QFont("Swis721 Ex BT", 12))

    self.button_root = QtWidgets.QPushButton(self.centralWidget)
    self.button_root.setGeometry(QtCore.QRect(180, 320, 61, 61))
    self.button_root.setToolTipDuration(0)
    self.button_root.setStyleSheet("QPushButton { background-color: rgb(214, 214, 214); border: "
                                   "1px solid gray; } QPushButton:pressed { "
                                   "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                   "stop: 0 #c9c9c9, stop: 1 #c7c7c7); }")
    self.button_root.setObjectName("button_root")
    self.button_root.setText("x√y")
    self.button_root.setFont(QFont("Swis721 Ex BT", 12))

    self.button_division = QtWidgets.QPushButton(self.centralWidget)
    self.button_division.setGeometry(QtCore.QRect(300, 80, 61, 61))
    self.button_division.setToolTipDuration(0)
    self.button_division.setStyleSheet("QPushButton { background-color: "
                                       "rgb(0, 0, 98); color: white; "
                                       "border: 1px solid gray; } "
                                       "QPushButton:pressed { "
                                       "background-color: qlineargradient(x1: 0, "
                                       "y1: 0, x2: 0, y2: 1, stop: 0 #000066, "
                                       "stop: 1 #000080); }")
    self.button_division.setObjectName("button_division")
    self.button_division.setText("/")
    self.button_division.setFont(QFont("Swis721 Ex BT", 12))

    self.button_minus = QtWidgets.QPushButton(self.centralWidget)
    self.button_minus.setGeometry(QtCore.QRect(300, 260, 61, 61))
    self.button_minus.setToolTipDuration(0)
    self.button_minus.setStyleSheet("QPushButton { background-color: "
                                    "rgb(0, 0, 98); color: white; "
                                    "border: 1px solid gray; } QPushButton:pressed { "
                                    "background-color: qlineargradient(x1: 0, y1: 0, "
                                    "x2: 0, y2: 1, stop: 0 #000066, "
                                    "stop: 1 #000080); }")
    self.button_minus.setObjectName("button_minus")
    self.button_minus.setText("-")
    self.button_minus.setFont(QFont("Swis721 Ex BT", 12))

    self.button_plus = QtWidgets.QPushButton(self.centralWidget)
    self.button_plus.setGeometry(QtCore.QRect(300, 200, 61, 61))
    self.button_plus.setToolTipDuration(0)
    self.button_plus.setStyleSheet("QPushButton { background-color: "
                                   "rgb(0, 0, 98); color: white; "
                                   "border: 1px solid gray; } QPushButton:pressed "
                                   "{ background-color: qlineargradient(x1: 0, y1: 0, "
                                   "x2: 0, y2: 1, stop: 0 #000066, "
                                   "stop: 1 #000080); }")
    self.button_plus.setObjectName("button_plus")
    self.button_plus.setText("+")
    self.button_plus.setFont(QFont("Swis721 Ex BT", 12))

    self.button_equal = QtWidgets.QPushButton(self.centralWidget)
    self.button_equal.setGeometry(QtCore.QRect(300, 320, 61, 61))
    self.button_equal.setToolTipDuration(0)
    self.button_equal.setStyleSheet("QPushButton { background-color: rgb(0, 0, 98); color: white; "
                                    "border: 1px solid gray; } QPushButton:pressed { "
                                    "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                    "stop: 0 #000066, stop: 1 #000080); }")
    self.button_equal.setObjectName("button_equal")
    self.button_equal.setText("=")
    self.button_equal.setFont(QFont("Swis721 Ex BT", 12))

    self.button_multiply = QtWidgets.QPushButton(self.centralWidget)
    self.button_multiply.setGeometry(QtCore.QRect(300, 140, 61, 61))
    self.button_multiply.setToolTipDuration(0)
    self.button_multiply.setStyleSheet("QPushButton { background-color: "
                                       "rgb(0, 0, 98); color: white; "
                                       "border: 1px solid gray; } "
                                       "QPushButton:pressed { "
                                       "background-color: qlineargradient(x1: 0, "
                                       "y1: 0, x2: 0, y2: 1, stop: 0 #000066, "
                                       "stop: 1 #000080); }")
    self.button_multiply.setObjectName("button_multiply")
    self.button_multiply.setText("*")
    self.button_multiply.setFont(QFont("Swis721 Ex BT", 12))

    self.button_rand = QtWidgets.QPushButton(self.centralWidget)
    self.button_rand.setGeometry(QtCore.QRect(240, 320, 61, 61))
    self.button_rand.setToolTipDuration(0)
    self.button_rand.setStyleSheet("QPushButton { background-color: rgb(214, 214, 214); border: "
                                   "1px solid gray; } QPushButton:pressed { "
                                   "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                   "stop: 0 #c9c9c9, stop: 1 #c7c7c7); }")
    self.button_rand.setObjectName("button_rand")
    self.button_rand.setText("rand")
    self.button_rand.setFont(QFont("Swis721 Ex BT", 12))

    self.abs_button = QtWidgets.QPushButton(self.centralWidget)
    self.abs_button.setGeometry(QtCore.QRect(240, 260, 61, 61))
    self.abs_button.setToolTipDuration(0)
    self.abs_button.setStyleSheet("QPushButton { background-color: rgb(214, 214, 214); border: "
                                  "1px solid gray; } QPushButton:pressed { "
                                  "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                  "stop: 0 #c9c9c9, stop: 1 #c7c7c7); }")
    self.abs_button.setObjectName("abs_button")
    self.abs_button.setText("|x|")
    self.abs_button.setFont(QFont("Swis721 Ex BT", 12))

    self.ten_power_button = QtWidgets.QPushButton(self.centralWidget)
    self.ten_power_button.setGeometry(QtCore.QRect(240, 200, 61, 61))
    self.ten_power_button.setToolTipDuration(0)
    self.ten_power_button.setStyleSheet("QPushButton { background-color: rgb(214, 214, 214); border: "
                                        "1px solid gray; } QPushButton:pressed { "
                                        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                        "stop: 0 #c9c9c9, stop: 1 #c7c7c7); }")
    self.ten_power_button.setObjectName("ten_power_button")
    self.ten_power_button.setText("10^x")
    self.ten_power_button.setFont(QFont("Swis721 Ex BT", 12))

    self.e_power_button = QtWidgets.QPushButton(self.centralWidget)
    self.e_power_button.setGeometry(QtCore.QRect(240, 140, 61, 61))
    self.e_power_button.setToolTipDuration(0)
    self.e_power_button.setStyleSheet("QPushButton { background-color: rgb(214, 214, 214); border: "
                                        "1px solid gray; } QPushButton:pressed { "
                                        "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                        "stop: 0 #c9c9c9, stop: 1 #c7c7c7); }")
    self.e_power_button.setObjectName("e_power_button")
    self.e_power_button.setText("e^x")
    self.e_power_button.setFont(QFont("Swis721 Ex BT", 12))

    self.e_button = QtWidgets.QPushButton(self.centralWidget)
    self.e_button.setGeometry(QtCore.QRect(240, 80, 61, 61))
    self.e_button.setToolTipDuration(0)
    self.e_button.setStyleSheet("QPushButton { background-color: rgb(214, 214, 214); border: "
                                      "1px solid gray; } QPushButton:pressed { "
                                      "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, "
                                      "stop: 0 #c9c9c9, stop: 1 #c7c7c7); }")
    self.e_button.setObjectName("e_button")
    self.e_button.setText("e")
    self.e_button.setFont(QFont("Swis721 Ex BT", 12))

    self.input = QtWidgets.QLineEdit(self.centralWidget)
    self.input.setGeometry(QtCore.QRect(0, 0, 361, 81))
    self.input.setMinimumSize(QtCore.QSize(361, 81))
    self.input.setMaximumSize(QtCore.QSize(361, 81))
    self.input.setAlignment(QtCore.Qt.AlignCenter)
    self.input.setStyleSheet("QLineEdit{border: 1px solid gray; }")
    self.input.setObjectName("input")
    self.input.setFont(QFont("Swis721 Ex BT", 10))
    MainWindow.setCentralWidget(self.centralWidget)

    QtCore.QMetaObject.connectSlotsByName(MainWindow)
