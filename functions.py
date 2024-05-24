import pandas as pd
from PyQt5.QtWidgets import QApplication, QFileDialog, QCheckBox, QTableWidgetItem, QWidget, QHBoxLayout, QDoubleSpinBox
import pyqtgraph as pg
from numpy import mean, std, max, trapz
import chardet
from piroliz_peak_dialog import *
from graduation_dialog import *


def check_encoding(file_name):
    with open(file_name, 'rb') as f:
        return chardet.detect(f.read())['encoding']


def check_file_name(list_name):
    """проверка названий файлов на совпадение веса у файлов трёх типов"""
    check_list, error_list = [], []
    for i in list_name:
        if not i.endswith('.xlsx'):
            if i.endswith('ox_ms.txt'):
                check_list.append('_'.join(i.split('_')[:-2]))
            elif i.endswith('_fid.TXT') or i.endswith('_ms.txt'):
                check_list.append('_'.join(i.split('_')[:-1]))
    for i in check_list:
        if check_list.count(i) != 3:
            error_list.append(i)
    return error_list


def select_signal_by_ion(file_name: str, ion: int):

    enc = check_encoding(file_name)
    def check_first_column(f_n, check_str):
        print(f_n)
        with open(f_n, encoding=enc) as f:
            empt = 0
            for idx, line in enumerate(f):
                if line.strip() == '':
                    empt += 1
                if line.strip().startswith(check_str):
                    return idx - empt
            return None

    if ion == 0:
        calc_head = check_first_column(file_name, 'R.Time')
        print(calc_head)
        all_signals = pd.read_table(file_name, sep='\t', header=calc_head, encoding=enc)
        print(all_signals)
        all_signals = all_signals.rename(columns={'Intensity': 'Absolute Intensity', 'R.Time': 'Ret.Time'})
        print(all_signals)
        for index_signal in all_signals.index:
            if all_signals['Ret.Time'][index_signal] == '[Chromatogram Additional (Ch1)]':
                index_ion_finish = index_signal - 1
                break
        index_ion_start = 0
    else:
        calc_head = check_first_column(file_name, 'Ret.Time')
        all_signals = pd.read_table(file_name, sep='\t', header=calc_head, encoding=enc)
        str_ion = '1-1 {}.00'.format(str(ion))
        index_ion = all_signals.loc[all_signals['Ret.Time'] == 'm/z'].loc[all_signals['Absolute Intensity'] ==
                                                                          str_ion].index.tolist()[0]
        for index_signal in all_signals.iloc[index_ion:].index:
            if all_signals['Ret.Time'][index_signal] == 'Ret.Time':
                index_ion_start = index_signal + 1
            if all_signals['Ret.Time'][index_signal] == '[MS Chromatogram]':
                index_ion_finish = index_signal - 1
                break

    signal_ion = all_signals.iloc[index_ion_start:index_ion_finish].reset_index()
    signal_ion['Absolute Intensity'] = signal_ion['Absolute Intensity'].astype(float)
    signal_ion['Ret.Time'] = signal_ion['Ret.Time'].astype(float)
    if file_name.endswith('_fid.TXT'):
        if signal_ion['Absolute Intensity'].min() < 0:
            signal_ion['Absolute Intensity'] = signal_ion['Absolute Intensity'] + \
                                               abs(signal_ion['Absolute Intensity'].min())
    return signal_ion


def find_intersection_zero(signal: list, min_window: int):
    """
    функция расчёта точек пересечения кривой с нулём
    :param signal: кривая в виде списка
    :param min_window: максимальная ширина шума, который не учитывается
    :return: на выходе два списка индексов: 1 - пересечения снизу-вверх, 2 - пересечения сверху вниз
    """
    bottom_up = [0]
    up_bottom = [0]
    up, down = 0, 0     # индексы последних положительного (up) и отрицательного (down) значений
    for n, i in enumerate(signal):                                      # для проверки min_window ^^^
        if i > 0:
            up = n
            if n - down > min_window and bottom_up[-1] <= up_bottom[-1]:
                bottom_up.append(down)
        else:
            down = n
            if n - up > min_window and up_bottom[-1] <= bottom_up[-1]:
                up_bottom.append(up)

    def remove_zero(the_list):
        return [value for value in the_list if value != 0]
    bottom_up = remove_zero(bottom_up)
    up_bottom = remove_zero(up_bottom)

    return [bottom_up, up_bottom]


