import os, sys
import subprocess

import pandas as pd

from PyQt5.QtWidgets import QApplication, QFileDialog, QCheckBox, QTableWidgetItem, QTableWidget
import pyqtgraph as pg

from piroliz_peak_dialog import *
from functions import *
from graduation_dialog import *
from manual import *

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)

Graduation = QtWidgets.QDialog()
ui_g = Ui_Graduation()
ui_g.setupUi(Graduation)

MainWindow.show()

ui.graphicsView_i44.setBackground('w')
ui.graphicsView_i44.showGrid(x=True, y=True)

ui.graphicsView_i28.setBackground('w')
ui.graphicsView_i28.showGrid(x=True, y=True)

pd.options.mode.chained_assignment = None

column = ['obr', 'S1S2_t1', 'S1S2_t2', 'S1S2_t3', 'S1_area', 'S2_area', 'S3_t1', 'S3_t2', 'S3_t3', 'S3_bl', 'S3_area',
          'S3__area', 'S3CO_t1', 'S3CO_t2', 'S3CO_t3', 'S3CO_bl', 'S3CO_area', 'S3_CO_area', 'S4CO2_t1', 'S4CO2_t2',
          'S4CO2_t3', 'S4CO2_bl', 'S4CO2m_bl', 'S4CO2_area', 'S5_area', 'S4CO_t1', 'S4CO_t2', 'S4CO_bl',
          'S4CO_area', 'S1S2_attn', 'S3_attn', 'S3CO_attn', 'S4CO2_attn', 'S4CO_attn', 'Tmax']
tab_areas = pd.DataFrame(columns=column)


def open_dir():
    global tab_areas
    dict_obr = {}
    ui.listWidget.clear()
    tab_areas = pd.DataFrame(columns=column)
    dir_name = QFileDialog.getExistingDirectory()
    list_files = sorted(os.listdir(dir_name))
    error_list = check_file_name(list_files)
    if len(error_list) > 0:
        ui.info.setText('Ошибка названия файлов! Проверьте названия файлов: ' + ', '.join(error_list))
        ui.info.setStyleSheet('color: red')
    else:
        ui.lineEdit_direct.setText(dir_name)
        ui.progressBar.reset()
        ui.progressBar.setMaximum(len(list_files))
        ui.info.setText('Загрузка проб: ' + dir_name)
        ui.info.setStyleSheet('color: blue')
        n = 1
        if 'areas.xlsx' in list_files:
            tab_areas = pd.read_excel(dir_name + '/areas.xlsx', header=0, index_col=0)
            for file_name in list_files:
                if not file_name.endswith('.xlsx'):
                    if file_name.endswith('ox_ms.txt'):
                        obr = '_'.join(file_name.split('_')[:-2])
                    else:
                        obr = '_'.join(file_name.split('_')[:-1])
                    obr_row = tab_areas.loc[tab_areas['obr'] == obr].index.tolist()[0]
                    if file_name.endswith('ms.txt'):
                        ui.listWidget.addItem(file_name)
                        if file_name.endswith('ox_ms.txt'):
                            if tab_areas['S4CO2_attn'][obr_row] == True or tab_areas['S4CO_attn'][obr_row] == True:
                                ui.listWidget.item(ui.listWidget.count() - 1).setBackground(QtGui.QColor(255, 100, 100))
                        else:
                            if tab_areas['S3_attn'][obr_row] == True or tab_areas['S3CO_attn'][obr_row] == True:
                                ui.listWidget.item(ui.listWidget.count() - 1).setBackground(QtGui.QColor(255, 100, 100))
                    elif file_name.endswith('_fid.TXT'):
                        ui.listWidget.addItem(file_name)
                        if tab_areas['S1S2_attn'][obr_row] == True:
                            ui.listWidget.item(ui.listWidget.count() - 1).setBackground(QtGui.QColor(255, 100, 100))
                    ui.progressBar.setValue(n+1)
                    print(n)
                    n += 1
        else:
            for file_name in list_files:
                attn = False
                if file_name.endswith('ms.txt') and not file_name.endswith('.xlsx'):
                    ui.listWidget.addItem(file_name)
                    signal_i44 = select_signal_by_ion(dir_name + '/' + file_name, 44)
                    signal_i28 = select_signal_by_ion(dir_name + '/' + file_name, 28)
                    if file_name.endswith('ox_ms.txt'):
                        dict_obr['obr'] = '_'.join(file_name.split('_')[:-2])
                        dict_obr['S4CO2_t1'], dict_obr['S4CO2_t2'], dict_obr['S4CO2_t3'], dict_obr['S4CO2_bl'], \
                        dict_obr['S4CO2m_bl'], dict_obr['S4CO2_area'], dict_obr['S5_area'], dict_obr['S4CO2_attn'] = \
                            calc_S4CO2(signal_i44)
                        attn = dict_obr['S4CO2_attn']
                        dict_obr['S4CO_t1'], dict_obr['S4CO_t2'], dict_obr['S4CO_bl'], dict_obr['S4CO_area'], \
                        dict_obr['S4CO_attn'] = calc_S4CO(signal_i28)
                        if not attn:
                            attn = dict_obr['S4CO_attn']
                    else:
                        dict_obr['obr'] = '_'.join(file_name.split('_')[:-1])
                        dict_obr['S3_t1'], dict_obr['S3_t2'], dict_obr['S3_t3'], dict_obr['S3_bl'], dict_obr['S3_area'], \
                        dict_obr['S3__area'], dict_obr['S3_attn'] = calc_S3(signal_i44)
                        attn = dict_obr['S3_attn']
                        dict_obr['S3CO_t1'], dict_obr['S3CO_t2'], dict_obr['S3CO_t3'], dict_obr['S3CO_bl'], \
                        dict_obr['S3CO_area'], dict_obr['S3_CO_area'], dict_obr['S3CO_attn'] = calc_S3CO(signal_i28)
                        if not attn:
                            attn = dict_obr['S3CO_attn']

                elif file_name.endswith('_fid.TXT'):
                    ui.listWidget.addItem(file_name)
                    signal_fid = select_signal_by_ion(dir_name + '/' + file_name, 0)
                    dict_obr['obr'] = '_'.join(file_name.split('_')[:-1])
                    dict_obr['S1S2_t1'], dict_obr['S1S2_t2'], dict_obr['S1S2_t3'], dict_obr['S1_area'], dict_obr['S2_area'], \
                    dict_obr['S1S2_attn'] = calc_S1S2(signal_fid)
                    dict_obr['Tmax'] = 25 * calc_Tmax(signal_fid) + 225
                    attn = dict_obr['S1S2_attn']
                if len(dict_obr) == len(column):
                    # tab_areas = tab_areas.append(dict_obr, ignore_index=True)
                    tab_areas = pd.concat([tab_areas, pd.DataFrame([dict_obr])], ignore_index=True)
                    dict_obr.clear()
                if attn:
                    ui.listWidget.item(ui.listWidget.count() - 1).setBackground(QtGui.QColor(255, 100, 100))
                ui.progressBar.setValue(n)
                print(n)
                n += 1
        if ui.listWidget.count() > 0:
            ui.listWidget.setCurrentRow(0)
            ui.info.setText('Готово! Обработано ' + str(ui.listWidget.count()) + ' файлов')
            ui.info.setStyleSheet('color: green')
            print(tab_areas)


