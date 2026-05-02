

from PyQt5.QtCore import Qt, QTime, QTimer
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
    global res

    person = line_1_fio.text()
    age = int(line_2_age.text())
    test1 = line_3_res_test1.text()
    test2 = line_4_res_test3.text()
    test3 = line_5_res_test3.text()

    res = results(person, age, test1, test2, test3)

    txt_index.setText('Индекс Руфье: ' + str(index))
    txt_res.setText('Работоспособность сердца: ' + res)

    # переход от 2 окна к 3
    work_win.hide()
    result_win.show()

def timer1Event(timer):
    global time1
    time1 = time1.addSecs(-1)
    text_timer.setText(time1.toString("hh:mm:ss"))
    text_timer.setFont(QFont("Times", 36, QFont.Bold))
    text_timer.setStyleSheet("color: rgb(0,0,0)")
    if time1.toString("hh:mm:ss") == "00:00:00":
        timer.stop()

def test1():
    global time1
    time1 = QTime(0, 0, 15)
    timer = QTimer()
    timer.timeout.connect(lambda: timer1Event(timer))
    timer.start(1000)

def timer2Event(timer):
    global time2
    time2 = time2.addSecs(-1)
    text_timer.setText(time2.toString("hh:mm:ss")[6:8])
    text_timer.setStyleSheet("color: rgb(0,0,0)")
    text_timer.setFont(QFont("Times", 36, QFont.Bold))
    if time2.toString("hh:mm:ss") == "00:00:00":
        timer.stop()

def test2():
    global time2
    time2 = QTime(0, 0, 30)
    timer = QTimer()
    # одно приседание в 1.5 сек
    timer.timeout.connect(lambda: timer2Event(timer))
    timer.start(1500)

def timer3Event(timer):
    global time3
    time3 = time3.addSecs(-1)
    text_timer.setText(time3.toString("hh:mm:ss"))
    if int(time3.toString("hh:mm:ss")[6:8]) >= 45:
        text_timer.setStyleSheet("color: rgb(0,255,0)")
    elif int(time3.toString("hh:mm:ss")[6:8]) <= 15:
        text_timer.setStyleSheet("color: rgb(0,255,0)")
    else:
        text_timer.setStyleSheet("color: rgb(0,0,0)")
    text_timer.setFont(QFont("Times", 36, QFont.Bold))
    if time3.toString("hh:mm:ss") == "00:00:00":
        timer.stop()

def test3():
    global time3
    time3 = QTime(0, 1, 0)
    timer = QTimer()
    timer.timeout.connect(lambda: timer3Event(timer))
    timer.start(1000)

button_start.clicked.connect(next_win_2)
btn_result.clicked.connect(next_win_3)

btn_test1.clicked.connect(test1)
btn_test2.clicked.connect(test2)
btn_test3.clicked.connect(test3)


txt_res1 = "низкая. Срочно обратитесь к врачу!"
txt_res2 = "удовлетворительная. Обратитесь к врачу!"
txt_res3 = "средняя. Возможно, стоит дополнительно обследоваться у врача."
txt_res4 = "выше среднего"
txt_res5 = "высокая"

def results(person, age, test1, test2, test3):
    global index
    if age < 7:
        index = 0
        return "нет данных для такого возраста"
    index = (4 * (int(test1) + int(test2) + int(test3)) - 200) / 10
    if age == 7 or age == 8:
        if index >= 21:
            return txt_res1
        elif index < 21 and index >= 17:
            return txt_res2
        elif index < 17 and index >= 12:
            return txt_res3
        elif index < 12 and index >= 6.5:
            return txt_res4
        else:
            return txt_res5
    elif age == 9 or age == 10:
        if index >= 19.5:
            return txt_res1
        elif index < 19.5 and index >= 15.5:
            return txt_res2
        elif index < 15.5 and index >= 10.5:
            return txt_res3
        elif index < 10.5 and index >= 5:
            return txt_res4
        else:
            return txt_res5
    elif age == 11 or age == 12:
        if index >= 18:
            return txt_res1
        elif index < 18 and index >= 14:
            return txt_res2
        elif index < 14 and index >= 9:
                return txt_res3
        elif index < 9 and index >= 3.5:
            return txt_res4
        else:
            return txt_res5
    elif age == 13 or age == 14:
        print('ind ', index)
        if index >= 16.5:
            return txt_res1
        elif index < 16.5 and index >= 12.5:
            return txt_res2
        elif index < 12.5 and index >= 7.5:
            return txt_res3
        elif index < 7.5 and index >= 2:
            return txt_res4
        else:
            return txt_res5
    elif age >= 15:
        if index >= 15:
            return txt_res1
        elif index < 15 and index >= 11:
            return txt_res2
        elif index < 11 and index >= 6:
            return txt_res3
        elif index < 6 and index >= 0.5:
            return txt_res4
        else:
            return txt_res5

main_win.show()
# work_win.show()
# result_win.show()
app.exec_()