def calc_area(line, it1, it2, base_line):
    if not base_line:
        a = line['Absolute Intensity'][it1]
        b = line['Absolute Intensity'][it2]
        # area = (line['Absolute Intensity'].iloc[it1:it2].sum() - (a + b)*(it2 - it2)*0.5) * 60 * 0.00066667
        area = (trapz(line['Absolute Intensity'].iloc[it1:it2], line['Ret.Time'].iloc[it1:it2]) - (
                    a + b) * (line['Ret.Time'][it2] - line['Ret.Time'][it1]) * 0.5) * 60
    else:
        # area = (line['Absolute Intensity'].iloc[it1:it2].sum() - base_line * (it2 - it1)) * 60 * 0.005
        area = (trapz(line['Absolute Intensity'].iloc[it1:it2], line['Ret.Time'].iloc[it1:it2]) -
                base_line * (line['Ret.Time'][it2] - line['Ret.Time'][it1])) * 60
    return area


def calc_Cpr(area, Kgrad, Wt):
    return area * Kgrad / Wt


def draw_area(graphicsView, line, it1, it2, base_line, color):
    if not base_line:
        graphicsView.plot(x=[line['Ret.Time'][it1], line['Ret.Time'][it2]],
                          y=[line['Absolute Intensity'][it1], line['Absolute Intensity'][it2]],
                          pen=pg.mkPen(color=color, width=2))
    else:
        graphicsView.plot(x=[line['Ret.Time'][it1], line['Ret.Time'][it2]], y=[base_line, base_line],
                          pen=pg.mkPen(color=color, width=2))
        graphicsView.plot(x=[line['Ret.Time'][it1], line['Ret.Time'][it1]], y=[base_line, line['Absolute Intensity'][it1]],
                          pen=pg.mkPen(color=color, width=2))
        graphicsView.plot(x=[line['Ret.Time'][it2], line['Ret.Time'][it2]],
                          y=[base_line, line['Absolute Intensity'][it2]],
                          pen=pg.mkPen(color=color, width=2))
    it1_line = pg.InfiniteLine(pos=line['Ret.Time'][it1], angle=90, pen=pg.mkPen(color=color, width=1.2, dash=[2, 6]))
    graphicsView.addItem(it1_line)
    it2_line = pg.InfiniteLine(pos=line['Ret.Time'][it2], angle=90, pen=pg.mkPen(color=color, width=1.2, dash=[6, 2]))
    graphicsView.addItem(it2_line)
    phigh = pg.PlotDataItem(x=line['Ret.Time'].iloc[it1:it2].tolist(), y=line['Absolute Intensity'].iloc[it1:it2].tolist(), pen='k')
    if not base_line:
        plow = pg.PlotCurveItem([line['Ret.Time'][it1], line['Ret.Time'][it2]],
                                [line['Absolute Intensity'][it1], line['Absolute Intensity'][it2]], pen='k')
    else:
        plow = pg.PlotCurveItem([line['Ret.Time'][it1], line['Ret.Time'][it2]], [base_line, base_line], pen='k')
    pfill = pg.FillBetweenItem(phigh, plow, brush=color+'80')
    graphicsView.addItem(pfill)


def draw_legend(graphicsView, xt1, xt2, xt3, xtmax, h):
    t1 = pg.TextItem('t1', color='k')
    t2 = pg.TextItem('t2', color='k')
    t3 = pg.TextItem('t3', color='k')
    tmax = pg.TextItem('Tmax', color='r')
    graphicsView.addItem(t1)
    t1.setPos(xt1, h)
    graphicsView.addItem(t2)
    t2.setPos(xt2, h)
    if xt3:
        graphicsView.addItem(t3)
        t3.setPos(xt3, h)
    if xtmax:
        graphicsView.addItem(tmax)
        tmax.setPos(xtmax, h)