def choose_file():
    file_name = ui.listWidget.item(ui.listWidget.currentRow()).text()
    dir_name = ui.lineEdit_direct.text()
    if file_name.endswith('_fid.TXT'):
        signal_i44 = select_signal_by_ion(dir_name + '/' + file_name, 0)
    else:
        signal_i44 = select_signal_by_ion(dir_name + '/' + file_name, 44)
        signal_i28 = select_signal_by_ion(dir_name + '/' + file_name, 28)
    if file_name.endswith('ox_ms.txt'):
        obr = '_'.join(file_name.split('_')[:-2])
    else:
        obr = '_'.join(file_name.split('_')[:-1])
    obr_row = tab_areas.loc[tab_areas['obr'] == obr].index.tolist()[0]
    Wt = float(tab_areas['obr'][obr_row].split('_')[-1])
    if file_name.endswith('_fid.TXT'):
        ui.label_ion44.setText('FID:')
        ui.doubleSpinBox1_t1.setMinimum(0.0005)
        ui.graphicsView_i28.hide()
        ui.widget2.hide()
        ui.label_ion28.hide()
        ui.name1.setText('S1/S2')
        ui.doubleSpinBox1_t3.setMaximum(signal_i44['Ret.Time'].max())
        ui.doubleSpinBox1_t2.setMaximum(signal_i44['Ret.Time'].max())
        ui.doubleSpinBox1_t1.setMaximum(signal_i44['Ret.Time'].max())
        ui.doubleSpinBox1_t3.setValue(signal_i44['Ret.Time'][tab_areas['S1S2_t3'][obr_row]])
        ui.doubleSpinBox1_t2.setValue(signal_i44['Ret.Time'][tab_areas['S1S2_t2'][obr_row]])
        ui.doubleSpinBox1_t1.setValue(signal_i44['Ret.Time'][tab_areas['S1S2_t1'][obr_row]])
        ui.doubleSpinBox_dtmax.show()
        ui.doubleSpinBox_dtmax.setValue((tab_areas['Tmax'][obr_row] - 225) / 25)
        ui.spinBox1_bl1.hide()
        ui.spinBox1_bl2.hide()
        area1, area2 = tab_areas['S1_area'][obr_row], tab_areas['S2_area'][obr_row]
        ui.area1.setText('{:.0f}'.format(area1))
        ui.area2.setText('{:.0f}'.format(area2))
        ui.conc1.setText('{:.6f}'.format(calc_Cpr(area1, float(ui.S1_kg.text()), Wt)))
        ui.conc2.setText('{:.6f}'.format(calc_Cpr(area2, float(ui.S2_kg.text()), Wt)))
        ui.Tmax.show()
        ui.Tmax.setText('{:.2f}'.format(tab_areas['Tmax'][obr_row] - float(ui.dTmax.text())))
        t1_i44 = tab_areas['S1S2_t1'][obr_row]
        t2_i44 = tab_areas['S1S2_t3'][obr_row]
    elif file_name.endswith('ox_ms.txt'):
        ui.label_ion44.setText('ION 44:')
        ui.doubleSpinBox1_t1.setMinimum(0.02)
        ui.graphicsView_i28.show()
        ui.widget2.show()
        ui.label_ion28.show()
        ui.name1.setText('S4CO2/S4CO2m (S5)')
        ui.name2.setText('S4CO')
        ui.doubleSpinBox_dtmax.hide()
        ui.doubleSpinBox1_t3.setMaximum(signal_i44['Ret.Time'].max())
        ui.doubleSpinBox1_t2.setMaximum(signal_i44['Ret.Time'].max())
        ui.doubleSpinBox1_t1.setMaximum(signal_i44['Ret.Time'].max())
        ui.doubleSpinBox1_t3.setValue(signal_i44['Ret.Time'][tab_areas['S4CO2_t3'][obr_row]])
        ui.doubleSpinBox1_t2.setValue(signal_i44['Ret.Time'][tab_areas['S4CO2_t2'][obr_row]])
        ui.doubleSpinBox1_t1.setValue(signal_i44['Ret.Time'][tab_areas['S4CO2_t1'][obr_row]])
        ui.spinBox1_bl1.show()
        ui.spinBox1_bl1.setValue(int(tab_areas['S4CO2_bl'][obr_row]))
        area1, area2 = tab_areas['S4CO2_area'][obr_row], tab_areas['S5_area'][obr_row]
        ui.area1.setText('{:.0f}'.format(area1))
        ui.spinBox1_bl2.show()
        ui.spinBox1_bl2.setValue(int(tab_areas['S4CO2m_bl'][obr_row]))
        ui.area2.setText('{:.0f}'.format(area2))
        ui.conc1.setText('{:.6f}'.format(calc_Cpr(area1, float(ui.S4CO2_kg.text()), Wt)))
        ui.conc2.setText('{:.6f}'.format(calc_Cpr(area2, float(ui.S5_kg.text()), Wt)))
        t1_i44 = tab_areas['S4CO2_t1'][obr_row]
        t2_i44 = tab_areas['S4CO2_t3'][obr_row]
        ui.doubleSpinBox2_t2.setMaximum(signal_i28['Ret.Time'].max())
        ui.doubleSpinBox2_t1.setMaximum(signal_i28['Ret.Time'].max())
        ui.doubleSpinBox2_t2.setValue(signal_i28['Ret.Time'][tab_areas['S4CO_t2'][obr_row]])
        ui.doubleSpinBox2_t1.setValue(signal_i28['Ret.Time'][tab_areas['S4CO_t1'][obr_row]])
        ui.doubleSpinBox2_t3.hide()
        ui.spinBox2_bl.setValue(int(tab_areas['S4CO_bl'][obr_row]))
        area3 = tab_areas['S4CO_area'][obr_row]
        ui.area3.setText('{:.0f}'.format(area3))
        ui.conc3.setText('{:.6f}'.format(calc_Cpr(area3, float(ui.S4CO_kg.text()), Wt)))
        ui.area4.hide()
        ui.conc4.hide()
        ui.Tmax.hide()
        t1_i28 = tab_areas['S4CO_t1'][obr_row]
        t2_i28 = tab_areas['S4CO_t2'][obr_row]
    else:
        ui.label_ion44.setText('ION 44:')
        ui.doubleSpinBox1_t1.setMinimum(0.02)
        ui.graphicsView_i28.show()
        ui.widget2.show()
        ui.label_ion28.show()
        ui.name1.setText('S3/S3\'')
        ui.doubleSpinBox_dtmax.hide()
        ui.doubleSpinBox1_t3.setMaximum(signal_i44['Ret.Time'].max())
        ui.doubleSpinBox1_t2.setMaximum(signal_i44['Ret.Time'].max())
        ui.doubleSpinBox1_t1.setMaximum(signal_i44['Ret.Time'].max())
        ui.doubleSpinBox1_t3.setValue(signal_i44['Ret.Time'][tab_areas['S3_t3'][obr_row]])
        ui.doubleSpinBox1_t2.setValue(signal_i44['Ret.Time'][tab_areas['S3_t2'][obr_row]])
        ui.doubleSpinBox1_t1.setValue(signal_i44['Ret.Time'][tab_areas['S3_t1'][obr_row]])
        ui.spinBox1_bl1.show()
        ui.spinBox1_bl1.setValue(int(tab_areas['S3_bl'][obr_row]))
        area1, area2 = tab_areas['S3_area'][obr_row], tab_areas['S3__area'][obr_row]
        ui.area1.setText('{:.0f}'.format(area1))
        ui.area2.setText('{:.0f}'.format(area2))
        ui.conc1.setText('{:.6f}'.format(calc_Cpr(area1, float(ui.S3_kg.text()), Wt)))
        ui.conc2.setText('{:.6f}'.format(calc_Cpr(area2, float(ui.S3__kg.text()), Wt)))
        ui.spinBox1_bl2.hide()
        t1_i44 = tab_areas['S3_t1'][obr_row]
        t2_i44 = tab_areas['S3_t3'][obr_row]

        ui.name2.setText('S3CO/S3\'CO')
        ui.doubleSpinBox2_t3.setMaximum(signal_i28['Ret.Time'].max())
        ui.doubleSpinBox2_t2.setMaximum(signal_i28['Ret.Time'].max())
        ui.doubleSpinBox2_t1.setMaximum(signal_i28['Ret.Time'].max())
        ui.doubleSpinBox2_t3.setValue(signal_i28['Ret.Time'][tab_areas['S3CO_t3'][obr_row]])
        ui.doubleSpinBox2_t2.setValue(signal_i28['Ret.Time'][tab_areas['S3CO_t2'][obr_row]])
        ui.doubleSpinBox2_t1.setValue(signal_i28['Ret.Time'][tab_areas['S3CO_t1'][obr_row]])
        ui.spinBox2_bl.setValue(int(tab_areas['S3CO_bl'][obr_row]))
        area3, area4 = tab_areas['S3CO_area'][obr_row], tab_areas['S3_CO_area'][obr_row]
        ui.area3.setText('{:.0f}'.format(area3))
        ui.doubleSpinBox2_t3.show()
        ui.area4.show()
        ui.conc4.show()
        ui.area4.setText('{:.0f}'.format(area4))
        ui.conc3.setText('{:.6f}'.format(calc_Cpr(area3, float(ui.S3CO_kg.text()), Wt)))
        ui.conc4.setText('{:.6f}'.format(calc_Cpr(area4, float(ui.S3_CO_kg.text()), Wt)))
        ui.Tmax.hide()
        t1_i28 = tab_areas['S3CO_t1'][obr_row]
        t2_i28 = tab_areas['S3CO_t3'][obr_row]
    ui.graphicsView_i44.autoRange()
    ui.graphicsView_i28.autoRange()
    ui.graphicsView_i44.setYRange(signal_i44['Absolute Intensity'].iloc[t1_i44:t2_i44].max(),
                                  signal_i44['Absolute Intensity'].iloc[t1_i44:t2_i44].min())
    change_param_1()
    if not file_name.endswith('_fid.TXT'):
        ui.graphicsView_i28.setYRange(signal_i28['Absolute Intensity'].iloc[t1_i28:t2_i28].max(),
                                      signal_i28['Absolute Intensity'].iloc[t1_i28:t2_i28].min())
        change_param_2()


