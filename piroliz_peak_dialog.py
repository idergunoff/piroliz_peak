# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\USER\PycharmProjects\piroliz_peak\piroliz_peak_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1350, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.graphicsView_i44 = PlotWidget(self.centralwidget)
        self.graphicsView_i44.setGeometry(QtCore.QRect(20, 40, 650, 400))
        self.graphicsView_i44.setObjectName("graphicsView_i44")
        self.graphicsView_i28 = PlotWidget(self.centralwidget)
        self.graphicsView_i28.setGeometry(QtCore.QRect(680, 40, 650, 400))
        self.graphicsView_i28.setObjectName("graphicsView_i28")
        self.label_ion44 = QtWidgets.QLabel(self.centralwidget)
        self.label_ion44.setGeometry(QtCore.QRect(20, 9, 651, 31))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_ion44.sizePolicy().hasHeightForWidth())
        self.label_ion44.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.label_ion44.setFont(font)
        self.label_ion44.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_ion44.setScaledContents(False)
        self.label_ion44.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ion44.setObjectName("label_ion44")
        self.label_ion28 = QtWidgets.QLabel(self.centralwidget)
        self.label_ion28.setGeometry(QtCore.QRect(680, 10, 651, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label_ion28.setFont(font)
        self.label_ion28.setAlignment(QtCore.Qt.AlignCenter)
        self.label_ion28.setObjectName("label_ion28")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 740, 1311, 10))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.info = QtWidgets.QLabel(self.centralwidget)
        self.info.setGeometry(QtCore.QRect(20, 720, 1201, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.info.setFont(font)
        self.info.setObjectName("info")
        self.pushButton_save_change = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_change.setGeometry(QtCore.QRect(160, 540, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_save_change.setFont(font)
        self.pushButton_save_change.setObjectName("pushButton_save_change")
        self.pushButton_open_dir = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_dir.setGeometry(QtCore.QRect(40, 540, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_open_dir.setFont(font)
        self.pushButton_open_dir.setObjectName("pushButton_open_dir")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(280, 530, 401, 181))
        self.listWidget.setObjectName("listWidget")
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(30, 440, 651, 91))
        self.widget1.setObjectName("widget1")
        self.area1 = QtWidgets.QLabel(self.widget1)
        self.area1.setGeometry(QtCore.QRect(360, 30, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.area1.setFont(font)
        self.area1.setObjectName("area1")
        self.label_38 = QtWidgets.QLabel(self.widget1)
        self.label_38.setGeometry(QtCore.QRect(310, 30, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_38.setFont(font)
        self.label_38.setObjectName("label_38")
        self.name1 = QtWidgets.QLabel(self.widget1)
        self.name1.setGeometry(QtCore.QRect(10, 0, 561, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.name1.setFont(font)
        self.name1.setAlignment(QtCore.Qt.AlignCenter)
        self.name1.setObjectName("name1")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.widget1)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 21, 284, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.horizontalLayoutWidget.setFont(font)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.doubleSpinBox1_t1 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox1_t1.setFont(font)
        self.doubleSpinBox1_t1.setDecimals(3)
        self.doubleSpinBox1_t1.setMinimum(0.02)
        self.doubleSpinBox1_t1.setSingleStep(0.005)
        self.doubleSpinBox1_t1.setObjectName("doubleSpinBox1_t1")
        self.horizontalLayout.addWidget(self.doubleSpinBox1_t1)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.doubleSpinBox1_t2 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox1_t2.setFont(font)
        self.doubleSpinBox1_t2.setDecimals(3)
        self.doubleSpinBox1_t2.setMinimum(0.02)
        self.doubleSpinBox1_t2.setSingleStep(0.005)
        self.doubleSpinBox1_t2.setObjectName("doubleSpinBox1_t2")
        self.horizontalLayout.addWidget(self.doubleSpinBox1_t2)
        self.label_5 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.doubleSpinBox1_t3 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox1_t3.setFont(font)
        self.doubleSpinBox1_t3.setDecimals(3)
        self.doubleSpinBox1_t3.setMinimum(0.02)
        self.doubleSpinBox1_t3.setSingleStep(0.005)
        self.doubleSpinBox1_t3.setObjectName("doubleSpinBox1_t3")
        self.horizontalLayout.addWidget(self.doubleSpinBox1_t3)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.widget1)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(10, 50, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.horizontalLayoutWidget_2.setFont(font)
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.spinBox1_bl1 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox1_bl1.setFont(font)
        self.spinBox1_bl1.setMaximum(10000000)
        self.spinBox1_bl1.setSingleStep(50)
        self.spinBox1_bl1.setObjectName("spinBox1_bl1")
        self.horizontalLayout_2.addWidget(self.spinBox1_bl1)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.spinBox1_bl2 = QtWidgets.QSpinBox(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox1_bl2.setFont(font)
        self.spinBox1_bl2.setMaximum(10000000)
        self.spinBox1_bl2.setSingleStep(50)
        self.spinBox1_bl2.setObjectName("spinBox1_bl2")
        self.horizontalLayout_2.addWidget(self.spinBox1_bl2)
        self.area2 = QtWidgets.QLabel(self.widget1)
        self.area2.setGeometry(QtCore.QRect(360, 50, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.area2.setFont(font)
        self.area2.setObjectName("area2")
        self.label_39 = QtWidgets.QLabel(self.widget1)
        self.label_39.setGeometry(QtCore.QRect(310, 50, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_39.setFont(font)
        self.label_39.setObjectName("label_39")
        self.conc1 = QtWidgets.QLabel(self.widget1)
        self.conc1.setGeometry(QtCore.QRect(470, 30, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.conc1.setFont(font)
        self.conc1.setObjectName("conc1")
        self.label_40 = QtWidgets.QLabel(self.widget1)
        self.label_40.setGeometry(QtCore.QRect(440, 30, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_40.setFont(font)
        self.label_40.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_40.setObjectName("label_40")
        self.conc2 = QtWidgets.QLabel(self.widget1)
        self.conc2.setGeometry(QtCore.QRect(470, 50, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.conc2.setFont(font)
        self.conc2.setObjectName("conc2")
        self.label_41 = QtWidgets.QLabel(self.widget1)
        self.label_41.setGeometry(QtCore.QRect(440, 50, 21, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_41.setObjectName("label_41")
        self.Tmax = QtWidgets.QLabel(self.widget1)
        self.Tmax.setGeometry(QtCore.QRect(600, 30, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Tmax.setFont(font)
        self.Tmax.setObjectName("Tmax")
        self.label_46 = QtWidgets.QLabel(self.widget1)
        self.label_46.setGeometry(QtCore.QRect(550, 30, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_46.setFont(font)
        self.label_46.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_46.setObjectName("label_46")
        self.doubleSpinBox_dtmax = QtWidgets.QDoubleSpinBox(self.widget1)
        self.doubleSpinBox_dtmax.setGeometry(QtCore.QRect(560, 50, 65, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox_dtmax.setFont(font)
        self.doubleSpinBox_dtmax.setDecimals(3)
        self.doubleSpinBox_dtmax.setMinimum(0.02)
        self.doubleSpinBox_dtmax.setSingleStep(0.005)
        self.doubleSpinBox_dtmax.setObjectName("doubleSpinBox_dtmax")
        self.pushButton_save_result = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_save_result.setGeometry(QtCore.QRect(40, 670, 221, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_save_result.setFont(font)
        self.pushButton_save_result.setObjectName("pushButton_save_result")
        self.lineEdit_direct = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_direct.setGeometry(QtCore.QRect(40, 590, 221, 20))
        self.lineEdit_direct.setObjectName("lineEdit_direct")
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(680, 440, 651, 91))
        self.widget2.setObjectName("widget2")
        self.area3 = QtWidgets.QLabel(self.widget2)
        self.area3.setGeometry(QtCore.QRect(360, 30, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.area3.setFont(font)
        self.area3.setObjectName("area3")
        self.label_42 = QtWidgets.QLabel(self.widget2)
        self.label_42.setGeometry(QtCore.QRect(310, 30, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setObjectName("label_42")
        self.name2 = QtWidgets.QLabel(self.widget2)
        self.name2.setGeometry(QtCore.QRect(10, 0, 561, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.name2.setFont(font)
        self.name2.setAlignment(QtCore.Qt.AlignCenter)
        self.name2.setObjectName("name2")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.widget2)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(10, 21, 284, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.horizontalLayoutWidget_3.setFont(font)
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        self.doubleSpinBox2_t1 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox2_t1.setFont(font)
        self.doubleSpinBox2_t1.setDecimals(3)
        self.doubleSpinBox2_t1.setMinimum(0.02)
        self.doubleSpinBox2_t1.setSingleStep(0.005)
        self.doubleSpinBox2_t1.setObjectName("doubleSpinBox2_t1")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox2_t1)
        self.label_7 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_3.addWidget(self.label_7)
        self.doubleSpinBox2_t2 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox2_t2.setFont(font)
        self.doubleSpinBox2_t2.setDecimals(3)
        self.doubleSpinBox2_t2.setMinimum(0.02)
        self.doubleSpinBox2_t2.setSingleStep(0.005)
        self.doubleSpinBox2_t2.setObjectName("doubleSpinBox2_t2")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox2_t2)
        self.label_8 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_3.addWidget(self.label_8)
        self.doubleSpinBox2_t3 = QtWidgets.QDoubleSpinBox(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.doubleSpinBox2_t3.setFont(font)
        self.doubleSpinBox2_t3.setDecimals(3)
        self.doubleSpinBox2_t3.setMinimum(0.02)
        self.doubleSpinBox2_t3.setSingleStep(0.005)
        self.doubleSpinBox2_t3.setObjectName("doubleSpinBox2_t3")
        self.horizontalLayout_3.addWidget(self.doubleSpinBox2_t3)
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.widget2)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(70, 50, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.horizontalLayoutWidget_4.setFont(font)
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_9 = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_4.addWidget(self.label_9)
        self.spinBox2_bl = QtWidgets.QSpinBox(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.spinBox2_bl.setFont(font)
        self.spinBox2_bl.setMaximum(10000000)
        self.spinBox2_bl.setSingleStep(50)
        self.spinBox2_bl.setObjectName("spinBox2_bl")
        self.horizontalLayout_4.addWidget(self.spinBox2_bl)
        self.area4 = QtWidgets.QLabel(self.widget2)
        self.area4.setGeometry(QtCore.QRect(360, 50, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.area4.setFont(font)
        self.area4.setObjectName("area4")
        self.label_43 = QtWidgets.QLabel(self.widget2)
        self.label_43.setGeometry(QtCore.QRect(310, 50, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_43.setFont(font)
        self.label_43.setObjectName("label_43")
        self.conc3 = QtWidgets.QLabel(self.widget2)
        self.conc3.setGeometry(QtCore.QRect(490, 30, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.conc3.setFont(font)
        self.conc3.setObjectName("conc3")
        self.label_44 = QtWidgets.QLabel(self.widget2)
        self.label_44.setGeometry(QtCore.QRect(440, 30, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_44.setObjectName("label_44")
        self.conc4 = QtWidgets.QLabel(self.widget2)
        self.conc4.setGeometry(QtCore.QRect(490, 50, 121, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.conc4.setFont(font)
        self.conc4.setObjectName("conc4")
        self.label_45 = QtWidgets.QLabel(self.widget2)
        self.label_45.setGeometry(QtCore.QRect(440, 50, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_45.setFont(font)
        self.label_45.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_45.setObjectName("label_45")
        self.pushButton_calc_grad = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_calc_grad.setGeometry(QtCore.QRect(40, 620, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_calc_grad.setFont(font)
        self.pushButton_calc_grad.setObjectName("pushButton_calc_grad")
        self.pushButton_open_grad = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_open_grad.setGeometry(QtCore.QRect(160, 620, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_open_grad.setFont(font)
        self.pushButton_open_grad.setObjectName("pushButton_open_grad")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(690, 540, 341, 151))
        self.groupBox.setObjectName("groupBox")
        self.label_10 = QtWidgets.QLabel(self.groupBox)
        self.label_10.setGeometry(QtCore.QRect(10, 50, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 70, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 90, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 110, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(10, 130, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(170, 70, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.groupBox)
        self.label_16.setGeometry(QtCore.QRect(170, 90, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(170, 50, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(170, 110, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_18.setObjectName("label_18")
        self.S1_kg = QtWidgets.QLabel(self.groupBox)
        self.S1_kg.setGeometry(QtCore.QRect(60, 50, 101, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S1_kg.setFont(font)
        self.S1_kg.setObjectName("S1_kg")
        self.S3_kg = QtWidgets.QLabel(self.groupBox)
        self.S3_kg.setGeometry(QtCore.QRect(60, 70, 101, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S3_kg.setFont(font)
        self.S3_kg.setObjectName("S3_kg")
        self.S3CO_kg = QtWidgets.QLabel(self.groupBox)
        self.S3CO_kg.setGeometry(QtCore.QRect(60, 90, 101, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S3CO_kg.setFont(font)
        self.S3CO_kg.setObjectName("S3CO_kg")
        self.S4CO2_kg = QtWidgets.QLabel(self.groupBox)
        self.S4CO2_kg.setGeometry(QtCore.QRect(60, 110, 101, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S4CO2_kg.setFont(font)
        self.S4CO2_kg.setObjectName("S4CO2_kg")
        self.S4CO_kg = QtWidgets.QLabel(self.groupBox)
        self.S4CO_kg.setGeometry(QtCore.QRect(60, 130, 101, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S4CO_kg.setFont(font)
        self.S4CO_kg.setObjectName("S4CO_kg")
        self.S2_kg = QtWidgets.QLabel(self.groupBox)
        self.S2_kg.setGeometry(QtCore.QRect(220, 50, 101, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S2_kg.setFont(font)
        self.S2_kg.setObjectName("S2_kg")
        self.S3__kg = QtWidgets.QLabel(self.groupBox)
        self.S3__kg.setGeometry(QtCore.QRect(220, 70, 101, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S3__kg.setFont(font)
        self.S3__kg.setObjectName("S3__kg")
        self.S3_CO_kg = QtWidgets.QLabel(self.groupBox)
        self.S3_CO_kg.setGeometry(QtCore.QRect(220, 90, 101, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S3_CO_kg.setFont(font)
        self.S3_CO_kg.setObjectName("S3_CO_kg")
        self.S5_kg = QtWidgets.QLabel(self.groupBox)
        self.S5_kg.setGeometry(QtCore.QRect(220, 110, 101, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.S5_kg.setFont(font)
        self.S5_kg.setObjectName("S5_kg")
        self.dTmax = QtWidgets.QLabel(self.groupBox)
        self.dTmax.setGeometry(QtCore.QRect(220, 130, 101, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.dTmax.setFont(font)
        self.dTmax.setObjectName("dTmax")
        self.label_19 = QtWidgets.QLabel(self.groupBox)
        self.label_19.setGeometry(QtCore.QRect(170, 130, 47, 13))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_19.setObjectName("label_19")
        self.lineEdit_grad = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_grad.setGeometry(QtCore.QRect(10, 20, 321, 21))
        self.lineEdit_grad.setObjectName("lineEdit_grad")
        self.pushButton_manual = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_manual.setGeometry(QtCore.QRect(1220, 680, 101, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_manual.setFont(font)
        self.pushButton_manual.setObjectName("pushButton_manual")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1350, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PirolizPeak"))
        self.label_ion44.setText(_translate("MainWindow", "ION 44:"))
        self.label_ion28.setText(_translate("MainWindow", "ION 28:"))
        self.info.setText(_translate("MainWindow", "INFO"))
        self.pushButton_save_change.setText(_translate("MainWindow", "Сохранить\n"
"изменения"))
        self.pushButton_open_dir.setText(_translate("MainWindow", "Выбрать\n"
"каталог"))
        self.area1.setText(_translate("MainWindow", "0000000000"))
        self.label_38.setText(_translate("MainWindow", "Area1:"))
        self.name1.setText(_translate("MainWindow", "S3/S3\'"))
        self.label.setText(_translate("MainWindow", "t1:"))
        self.label_2.setText(_translate("MainWindow", "t2:"))
        self.label_5.setText(_translate("MainWindow", "t3:"))
        self.label_3.setText(_translate("MainWindow", "BL1:"))
        self.label_4.setText(_translate("MainWindow", "BL2:"))
        self.area2.setText(_translate("MainWindow", "0000000000"))
        self.label_39.setText(_translate("MainWindow", "Area2:"))
        self.conc1.setText(_translate("MainWindow", "0000000000"))
        self.label_40.setText(_translate("MainWindow", "C1:"))
        self.conc2.setText(_translate("MainWindow", "0000000000"))
        self.label_41.setText(_translate("MainWindow", "C2:"))
        self.Tmax.setText(_translate("MainWindow", "00000"))
        self.label_46.setText(_translate("MainWindow", "Tmax:"))
        self.pushButton_save_result.setText(_translate("MainWindow", "Сохранить результат"))
        self.area3.setText(_translate("MainWindow", "0000000000"))
        self.label_42.setText(_translate("MainWindow", "Area3:"))
        self.name2.setText(_translate("MainWindow", "S3CO/S3\'CO"))
        self.label_6.setText(_translate("MainWindow", "t1:"))
        self.label_7.setText(_translate("MainWindow", "t2:"))
        self.label_8.setText(_translate("MainWindow", "t3:"))
        self.label_9.setText(_translate("MainWindow", "BL:"))
        self.area4.setText(_translate("MainWindow", "0000000000"))
        self.label_43.setText(_translate("MainWindow", "Area4:"))
        self.conc3.setText(_translate("MainWindow", "0000000000"))
        self.label_44.setText(_translate("MainWindow", "C3:"))
        self.conc4.setText(_translate("MainWindow", "0000000000"))
        self.label_45.setText(_translate("MainWindow", "C4:"))
        self.pushButton_calc_grad.setText(_translate("MainWindow", "Выполнить\n"
"градуировку"))
        self.pushButton_open_grad.setText(_translate("MainWindow", "Загрузить\n"
"градуировку"))
        self.groupBox.setTitle(_translate("MainWindow", "Градуировочные коэффициенты"))
        self.label_10.setText(_translate("MainWindow", "S1:"))
        self.label_11.setText(_translate("MainWindow", "S3:"))
        self.label_12.setText(_translate("MainWindow", "S3CO:"))
        self.label_13.setText(_translate("MainWindow", "S4CO2:"))
        self.label_14.setText(_translate("MainWindow", "S4CO:"))
        self.label_15.setText(_translate("MainWindow", "S3\':"))
        self.label_16.setText(_translate("MainWindow", "S3\'CO:"))
        self.label_17.setText(_translate("MainWindow", "S2:"))
        self.label_18.setText(_translate("MainWindow", "S5:"))
        self.S1_kg.setText(_translate("MainWindow", "0"))
        self.S3_kg.setText(_translate("MainWindow", "0"))
        self.S3CO_kg.setText(_translate("MainWindow", "0"))
        self.S4CO2_kg.setText(_translate("MainWindow", "0"))
        self.S4CO_kg.setText(_translate("MainWindow", "0"))
        self.S2_kg.setText(_translate("MainWindow", "0"))
        self.S3__kg.setText(_translate("MainWindow", "0"))
        self.S3_CO_kg.setText(_translate("MainWindow", "0"))
        self.S5_kg.setText(_translate("MainWindow", "0"))
        self.dTmax.setText(_translate("MainWindow", "0"))
        self.label_19.setText(_translate("MainWindow", "dT:"))
        self.pushButton_manual.setText(_translate("MainWindow", "Инструкция"))
from pyqtgraph import PlotWidget


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
