from PyQt5.QtWidgets import*
from li import*

app=QApplication([])
class MainWindow(QMainWindow):
    def _init_(self):
        super()._init_()
        self.ui=Ui_MainWindow
        self.ui.setupUi(self)
        self.readfile()
    def ReadFile(self):
        with open ("notes.txt",'r', encoding='utf-8') as file:
            self.ui.textEdit.setText(file.read())

ex=MainWindow()
ex.show()
app.exec_()