def change_param_1():
    ui.graphicsView_i44.clear()
    t1_1 = ui.doubleSpinBox1_t1.value()
    t2_1 = ui.doubleSpinBox1_t2.value()
    t3_1 = ui.doubleSpinBox1_t3.value()
    bl_1 = ui.spinBox1_bl1.value()
    bl_2 = bl_1 if ui.name1.text() == 'S3/S3\'' else ui.spinBox1_bl2.value()
    file_name = ui.listWidget.item(ui.listWidget.currentRow()).text()
    dir_name = ui.lineEdit_direct.text()
    iWt = -3 if file_name.endswith('ox_ms.txt') else -2
    Wt = float(file_name.split('_')[iWt])
    ion = 0 if ui.label_ion44.text() == 'FID:' else 44
    signal_i44 = select_signal_by_ion(dir_name + '/' + file_name, ion)
    if ui.label_ion44.text() == 'FID:':
        Kg1, Kg2 = float(ui.S1_kg.text()), float(ui.S2_kg.text())
    else:
        if ui.name1.text() == 'S3/S3\'':
            Kg1, Kg2 = float(ui.S3_kg.text()), float(ui.S3__kg.text())
        else:
            Kg1, Kg2 = float(ui.S4CO2_kg.text()), float(ui.S5_kg.text())
    ui.graphicsView_i44.plot(x=signal_i44['Ret.Time'], y=signal_i44['Absolute Intensity'], pen=pg.mkPen(width=2,
                                                                                                        color='r'))
    if ion == 0:
        it1 = signal_i44.loc[signal_i44['Ret.Time'] == get_nearest_value(signal_i44['Ret.Time'], t1_1)].index.tolist()[0]
        it2 = signal_i44.loc[signal_i44['Ret.Time'] == get_nearest_value(signal_i44['Ret.Time'], t2_1)].index.tolist()[0]
        it3 = signal_i44.loc[signal_i44['Ret.Time'] == get_nearest_value(signal_i44['Ret.Time'], t3_1)].index.tolist()[0]
        draw_area(ui.graphicsView_i44, signal_i44, it1, it2, False, '#44944A')
        draw_area(ui.graphicsView_i44, signal_i44, it2, it3, False, '#423189')
        draw_legend(ui.graphicsView_i44, t1_1, t2_1, t3_1, ui.doubleSpinBox_dtmax.value(), ui.graphicsView_i44.viewRange()[1][1])
        draw_tmax(ui.graphicsView_i44, ui.doubleSpinBox_dtmax.value())
        ui.Tmax.setText(str(round((ui.doubleSpinBox_dtmax.value() * 25 + 225) - float(ui.dTmax.text()), 2)))
        area1 = calc_area(signal_i44, it1, it2, False)
        area2 = calc_area(signal_i44, it2, it3, False)
    else:
        draw_area(ui.graphicsView_i44, signal_i44, int((t1_1 / 0.005) - 4), int((t2_1 / 0.005) - 4), bl_1, '#44944A')
        draw_area(ui.graphicsView_i44, signal_i44, int((t2_1 / 0.005) - 4), int((t3_1 / 0.005) - 4), bl_2, '#423189')
        draw_legend(ui.graphicsView_i44, t1_1, t2_1, t3_1, False, ui.graphicsView_i44.viewRange()[1][1])
        area1 = calc_area(signal_i44, int((t1_1 / 0.005) - 4), int((t2_1 / 0.005) - 4), bl_1)
        area2 = calc_area(signal_i44, int((t2_1 / 0.005) - 4), int((t3_1 / 0.005) - 4), bl_2)
    ui.area1.setText('{:.0f}'.format(area1))
    ui.area2.setText('{:.0f}'.format(area2))
    ui.conc1.setText('{:.6f}'.format(calc_Cpr(area1, Kg1, Wt)))
    ui.conc2.setText('{:.6f}'.format(calc_Cpr(area2, Kg2, Wt)))


