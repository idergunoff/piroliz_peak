# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\USER\PycharmProjects\piroliz_peak\manual.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Manual(object):
    def setupUi(self, Manual):
        Manual.setObjectName("Manual")
        Manual.resize(815, 889)
        self.textBrowser = QtWidgets.QTextBrowser(Manual)
        self.textBrowser.setGeometry(QtCore.QRect(20, 10, 781, 811))
        self.textBrowser.setObjectName("textBrowser")
        self.pushButton_standart = QtWidgets.QPushButton(Manual)
        self.pushButton_standart.setGeometry(QtCore.QRect(20, 840, 271, 31))
        self.pushButton_standart.setObjectName("pushButton_standart")

        self.retranslateUi(Manual)
        QtCore.QMetaObject.connectSlotsByName(Manual)

    def retranslateUi(self, Manual):
        _translate = QtCore.QCoreApplication.translate
        Manual.setWindowTitle(_translate("Manual", "Manual"))
        self.textBrowser.setHtml(_translate("Manual", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; text-decoration: underline;\">Инструкция к программе PirolizPeak</span><span style=\" font-size:14pt; text-decoration: underline;\"> </span></p>\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">интерпретация данных пиролиза (Rock Eval 6)</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; font-weight:600;\"><br /></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">1. </span><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">&quot;Выбрать каталог&quot;</span><span style=\" font-size:12pt;\"> - загрузка файлов для интерпретации. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Необходимо выбрать каталог, содержащий файлы хроматограмм импортированные в формат </span><span style=\" font-size:12pt; font-style:italic;\">txt. </span><span style=\" font-size:12pt;\">При импорте в программе </span><span style=\" font-size:12pt; font-weight:600; font-style:italic;\">Postrun</span><span style=\" font-size:12pt; font-style:italic;\"> </span><span style=\" font-size:12pt;\">выбрать категории Chromatogram, (TIC/MIC), (MS), delimeter - tab. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Обязательным условием является наличие в папке трех типов файлов для каждой пробы: *</span><span style=\" font-size:12pt; font-style:italic;\">_fid</span><span style=\" font-size:12pt;\">, *</span><span style=\" font-size:12pt; font-style:italic;\">_ms</span><span style=\" font-size:12pt;\">, *</span><span style=\" font-size:12pt; font-style:italic;\">_ox_ms. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">В названии файла должны содержаться данные разделенные нижним подчеркиванием ( _ ): 1 - номер образца, 2 - номер пробы, 3 - навеска обазца в формате 0.00000, 4 - один из трех типов файла, описанных выше.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">2. </span><span style=\" font-size:12pt;\">После загрузки и первичной автоматической обработки доступен список загруженных файлов. При клике по файлу в списке выводятся хроматограммы соответстующего файла. В зависимости от типа файла, на хроматограмме автоматически выделены пики  соответствующих параметров. </span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Выделение пиков можно корректировать изменяя параметры t1, t2, t3, BL (базовая линия). Необходимо проверить выделение параметров в каждом файле, особое внимание стоит уделить файлам выделенным в списке красным цветом. После корректировки выделения пика нужно обязательно нажать кнопку </span><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">&quot;Сохранить изменения&quot;</span><span style=\" font-size:12pt;\">. При этом файл в списке выделится зеленым цветом.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">3. Градуировка.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Для градуировки необходимо загрузить папку с файлами хроматограмм стандартного образца. Обработать все файлы - проверить правильность выделения пиков. Далее нажать кнопку </span><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">&quot;Выполнить градуировку&quot;</span><span style=\" font-size:12pt;\">.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">В окне градуировки отображаются вкладки с расчетными параметрами S1, S2 и т.д. Для каждого параметра отображается таблица с пробами градуировки и значениями площади пика параметра пробы. В таблице можно исключить из расчетов отдельный компонент отжав соответствующюю галочку. Красным цветом в таблице выделен компонент наиболее удаленный от среднего значения.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Для каждого параметра также отображаются: среднее значение навески пробы, среднее значение площади пика, RSD - коэффициент вариации, C_st - концентрация параметра в стандартном образце, расчитанный градуировочный коэффициент. Концентрацию стандартного образца можно изменить вручную или загрузить в соответствующем фалйле xlsx нажав на кнопку </span><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">&quot;Стандартный образец&quot;</span><span style=\" font-size:12pt;\">.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Для параметра Tmax отображаются: средняя Tmax, Tmax стандартного образца и расчитанный коэффициент dT.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">Не закрывая окно градуировки, можно корректировать выделение пиков параметров в основном окне программы. При нажатии кнопки </span><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">&quot;Сохранить изменения&quot;</span><span style=\" font-size:12pt;\">, значения в окне градуировки пересчитаются.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">&quot;Сохранить градуировку&quot;</span><span style=\" font-size:12pt;\"> - сохраняет градуировочные коэффициенты в xls файл. Данный файл загружается в основном окне программы нажатием на кнопку </span><span style=\" font-size:12pt; font-style:italic; text-decoration: underline;\">&quot;Загрузить градуировку&quot;</span><span style=\" font-size:12pt;\">. При загрузке градуировки, градуировочные коэффициенты отображаются в соответствующей панели и применяются для расчета концентраций в загруженных файлах проб.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:600;\">4.</span><span style=\" font-size:12pt;\"> </span><span style=\" font-size:12pt; font-weight:600; font-style:italic; text-decoration: underline;\">&quot;Сохранить результат&quot;</span><span style=\" font-size:12pt;\"> - сохраняет таблицу с концентрациями и градуировочными коэффициентами в xls файл.</span></p></body></html>"))
        self.pushButton_standart.setText(_translate("Manual", "Файл стандартного образца"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Manual = QtWidgets.QDialog()
    ui = Ui_Manual()
    ui.setupUi(Manual)
    Manual.show()
    sys.exit(app.exec_())
