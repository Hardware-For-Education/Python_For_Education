from python_for_education.Hardware_Educacion import *
import python_for_education.s3a as s3a

class MainWindow(QtWidgets.QMainWindow, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        QtWidgets.QMainWindow.__init__(self, *args, **kwargs)
        self.setupUi(self)

        self.pushButton.clicked.connect(self.iniciar)
    def iniciar(self):
        s3a.s3ax()
if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()