def change_param_2():
    ui.graphicsView_i28.clear()
    t1_2 = ui.doubleSpinBox2_t1.value()
    t2_2 = ui.doubleSpinBox2_t2.value()
    t3_2 = ui.doubleSpinBox2_t3.value()
    bl = ui.spinBox2_bl.value()
    file_name = ui.listWidget.item(ui.listWidget.currentRow()).text()
    dir_name = ui.lineEdit_direct.text()
    iWt = -3 if file_name.endswith('ox_ms.txt') else -2
    Wt = float(file_name.split('_')[iWt])
    signal_i28 = select_signal_by_ion(dir_name + '/' + file_name, 28)
    ui.graphicsView_i28.plot(x=signal_i28['Ret.Time'], y=signal_i28['Absolute Intensity'], pen=pg.mkPen(width=2,
                                                                                                        color='r'))
    draw_area(ui.graphicsView_i28, signal_i28, int((t1_2 / 0.005) - 4), int((t2_2 / 0.005) - 4), bl, '#44944A')
    draw_legend(ui.graphicsView_i28, t1_2, t2_2, False, False, ui.graphicsView_i28.viewRange()[1][1])
    area3 = calc_area(signal_i28, int((t1_2 / 0.005) - 4), int((t2_2 / 0.005) - 4), bl)
    Kg3 = float(ui.S3CO_kg.text()) if ui.name2.text() == 'S3CO/S3\'CO' else float(ui.S4CO_kg.text())
    ui.area3.setText('{:.0f}'.format(area3))
    ui.conc3.setText('{:.6f}'.format(calc_Cpr(area3, Kg3, Wt)))
    if ui.name2.text() == 'S3CO/S3\'CO':
        draw_area(ui.graphicsView_i28, signal_i28, int((t2_2 / 0.005) - 4), int((t3_2 / 0.005) - 4), bl, '#423189')
        draw_legend(ui.graphicsView_i28, t1_2, t2_2, t3_2, False, ui.graphicsView_i28.viewRange()[1][1])
        area4 = calc_area(signal_i28, int((t2_2 / 0.005) - 4), int((t3_2 / 0.005) - 4), bl)
        ui.area4.setText('{:.0f}'.format(area4))
        ui.conc4.setText('{:.6f}'.format(calc_Cpr(area4, float(ui.S3_CO_kg.text()), Wt)))