def draw_tmax(graphicsView, ttmax):
    tmax_line = pg.InfiniteLine(pos=ttmax, angle=90, pen=pg.mkPen(color='#FF2400', width=1.2, dash=[2, 2]))
    graphicsView.addItem(tmax_line)


def calc_S1S2(line):
    it1 = find_intersection_zero(line['Absolute Intensity'].diff(), 6)[0][0]
    it2 = line.loc[line['Ret.Time'] == get_nearest_value(line['Ret.Time'], 3.4)].index.tolist()[0]
    it3 = line.loc[line['Ret.Time'] == get_nearest_value(line['Ret.Time'], 17)].index.tolist()[0]
    area1 = calc_area(line, it1, it2, False)
    area2 = calc_area(line, it2, it3, False)
    attention = True if area1 < 0 or area2 < 0 or it1 > 200 else False
    return it1, it2, it3, area1, area2, attention


def calc_Tmax(line):
    tTmax = line['Ret.Time'].iloc[5100:25500].loc[line['Absolute Intensity'] ==
                                                  line['Absolute Intensity'].iloc[5100:25500].max()].tolist()[0]
    return tTmax


def calc_S3(line):
    it1 = find_intersection_zero(line['Absolute Intensity'].diff(), 6)[0][0]
    it2 = line.loc[line['Ret.Time'] == 7].index.tolist()[0]
    base_line = line['Absolute Intensity'].iloc[100:it2].min()
    if line['Absolute Intensity'][len(line['Ret.Time']) - 1] > base_line:
        it3 = len(line['Ret.Time']) - 1
    else:
        it3 = line.iloc[it2:].loc[line['Absolute Intensity'].iloc[it2:] ==
                                  get_nearest_value(line['Absolute Intensity'].iloc[it2:], base_line)].index.tolist()[0]
    area1 = calc_area(line, it1, it2, base_line)
    area2 = calc_area(line, it2, it3, base_line)
    attention = True if area1 < 0 or area2 < 0 or it1 > 40 or it3 < 3600 else False
    return it1, it2, it3, base_line, area1, area2, attention


def calc_S3CO(line):
    it1 = line.iloc[:2600].loc[line['Absolute Intensity'] == line['Absolute Intensity'].iloc[:2600].min()].index.tolist()[0]
    it2 = line.loc[line['Ret.Time'] == 13].index.tolist()[0]
    it3 = len(line['Ret.Time']) - 1
    base_line = line['Absolute Intensity'].min()
    area1 = calc_area(line, it1, it2, base_line)
    area2 = calc_area(line, it2, it3, base_line)
    attention = True if area1 < 0 or area2 < 0 or it1 < 200 or it1 > 1400 else False
    return it1, it2, it3, base_line, area1, area2, attention


def calc_S4CO2(line):
    attention = False
    it1 = line.iloc[600:1000].loc[line['Absolute Intensity'] == line['Absolute Intensity'].iloc[600:1000].min()].index.tolist()[0]
    minimums = find_intersection_zero(calc_diff(line['Absolute Intensity'], 50), 35)[0]
    it2 = 0
    for i in minimums:
        if 1000 < i < 1400:
            it2 = i
            break
    if it2 == 0:
        attention = True
        minimums2 = find_intersection_zero(calc_diff3(line['Absolute Intensity'], 150), 35)
        for i in minimums2[1]:
            if 1020 < i < 1420:
                it2 = i
                break
    if it2 == 0:
        minimums2 = find_intersection_zero(calc_diff2(line['Absolute Intensity'], 100), 35)
        for i in minimums2[0]:
            if 1100 < i < 1400:
                it2 = i
                break
    it3 = len(line['Ret.Time']) - 1
    base_line1 = line['Absolute Intensity'].iloc[600:1000].min()
    base_line2 = line['Absolute Intensity'].iloc[1000:].min()
    area1 = calc_area(line, it1, it2, base_line1)
    area2 = calc_area(line, it2, it3, base_line2)
    if not attention:
        attention = True if area1 < 0 or area2 < 0 or it1 < 200 else False
    return it1, it2, it3, base_line1, base_line2, area1, area2, attention


