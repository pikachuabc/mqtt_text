import sys
import mainwindow
from PyQt5.QtWidgets import QApplication, QMainWindow



if __name__ == '__main__':

    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = mainwindow.Ui_MainWindow()
    ui.setupUi(MainWindow)
    ui.change_label()
    MainWindow.show()
    app.exec_()