def save_change():
    file_name = ui.listWidget.item(ui.listWidget.currentRow()).text()
    if file_name.endswith('ox_ms.txt'):
        obr = '_'.join(file_name.split('_')[:-2])
    else:
        obr = '_'.join(file_name.split('_')[:-1])
    obr_row = tab_areas.loc[tab_areas['obr'] == obr].index.tolist()[0]
    if file_name.endswith('_fid.TXT'):
        dir_name = ui.lineEdit_direct.text()
        signal_i44 = select_signal_by_ion(dir_name + '/' + file_name, 0)
        it1 = signal_i44.loc[signal_i44['Ret.Time'] ==
                             get_nearest_value(signal_i44['Ret.Time'], ui.doubleSpinBox1_t1.value())].index.tolist()[0]
        it2 = signal_i44.loc[signal_i44['Ret.Time'] ==
                             get_nearest_value(signal_i44['Ret.Time'], ui.doubleSpinBox1_t2.value())].index.tolist()[0]
        it3 = signal_i44.loc[signal_i44['Ret.Time'] ==
                             get_nearest_value(signal_i44['Ret.Time'], ui.doubleSpinBox1_t3.value())].index.tolist()[0]
        tab_areas['S1S2_t3'][obr_row] = it3
        tab_areas['S1S2_t2'][obr_row] = it2
        tab_areas['S1S2_t1'][obr_row] = it1
        tab_areas['S1_area'][obr_row] = float(ui.area1.text())
        tab_areas['S2_area'][obr_row] = float(ui.area2.text())
        tab_areas['Tmax'][obr_row] = float(ui.Tmax.text()) + float(ui.dTmax.text())
        tab_areas['S1S2_attn'][obr_row] = False

    elif file_name.endswith('ox_ms.txt'):
        tab_areas['S4CO2_t3'][obr_row] = int((ui.doubleSpinBox1_t3.value() / 0.005) - 4)
        tab_areas['S4CO2_t2'][obr_row] = int((ui.doubleSpinBox1_t2.value() / 0.005) - 4)
        tab_areas['S4CO2_t1'][obr_row] = int((ui.doubleSpinBox1_t1.value() / 0.005) - 4)
        tab_areas['S4CO2_bl'][obr_row] = ui.spinBox1_bl1.value()
        tab_areas['S4CO2_area'][obr_row] = float(ui.area1.text())
        tab_areas['S4CO2m_bl'][obr_row] = ui.spinBox1_bl2.value()
        tab_areas['S5_area'][obr_row] = float(ui.area2.text())
        tab_areas['S4CO2_attn'][obr_row] = False

        tab_areas['S4CO_t2'][obr_row] = int((ui.doubleSpinBox2_t2.value() / 0.005) - 4)
        tab_areas['S4CO_t1'][obr_row] = int((ui.doubleSpinBox2_t1.value() / 0.005) - 4)
        tab_areas['S4CO_bl'][obr_row] = ui.spinBox2_bl.value()
        tab_areas['S4CO_area'][obr_row] = float(ui.area3.text())
        tab_areas['S4CO_attn'][obr_row] = False

    else:
        tab_areas['S3_t3'][obr_row] = int((ui.doubleSpinBox1_t3.value() / 0.005) - 4)
        tab_areas['S3_t2'][obr_row] = int((ui.doubleSpinBox1_t2.value() / 0.005) - 4)
        tab_areas['S3_t1'][obr_row] = int((ui.doubleSpinBox1_t1.value() / 0.005) - 4)
        tab_areas['S3_bl'][obr_row] = ui.spinBox1_bl1.value()
        tab_areas['S3_area'][obr_row] = float(ui.area1.text())
        tab_areas['S3__area'][obr_row] = float(ui.area2.text())
        tab_areas['S3_attn'][obr_row] = False

        tab_areas['S3CO_t3'][obr_row] = int((ui.doubleSpinBox2_t3.value() / 0.005) - 4)
        tab_areas['S3CO_t2'][obr_row] = int((ui.doubleSpinBox2_t2.value() / 0.005) - 4)
        tab_areas['S3CO_t1'][obr_row] = int((ui.doubleSpinBox2_t1.value() / 0.005) - 4)
        tab_areas['S3CO_bl'][obr_row] = ui.spinBox2_bl.value()
        tab_areas['S3CO_area'][obr_row] = ui.area3.text()
        tab_areas['S3_CO_area'][obr_row] = ui.area4.text()
        tab_areas['S3CO_attn'][obr_row] = False
    ui.listWidget.item(ui.listWidget.currentRow()).setBackground(QtGui.QColor(100, 255, 100))
    ui.info.setText('Корректировки интерпретации сохранены - ' + file_name)
    ui.info.setStyleSheet('color: green')
    if Graduation:
        fill_tabs(ui_g, tab_areas)
        calc_mean_RSD(ui_g)