def calc_S4CO(line):
    attention = False
    it1 = line.iloc[600:1000].loc[line['Absolute Intensity'] == line['Absolute Intensity'].iloc[600:1000].min()].index.tolist()[0]
    minimums = find_intersection_zero(calc_diff(line['Absolute Intensity'], 50), 35)[0]
    it2 = 0
    for i in minimums:
        if 1000 < i < 1400:
            it2 = i
            break
    if it2 == 0:
        attention = True
        minimums2 = find_intersection_zero(calc_diff3(line['Absolute Intensity'], 150), 35)
        for i in minimums2[1]:
            if 1020 < i < 1420:
                it2 = i
                break
    if it2 == 0:
        minimums2 = find_intersection_zero(calc_diff2(line['Absolute Intensity'], 100), 35)
        for i in minimums2[0]:
            if 1100 < i < 1400:
                it2 = i
                break
    base_line = line['Absolute Intensity'].iloc[600:1000].min()
    area = calc_area(line, it1, it2, base_line)
    if not attention:
        attention = True if area < 0 or it1 < 200 else False
    return it1, it2, base_line, area, attention


def get_nearest_value(iterable, value):
    """ функция поиска ближайщего значения """
    return min(iterable, key=lambda x: abs(x - value))


def calc_diff(sig, smooth):
    sig_diff = sig.rolling(smooth, min_periods=1, center=True).mean().diff().rolling(
        smooth, min_periods=1, center=True).mean()
    return sig_diff


def calc_diff2(sig, smooth):
    sig_diff2 = sig.rolling(smooth, min_periods=1, center=True).mean().diff().rolling(
        smooth, min_periods=1, center=True).mean().diff().rolling(smooth, min_periods=1, center=True).mean()
    return sig_diff2


def calc_diff3(sig, smooth):
    sig_diff3 = sig.rolling(smooth, min_periods=1, center=True).mean().diff().rolling(
        smooth, min_periods=1, center=True).mean().diff().rolling(
        smooth, min_periods=1, center=True).mean().diff().rolling(smooth, min_periods=1, center=True).mean()
    return sig_diff3


def fill_tab_grad(tab, tab_res, param):
    """заполнение таблицы градуировки для каждого параметра"""
    row_count = tab.rowCount()
    for i in range(row_count + 1):
        tab.removeRow(row_count - i)
    for i in tab_res.index:
        tab.insertRow(i)
        tab.setItem(i, 0, QTableWidgetItem(tab_res['obr'][i]))
        if param == 'Tmax':
            tab.setItem(i, 1, QTableWidgetItem(str(int(tab_res[param][i]))))
        else:
            tab.setItem(i, 1, QTableWidgetItem(str(int(tab_res[param + '_area'][i]))))
        widget = QWidget()
        checkbox = QCheckBox()
        checkbox.setChecked(True)
        layoutH = QHBoxLayout(widget)
        layoutH.addWidget(checkbox)
        layoutH.setAlignment(QtCore.Qt.AlignCenter)
        layoutH.setContentsMargins(0, 0, 0, 0)
        tab.setCellWidget(i, 2, widget)
    tab.resizeColumnsToContents()


def calc_RSD(table, C_st, Tmax):
    """расчет среднего, коэффициента вариации градуировочного коэффицента для значений в таблице с проверкой
    чекбоксов """
    checked_list, wt_list = [], []
    for i in range(table.rowCount()):
        if table.cellWidget(i, 2).findChild(type(QCheckBox())).isChecked():
            checked_list.append(int(table.item(i, 1).text()))
            wt_list.append(float(table.item(i, 0).text().split('_')[-1]))
    mean_area = float(mean(checked_list))
    RSD = round((std(checked_list, ddof=1) * 100 / mean_area), 2)
    wt_mean = mean(wt_list)
    if Tmax:
        k_grad = mean_area - C_st
    else:
        k_grad = C_st * wt_mean / mean_area
    i_critic = find_critic_value(checked_list)

    return mean_area, RSD, wt_mean, k_grad, i_critic


