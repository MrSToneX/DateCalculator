# coding:utf-8
# running by Python3 - 20201203Created
"""========================================== Update Log ======================

V1.0 20.11.26.2127 - Early version, achieve the basic functions, many bugs.
    需求：
    1. 计划开工日期，计划竣工日期，计划工期 计算
============================================================================"""
import sys
import datetime
from PyQt5 import QtGui, QtWidgets, QtCore
import DateCalculator_GUI_V1_0

MAIN_TITLE_NAME = 'DateCalculator V1.0'

def date_translate(date_str: str):
    return datetime.datetime.strptime(date_str, '%Y-%m-%d')


def set_label_text(label_name: QtWidgets.QLabel, label_text: str, label_color: str):
    label_name.setText(label_text)
    label_name.setStyleSheet('color:%s' % label_color)


def calculate():
    date_start = date_translate(ui.date_edit_start.text())
    date_stop = date_translate(ui.date_edit_stop.text())
    if ui.checkBox_start.isChecked() is True and ui.checkBox_stop.isChecked() is True and ui.checkBox_days.isChecked() is False:
        if date_start <= date_stop:
            days = (date_stop - date_start + datetime.timedelta(days=1)).days
            ui.line_days.setText(str(days))
            set_label_text(ui.label_status, '', 'black')
        else:
            set_label_text(ui.label_status, '需要：开工＜竣工', 'red')
    elif ui.checkBox_start.isChecked() is True and ui.checkBox_stop.isChecked() is False and ui.checkBox_days.isChecked() is True:
        try:
            date_days = int(ui.line_days.text())
        except:
            set_label_text(ui.label_status, '需要：工期为整数', 'red')
            return
        if date_days > 0:
            datedt = (date_start + datetime.timedelta(days=date_days - 1)).strftime('%Y-%m-%d')
            ui.date_edit_stop.setDate(QtCore.QDate.fromString(datedt, 'yyyy-M-d'))
            set_label_text(ui.label_status, '', 'black')
        else:
            set_label_text(ui.label_status, '需要：工期＞0', 'red')
    elif ui.checkBox_start.isChecked() is False and ui.checkBox_stop.isChecked() is True and ui.checkBox_days.isChecked() is True:
        try:
            date_days = int(ui.line_days.text())
        except:
            set_label_text(ui.label_status, '需要：工期为整数', 'red')
            return
        if date_days > 0:
            datedt = (date_stop - datetime.timedelta(days=date_days - 1)).strftime('%Y-%m-%d')
            ui.date_edit_start.setDate(QtCore.QDate.fromString(datedt, 'yyyy-M-d'))
            set_label_text(ui.label_status, '', 'black')
        else:
            set_label_text(ui.label_status, '需要：工期＞0', 'red')
    else:
        set_label_text(ui.label_status, '需要：任意3选2', 'red')


def ui_init():
    widgets.setWindowTitle(MAIN_TITLE_NAME)
    ui.date_edit_start.setDisplayFormat('yyyy-M-d')
    ui.date_edit_start.setCalendarPopup(True)
    ui.date_edit_start.setDate(QtCore.QDate.currentDate())
    ui.date_edit_stop.setDisplayFormat('yyyy-M-d')
    ui.date_edit_stop.setCalendarPopup(True)
    ui.date_edit_stop.setDate(QtCore.QDate.currentDate())


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    widgets = QtWidgets.QMainWindow()
    ui = DateCalculator_GUI_V1_0.Ui_Form()
    ui.setupUi(widgets)
    ui.pushButton.clicked.connect(calculate)
    widgets.show()
    ui_init()
    sys.exit(app.exec_())