def open_grad():
    file_name_grad = QFileDialog.getOpenFileName( )
    ui.lineEdit_grad.setText(file_name_grad[0])
    tab_grad = pd.read_excel(file_name_grad[0], header=0, index_col=0)
    try:
        ui.S1_kg.setText("{:.6e}".format(tab_grad['Kgrad']['S1']))
        ui.S2_kg.setText("{:.6e}".format(tab_grad['Kgrad']['S2']))
        ui.S3_kg.setText("{:.6e}".format(tab_grad['Kgrad']['S3']))
        ui.S3__kg.setText("{:.6e}".format(tab_grad['Kgrad']['S3_']))
        ui.S3CO_kg.setText("{:.6e}".format(tab_grad['Kgrad']['S3CO']))
        ui.S3_CO_kg.setText("{:.6e}".format(tab_grad['Kgrad']['S3_CO']))
        ui.S4CO2_kg.setText("{:.6e}".format(tab_grad['Kgrad']['S4CO2']))
        ui.S5_kg.setText("{:.6e}".format(tab_grad['Kgrad']['S5']))
        ui.S4CO_kg.setText("{:.6e}".format(tab_grad['Kgrad']['S4CO']))
        ui.dTmax.setText("{:.2f}".format(tab_grad['Kgrad']['Tmax']))
        ui.info.setText('Загружен файл градуировки: ' + file_name_grad[0])
        ui.info.setStyleSheet('color: green')
        if len(tab_areas) != 0:
            print(tab_areas)
            change_param_1()
    except:
        ui.info.setText('Внимание! Ошибка загрузки файла градуировки: ' + file_name_grad[0])
        ui.info.setStyleSheet('color: red')


