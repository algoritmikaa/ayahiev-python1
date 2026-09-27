from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget,
                              QPushButton, QLabel, QVBoxLayout,
                                QRadioButton,QMessageBox,
                                QHBoxLayout,
                                QPushButton, QGroupBox,
                                QButtonGroup,)
from random import shuffle


def  show_result():
    Radio_groupbox.hide()
    AnsGroupBox.show()
    button.setText("Следущий вопрос")

def shoe_question():
      AnsGroupBox.hide()
      Radio_groupbox.show()
      button.setText("Ответить")
      GroupBox.setExclusive(False)
      rtb1.setChecked(False)
      rtb2.setChecked(False)
      rtb3.setChecked(False)
      rtb4.setChecked(False)
      GroupBox.setExclusive(True)

def ask(question1, right_answer, wrong1, wrong2, wrong3):
     shuffle(answers)
     question.setText(question1)
     answers[0].setText(right_answer)
     answers[1].setText(wrong1)
     answers[2].setText(wrong2)
     answers[3].setText(wrong3)
     lb_correct.setText(right_answer)

def show_correct(res):
          lb_result.setText(res)
          show_result()

def check_answer():
  if answers[0].isChecked():
    show_correct("Правда")
  elif answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
    show_correct("Неверно")



app = QApplication([])
main_win = QWidget()
main_win.resize(600,400)
main_win.setWindowTitle("Карточки для запоминания")




question =  QLabel("Вопрос")
button = QPushButton("Ответить")
rtb1 = QRadioButton("Ответ1")
rtb2 = QRadioButton("Ответ2")
rtb3 = QRadioButton("Ответ3")
rtb4 = QRadioButton("Ответ4")

answers = [rtb1, rtb2, rtb3 , rtb4]

Radio_groupbox = QGroupBox("Варианты ответа")

GroupBox = QButtonGroup()
GroupBox.addButton(rtb1)
GroupBox.addButton(rtb2)
GroupBox.addButton(rtb3)
GroupBox.addButton(rtb4)


main_group_line = QVBoxLayout()
group_line1 = QHBoxLayout()
group_line2 = QHBoxLayout()

group_line1.addWidget(rtb1)
group_line1.addWidget(rtb2)
group_line2.addWidget(rtb3)
group_line2.addWidget(rtb4)

main_group_line.addLayout(group_line1)
main_group_line.addLayout(group_line2)

Radio_groupbox.setLayout(main_group_line)


AnsGroupBox = QGroupBox()
lb_result = QLabel("Правда/Неправда")
lb_correct = QLabel("Сам верный ответ")




ans_group_line = QVBoxLayout()
ans_group_line.addWidget(lb_result,alignment=(Qt.AlignTop | Qt.AlignLeft))
ans_group_line.addWidget(lb_correct, alignment= Qt.AlignHCenter)

AnsGroupBox.setLayout(ans_group_line)


main_line = QVBoxLayout()
line1 = QHBoxLayout()
line2 = QHBoxLayout()
line3 = QHBoxLayout()

line1.addWidget(question, alignment=Qt.AlignCenter)
line2.addWidget(Radio_groupbox)
line2.addWidget(AnsGroupBox)
line3.addStretch(2)
line3.addWidget(button,stretch=2)
line3.addStretch(2)
AnsGroupBox.hide()

main_line.addLayout(line1,stretch=2)
main_line.addLayout(line2,stretch=8)
main_line.addStretch(1)
main_line.addLayout(line3,stretch=2)
main_line.addStretch(1)
main_line.addSpacing(5)

main_win.setLayout(main_line)

main_win.setStyleSheet('''background-color: white;
                     font-size:16px;
                     background: qlineargradient(x1:0, y1:0, x2:1, y2:1,
                                    stop:0 #d37aff, stop:1 #ffffff);
                     color:black;
                     box-shadow:''')


ask("Какой газ преобладает в атмосфере Земли?", "азот","кислород","Углекислый газ","Водород")

button.clicked.connect(check_answer)


main_win.show()
app.exec()
