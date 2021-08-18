from PyQt5 import QtCore, QtGui, QtWidgets
from translate import Translator

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 367)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(110, 280, 141, 51))
        self.pushButton.setStyleSheet("background-color: rgb(255, 246, 143);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(520, 280, 141, 51))
        self.pushButton_2.setStyleSheet("background-color: rgb(255, 246, 143);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 90, 261, 161))
        self.textEdit.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(450, 90, 261, 161))
        self.textEdit_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.textEdit_2.setObjectName("textEdit_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(300, 160, 151, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 121, 31))
        self.lineEdit.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(520, 50, 121, 31))
        self.lineEdit_2.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 10, 181, 41))
        self.label.setStyleSheet("font: 22pt \"NSimSun\";\n"
"color: rgb(255, 94, 110);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def trans(self):
        from_lang = self.lineEdit.text()
        to_lang = self.lineEdit_2.text()
        tx1 = self.textEdit.toPlainText()

        t = Translator(from_lang=from_lang, to_lang=to_lang)
        tr = t.translate(tx1)

        self.textEdit_2.setText(tr)

    def update(self):
        # self.lineEdit.setText("")
        # self.lineEdit_2.setText("")

        self.textEdit.setText("")
        self.textEdit_2.setText("")





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "перевести"))
        self.pushButton.clicked.connect(self.trans)

        self.pushButton_2.setText(_translate("MainWindow", "обновить"))
        self.pushButton_2.clicked.connect(self.update)

        self.label.setText(_translate("MainWindow", "Translator"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
