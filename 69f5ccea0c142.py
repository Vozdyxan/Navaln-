

from PyQt5.QtCore import Qt, QTime
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QLineEdit


app = QApplication([])

win_x, win_y = 200, 100
win_width, win_height = 1000, 600

"""ОКНО 1"""
# главное окно:
main_win = QWidget()
main_win.setWindowTitle('Здоровье')
main_win.resize(win_width, win_height)
main_win.move(win_x, win_y)

#виджеты окна: кнопка и надпись
txt_hello = QLabel('Добро пожаловать в программу по определению состояния здоровья!')
txt_instruction = QLabel('Данное приложение позволит вам с помощью теста Руфье провести первичную диагностику вашего здоровья.\n'
                    'Проба Руфье представляет собой нагрузочный комплекс, предназначенный для оценки работоспособности сердца при физической нагрузке.\n'
                    'У испытуемого, находящегося в положении лежа на спине в течение 5 мин, определяют частоту пульса за 15 секунд;\n'
                    'затем в течение 45 секунд испытуемый выполняет 30 приседаний.\n'
                    'После окончания нагрузки испытуемый ложится, и у него вновь подсчитывается число пульсаций за первые 15 секунд,\n'
                    'а потом — за последние 15 секунд первой минуты периода восстановления.\n'
                    'Важно! Если в процессе проведения испытания вы почувствуете себя плохо (появится головокружение, шум в\n'
                    'ушах, сильная одышка и др.), то тест необходимо прервать и обратиться к врачу.' )

button_start = QPushButton('Начать')

#расположение виджетов
main_v_layout_1 = QVBoxLayout()
main_v_layout_1.addWidget(txt_hello)
main_v_layout_1.addWidget(txt_instruction)
main_v_layout_1.addWidget(button_start, alignment = Qt.AlignCenter)

main_win.setLayout(main_v_layout_1)






"""ОКНО 2"""

work_win = QWidget()
work_win.setWindowTitle('Здоровье')
work_win.resize(win_width, win_height)
work_win.move(win_x, win_y)

#виджеты окна: кнопка и надпись
txt_fio = QLabel('Введите Ф.И.О.:')
txt_age = QLabel('Полных лет:')
txt_test1 = QLabel('Лягте на спину и замерьте пульс за 15 секунд. Нажмите кнопку "Начать первый тест", чтобы запустить таймер.\nРезультат запишите в соответствующее поле.')
txt_test2 = QLabel('Выполните 30 приседаний за 45 секунд. Для этого нажмите кнопку "Начать делать приседания",\nчтобы запустить счетчик приседаний.')
txt_test3 = QLabel('Лягте на спину и замерьте пульс сначала за первые 15 секунд минуты, затем за последние 15 секунд.\nНажмите кнопку "Начать финальный тест", чтобы запустить таймер.\nЗеленым обозначены секунды, в течение которых необходимо \nпроводить измерения, черным - минуты без замера пульсаций. Результаты запишите в соответствующие поля.')

btn_test1 = QPushButton('Начать первый тест')
btn_test2 = QPushButton('Начать делать приседания')
btn_test3 = QPushButton('Начать финальный тест')
btn_result = QPushButton('Отправить результаты')

line_1_fio = QLineEdit("Ф.И.О.")
line_2_age = QLineEdit('0')
line_3_res_test1 = QLineEdit('0')
line_4_res_test3  = QLineEdit('0')
line_5_res_test3 = QLineEdit('0')

time = QTime(0, 0, 15)
txt_timer = time.toString("hh:mm:ss")
text_timer = QLabel(txt_timer)
text_timer.setFont(QFont("Times", 36, QFont.Bold))

#расположение виджетов
left_v_layout_2 = QVBoxLayout()
rigth_v_layout_2 = QVBoxLayout()
main_h_layout_2 = QHBoxLayout()

left_v_layout_2.addWidget(txt_fio)
left_v_layout_2.addWidget(line_1_fio, alignment = Qt.AlignLeft)
left_v_layout_2.addWidget(txt_age)
left_v_layout_2.addWidget(line_2_age, alignment = Qt.AlignLeft)
left_v_layout_2.addWidget(txt_test1)
left_v_layout_2.addWidget(btn_test1, alignment = Qt.AlignLeft)
left_v_layout_2.addWidget(line_3_res_test1, alignment = Qt.AlignLeft)
left_v_layout_2.addWidget(txt_test2)
left_v_layout_2.addWidget(btn_test2, alignment = Qt.AlignLeft)
left_v_layout_2.addWidget(txt_test3)
left_v_layout_2.addWidget(btn_test3, alignment = Qt.AlignLeft)
left_v_layout_2.addWidget(line_4_res_test3, alignment = Qt.AlignLeft)
left_v_layout_2.addWidget(line_5_res_test3, alignment = Qt.AlignLeft)
left_v_layout_2.addWidget(btn_result, alignment = Qt.AlignCenter)

rigth_v_layout_2.addWidget(text_timer, alignment = Qt.AlignCenter)

main_h_layout_2.addLayout(left_v_layout_2)
main_h_layout_2.addLayout(rigth_v_layout_2)

work_win.setLayout(main_h_layout_2)









"""ОКНО 3"""

result_win = QWidget()
result_win.setWindowTitle('Результат')
result_win.resize(win_width, win_height)
result_win.move(win_x, win_y)

#виджеты окна: кнопка и надпись
txt_index = QLabel('Индекс Руфье: ', alignment = Qt.AlignCenter)
txt_res = QLabel('Работоспособность сердца: ', alignment = Qt.AlignCenter)

#расположение виджетов
main_v_layout_3 = QVBoxLayout()
main_v_layout_3.addWidget(txt_index)
main_v_layout_3.addWidget(txt_res)

result_win.setLayout(main_v_layout_3)



def next_win_2():
    # переход от 1 окна к 2
    main_win.hide()
    work_win.show()

def next_win_3():
    # переход от 2 окна к 3
    work_win.hide()
    result_win.show()

def test1():
    pass

def test2():
    pass

def test3():
    pass

button_start.clicked.connect(next_win_2)
btn_result.clicked.connect(next_win_3)

btn_test1.clicked.connect(test1)
btn_test2.clicked.connect(test2)
btn_test3.clicked.connect(test3)


main_win.show()
# work_win.show()
# result_win.show()
app.exec_()



