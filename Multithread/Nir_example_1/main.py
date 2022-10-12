import time
import sys
from PyQt5 import uic, QtWidgets
from PyQt5.QtCore import pyqtSignal, QObject, QRunnable, QThreadPool, pyqtSlot


class delayWorkerSignals(QObject):
    start = pyqtSignal()
    end = pyqtSignal()
    progress = pyqtSignal(int)


class delayWorker(QRunnable):
    def __init__(self, timeDelay):
        super(delayWorker, self).__init__()
        self.signals = delayWorkerSignals()

        self.timeDelay = timeDelay

    @pyqtSlot()
    def run(self):
        self.signals.start.emit()
        time.sleep(0.5)
        # work can be done also on the gui thread and pass the function from gui thread to be done on the worker, but do not change gui elements
        for i in range(self.timeDelay):
            progress = int(((i+1)/self.timeDelay) * 100)
            self.signals.progress.emit(progress)
            time.sleep(1)

        self.signals.end.emit()


class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('main.ui', self)
        self.show()

        self.initComponents()

        self.threadpool = QThreadPool()

    def initComponents(self):

        self.txtSET = self.findChild(QtWidgets.QLineEdit, 'txtSET')
        self.txtRemain = self.findChild(QtWidgets.QLineEdit, 'txtRemain')

        self.btnStart = self.findChild(QtWidgets.QPushButton, 'btnStart')
        self.btnStart.pressed.connect(self.handleBtn)

        self.progressBar = self.findChild(
            QtWidgets.QProgressBar, 'progressBar')
        self.progressBar.setValue(0)

    def handleStart(self):
        self.btnStart.setEnabled(False)

    def handleStop(self):
        self.progressBar.setValue(0)
        self.btnStart.setEnabled(True)

    def handleProgress(self, percent):
        self.progressBar.setValue(percent)
        timeDelay = int(self.txtSET.text())
        timePassed = int(timeDelay * (percent/100))

        self.txtRemain.setText(str(timeDelay - timePassed))

    def handleBtn(self):
        try:
            timeDelay = int(self.txtSET.text())
        except:
            print('error with text field')
            return

        worker = delayWorker(timeDelay)
        worker.signals.start.connect(self.handleStart)
        worker.signals.progress.connect(self.handleProgress)
        worker.signals.end.connect(self.handleStop)
        self.threadpool.start(worker)


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Main()
    app.exec_()
