import time
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import QProcess


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()

        self.p = None

        self.initComponents()
        self.changeStatus('standby')

    def initComponents(self):
        """
        Initilize gui components & action definition
        """
        self.btn_bigTask = self.findChild(QtWidgets.QPushButton, "btn_bigTask")
        self.btn_bigTask.pressed.connect(self.handleBtn)
        self.statusLabel = self.findChild(QtWidgets.QLabel, 'statusLabel')
        self.plainTextEdit = self.findChild(
            QtWidgets.QPlainTextEdit, 'plainTextEdit')
        self.txtNum1 = self.findChild(QtWidgets.QLineEdit,'txtNum1')
        self.txtNum2 = self.findChild(QtWidgets.QLineEdit,'txtNum2')

    def handleBtn(self):
        """
        Handles Start button
        """
        if self.p is None:
            self.p = QProcess()
            self.p.stateChanged.connect(self.handle_state)
            self.p.readyReadStandardOutput.connect(self.handle_stdout)
            self.p.readyReadStandardError.connect(self.handle_stderr)
            self.p.finished.connect(self.process_finished)

            num_one = self.txtNum1.text()
            num_two = self.txtNum2.text()

            self.p.start("python", ['dummy.py',str(num_one),str(num_two)])

    def log(self, text: str):
        self.plainTextEdit.appendPlainText(text)

    def handle_stdout(self):
        data = self.p.readAllStandardOutput()
        stdout = bytes(data).decode("utf8")
        self.log(f"Result is: {stdout}")

    def process_finished(self):
        self.changeStatus('standby')
        self.log("Process Finished!")
        self.p = None

    def handle_state(self, state):
        if state == QProcess.Starting:
            pass
            # self.changeStatus('active')
            #self.log("Process started!")
        elif state == QProcess.Running:
            self.changeStatus('active')
            self.log("Process Running!")

    def handle_stderr(self):
        data = self.p.readAllStandardError()
        stderr = bytes(data).decode("utf8")
        error_dialog = QtWidgets.QErrorMessage()
        error_dialog.showMessage(stderr)
        error_dialog.exec_()

    def changeStatus(self, status):
        status_list = {
            'standby': 'white',
            'active': 'lightgreen',
            'error': 'red'
        }
        self.statusLabel.setStyleSheet(
            f'background-color:{status_list[status]}')


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    app.exec_()