def save_result():
    tab_result = pd.DataFrame(columns=['name', 'Wt', 'S1', 'S2', 'S3', 'S3_', 'S3CO', 'S3_CO', 'S4CO2', 'S5', 'S4CO',
                                       'Tmax', 'kS1', 'kS2', 'kS3', 'kS3_', 'kS3CO', 'kS3_CO', 'kS4CO2', 'kS5',
                                       'kS4CO', 'dT'])
    for i in tab_areas.index:
        dict_result = {}
        Wt = float(tab_areas['obr'][i].split('_')[-1])
        dict_result['name'] = '_'.join(tab_areas['obr'][i].split('_')[:-1])
        dict_result['Wt'] = Wt
        dict_result['S1'] = calc_Cpr(tab_areas['S1_area'][i], float(ui.S1_kg.text()), Wt)
        dict_result['S2'] = calc_Cpr(tab_areas['S2_area'][i], float(ui.S2_kg.text()), Wt)
        dict_result['S3'] = calc_Cpr(tab_areas['S3_area'][i], float(ui.S3_kg.text()), Wt)
        dict_result['S3_'] = calc_Cpr(tab_areas['S3__area'][i], float(ui.S3__kg.text()), Wt)
        dict_result['S3CO'] = calc_Cpr(tab_areas['S3CO_area'][i], float(ui.S3CO_kg.text()), Wt)
        dict_result['S3_CO'] = calc_Cpr(tab_areas['S3_CO_area'][i], float(ui.S3_CO_kg.text()), Wt)
        dict_result['S4CO2'] = calc_Cpr(tab_areas['S4CO2_area'][i], float(ui.S4CO2_kg.text()), Wt)
        dict_result['S5'] = calc_Cpr(tab_areas['S5_area'][i], float(ui.S5_kg.text()), Wt)
        dict_result['S4CO'] = calc_Cpr(tab_areas['S4CO_area'][i], float(ui.S4CO_kg.text()), Wt)
        dict_result['Tmax'] = tab_areas['Tmax'][i] - float(ui.dTmax.text())
        dict_result['kS1'] = float(ui.S1_kg.text())
        dict_result['kS2'] = float(ui.S2_kg.text())
        dict_result['kS3'] = float(ui.S3_kg.text())
        dict_result['kS3_'] = float(ui.S3__kg.text())
        dict_result['kS3CO'] = float(ui.S3CO_kg.text())
        dict_result['kS3_CO'] = float(ui.S3_CO_kg.text())
        dict_result['kS4CO2'] = float(ui.S4CO2_kg.text())
        dict_result['kS5'] = float(ui.S5_kg.text())
        dict_result['kS4CO'] = float(ui.S4CO_kg.text())
        dict_result['dT'] = float(ui.dTmax.text())
        # tab_result = tab_result.append(dict_result, ignore_index=True)
        tab_result = pd.concat([tab_result, pd.DataFrame([dict_result])], ignore_index=True)
    file_name_result = QFileDialog.getSaveFileName(filter='*.xlsx')
    try:
        tab_result.to_excel(file_name_result[0])
        tab_areas.to_excel(ui.lineEdit_direct.text() + '/areas.xlsx')
        ui.info.setText('Результаты обработки сохранены в файл: ' + file_name_result[0])
        ui.info.setStyleSheet('color: blue')
    except PermissionError:
        ui.info.setText('Внимание! Ошибка сохранения. Возможно открыт файл таблицы результатов.')
        ui.info.setStyleSheet('color: red')