def fill_tabs(form, tab_areas):
    """заполняем все таблицы по параметрам"""
    def check_for_calc_mean_RSD():
        """функция для сигнала нажатия чекбокcа"""
        calc_mean_RSD(form)
    fill_tab_grad(form.tableWidget_S1, tab_areas, 'S1')
    fill_tab_grad(form.tableWidget_S2, tab_areas, 'S2')
    fill_tab_grad(form.tableWidget_S3, tab_areas, 'S3')
    fill_tab_grad(form.tableWidget_S3_, tab_areas, 'S3_')
    fill_tab_grad(form.tableWidget_S3CO, tab_areas, 'S3CO')
    fill_tab_grad(form.tableWidget_S3_CO, tab_areas, 'S3_CO')
    fill_tab_grad(form.tableWidget_S4CO2, tab_areas, 'S4CO2')
    fill_tab_grad(form.tableWidget_S5, tab_areas, 'S5')
    fill_tab_grad(form.tableWidget_S4CO, tab_areas, 'S4CO')
    fill_tab_grad(form.tableWidget_Tmax, tab_areas, 'Tmax')
    for i in form.tabWidget.findChildren(type(QCheckBox())):
        i.stateChanged.connect(check_for_calc_mean_RSD)
    for i in form.tabWidget.findChildren(type(QDoubleSpinBox())):
        i.valueChanged.connect(check_for_calc_mean_RSD)


def calc_mean_RSD(form):
    """расчет статистических параметров для всех параметров"""

    mean_S1, RSD_S1, wt_S1, Kg_S1, crit_S1 = calc_RSD(form.tableWidget_S1, form.S1_Cst.value(), False)
    form.S1_mean.setText("{:.3f}".format(mean_S1))
    form.S1_RSD.setText(str(RSD_S1))
    form.S1_wt.setText(str(wt_S1))
    form.S1_Kg.setText("{:.6e}".format(Kg_S1))
    draw_cell(form.tableWidget_S1, crit_S1)
    mean_S2, RSD_S2, wt_S2, Kg_S2, crit_S2 = calc_RSD(form.tableWidget_S2, form.S2_Cst.value(), False)
    form.S2_mean.setText("{:.3f}".format(mean_S2))
    form.S2_RSD.setText(str(RSD_S2))
    form.S2_wt.setText(str(wt_S2))
    form.S2_Kg.setText("{:.6e}".format(Kg_S2))
    draw_cell(form.tableWidget_S2, crit_S2)
    mean_S3, RSD_S3, wt_S3, Kg_S3, crit_S3 = calc_RSD(form.tableWidget_S3, form.S3_Cst.value(), False)
    form.S3_mean.setText("{:.3f}".format(mean_S3))
    form.S3_RSD.setText(str(RSD_S3))
    form.S3_wt.setText(str(wt_S3))
    form.S3_Kg.setText("{:.6e}".format(Kg_S3))
    draw_cell(form.tableWidget_S3, crit_S3)
    mean_S3_, RSD_S3_, wt_S3_, Kg_S3_, crit_S3_ = calc_RSD(form.tableWidget_S3_, form.S3__Cst.value(), False)
    form.S3__mean.setText("{:.3f}".format(mean_S3_))
    form.S3__RSD.setText(str(RSD_S3_))
    form.S3__wt.setText(str(wt_S3_))
    form.S3__Kg.setText("{:.6e}".format(Kg_S3_))
    draw_cell(form.tableWidget_S3_, crit_S3_)
    mean_S3CO, RSD_S3CO, wt_S3CO, Kg_S3CO, crit_S3CO = calc_RSD(form.tableWidget_S3CO, form.S3CO_Cst.value(), False)
    form.S3CO_mean.setText("{:.3f}".format(mean_S3CO))
    form.S3CO_RSD.setText(str(RSD_S3CO))
    form.S3CO_wt.setText(str(wt_S3CO))
    form.S3CO_Kg.setText("{:.6e}".format(Kg_S3CO))
    draw_cell(form.tableWidget_S3CO, crit_S3CO)
    mean_S3_CO, RSD_S3_CO, wt_S3_CO, Kg_S3_CO, crit_S3_CO = calc_RSD(form.tableWidget_S3_CO, form.S3_CO_Cst.value(), False)
    form.S3_CO_mean.setText("{:.3f}".format(mean_S3_CO))
    form.S3_CO_RSD.setText(str(RSD_S3_CO))
    form.S3_CO_wt.setText(str(wt_S3_CO))
    form.S3_CO_Kg.setText("{:.6e}".format(Kg_S3_CO))
    draw_cell(form.tableWidget_S3_CO, crit_S3_CO)
    mean_S4CO2, RSD_S4CO2, wt_S4CO2, Kg_S4CO2, crit_S4CO2 = calc_RSD(form.tableWidget_S4CO2, form.S4CO2_Cst.value(), False)
    form.S4CO2_mean.setText("{:.3f}".format(mean_S4CO2))
    form.S4CO2_RSD.setText(str(RSD_S4CO2))
    form.S4CO2_wt.setText(str(wt_S4CO2))
    form.S4CO2_Kg.setText("{:.6e}".format(Kg_S4CO2))
    draw_cell(form.tableWidget_S4CO2, crit_S4CO2)
    mean_S5, RSD_S5, wt_S5, Kg_S5, crit_S5 = calc_RSD(form.tableWidget_S5, form.S5_Cst.value(), False)
    form.S5_mean.setText("{:.3f}".format(mean_S5))
    form.S5_RSD.setText(str(RSD_S5))
    form.S5_wt.setText(str(wt_S5))
    form.S5_Kg.setText("{:.6e}".format(Kg_S5))
    draw_cell(form.tableWidget_S5, crit_S5)
    mean_S4CO, RSD_S4CO, wt_S4CO, Kg_S4CO, crit_S4CO = calc_RSD(form.tableWidget_S4CO, form.S4CO_Cst.value(), False)
    form.S4CO_mean.setText("{:.3f}".format(mean_S4CO))
    form.S4CO_RSD.setText(str(RSD_S4CO))
    form.S4CO_wt.setText(str(wt_S4CO))
    form.S4CO_Kg.setText("{:.6e}".format(Kg_S4CO))
    draw_cell(form.tableWidget_S4CO, crit_S4CO)
    mean_Tmax, RSD_Tmax, wt_Tmax, Kg_Tmax, crit_Tmax = calc_RSD(form.tableWidget_Tmax, form.Tmax_st.value(), True)
    form.Tmax_mean.setText("{:.2f}".format(mean_Tmax))
    form.Tmax_RSD.setText(str(RSD_Tmax))
    form.dTmax.setText("{:.2f}".format(Kg_Tmax))
    draw_cell(form.tableWidget_Tmax, crit_Tmax)