def graduation():
    Graduation.setWindowFlag(QtCore.Qt.WindowStaysOnTopHint)
    Graduation.show()

    fill_tabs(ui_g, tab_areas)
    calc_mean_RSD(ui_g)

    def open_standard():
        file_stand = QFileDialog.getOpenFileName(filter='*.xls *.xlsx')
        tab_stand = pd.read_excel(file_stand[0], header=0, index_col=0)
        ui_g.S1_Cst.setValue(tab_stand['VALUE']['S1'])
        ui_g.S2_Cst.setValue(tab_stand['VALUE']['S2'])
        ui_g.S3_Cst.setValue(tab_stand['VALUE']['S3'])
        ui_g.S3__Cst.setValue(tab_stand['VALUE']['S3_'])
        ui_g.S3CO_Cst.setValue(tab_stand['VALUE']['S3CO'])
        ui_g.S3_CO_Cst.setValue(tab_stand['VALUE']['S3_CO'])
        ui_g.S4CO2_Cst.setValue(tab_stand['VALUE']['S4CO2'])
        ui_g.S5_Cst.setValue(tab_stand['VALUE']['S5'])
        ui_g.S4CO_Cst.setValue(tab_stand['VALUE']['S4CO'])
        ui_g.Tmax_st.setValue(tab_stand['VALUE']['Tmax'])

    def for_save_grad():
        save_grad(ui_g)

    ui_g.pushButton_standart.clicked.connect(open_standard)
    ui_g.pushButton_save_grad.clicked.connect(for_save_grad)

    Graduation.exec_()


def open_manual():
    manual = QtWidgets.QDialog()
    ui_m = Ui_Manual()
    ui_m.setupUi(manual)
    manual.show()

    def open_standart_file():
        subprocess.call('шаблон/стандартный образец.xlsx', shell=True)

    ui_m.pushButton_standart.clicked.connect(open_standart_file)

    manual.exec_()


ui.pushButton_open_dir.clicked.connect(open_dir)
ui.pushButton_save_change.clicked.connect(save_change)
ui.listWidget.itemSelectionChanged.connect(choose_file)
ui.doubleSpinBox1_t1.valueChanged.connect(change_param_1)
ui.doubleSpinBox1_t2.valueChanged.connect(change_param_1)
ui.doubleSpinBox1_t3.valueChanged.connect(change_param_1)
ui.spinBox1_bl1.valueChanged.connect(change_param_1)
ui.spinBox1_bl2.valueChanged.connect(change_param_1)
ui.doubleSpinBox_dtmax.valueChanged.connect(change_param_1)
ui.doubleSpinBox2_t1.valueChanged.connect(change_param_2)
ui.doubleSpinBox2_t2.valueChanged.connect(change_param_2)
ui.doubleSpinBox2_t3.valueChanged.connect(change_param_2)
ui.spinBox2_bl.valueChanged.connect(change_param_2)
ui.pushButton_calc_grad.clicked.connect(graduation)
ui.pushButton_open_grad.clicked.connect(open_grad)
ui.pushButton_save_result.clicked.connect(save_result)
ui.pushButton_manual.clicked.connect(open_manual)

sys.exit(app.exec_())