def find_critic_value(list_value):
    list_dist = list(abs(i - mean(list_value)) for i in list_value)
    i_critic = list_dist.index(max(list_dist))
    return list_value[i_critic]


def draw_cell(tab, value):
    for i in range(tab.rowCount()):
        if tab.item(i, 1).text() == str(value):
            tab.item(i, 1).setBackground(QtGui.QColor(255, 100, 100))
        else:
            tab.item(i, 1).setBackground(QtGui.QColor(255, 255, 255))


def save_grad(form):
    tab_grad = pd.DataFrame(index=['S1', 'S2', 'S3', 'S3_', 'S3CO', 'S3_CO', 'S4CO2', 'S5', 'S4CO', 'Tmax'], columns=['Kgrad'])
    tab_grad['Kgrad']['S1'] = float(form.S1_Kg.text())
    tab_grad['Kgrad']['S2'] = float(form.S2_Kg.text())
    tab_grad['Kgrad']['S3'] = float(form.S3_Kg.text())
    tab_grad['Kgrad']['S3_'] = float(form.S3__Kg.text())
    tab_grad['Kgrad']['S3CO'] = float(form.S3CO_Kg.text())
    tab_grad['Kgrad']['S3_CO'] = float(form.S3_CO_Kg.text())
    tab_grad['Kgrad']['S4CO2'] = float(form.S4CO2_Kg.text())
    tab_grad['Kgrad']['S5'] = float(form.S5_Kg.text())
    tab_grad['Kgrad']['S4CO'] = float(form.S4CO_Kg.text())
    tab_grad['Kgrad']['Tmax'] = float(form.dTmax.text())
    file_name_grad = QFileDialog.getSaveFileName(filter='*.xlsx')
    tab_grad.to_excel(file_name_grad[0])
