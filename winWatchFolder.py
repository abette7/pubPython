### Simple watch/hot folder with gui.

import logging
import random
import sys
import time
import os
import time
import shutil

inFolder = "C:/Users/myUser/Desktop/watch_folder" # folder to watch
ot_folder = "P:/Ingest/Ready" #final destination
collateral_folder = "D:/Collateral/" #backup of file lands here
network_temp_folder = "P:/Ingest/Temp/" #temporary landing zone on the same volume as final destination


from PySide6.QtCore import QRunnable, Qt, QThreadPool
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

logging.basicConfig(format="%(message)s", level=logging.INFO)

# 1. Subclass QRunnable
class Runnable(QRunnable):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        """Long-running task."""
        global isRunning
        while isRunning == "1":
        #while True:
            window.label.setText("Idle . . .")
            files = os.listdir(inFolder)
            try:
                file_name = files[0]
            except:
                continue
            try:
                #for file_name in files:
                if file_name:
                    file_path = os.path.join(inFolder, file_name)
                    if os.path.isfile(file_path):
                        os.rename(file_path,file_path)
                        window.label.setText("Copying " + file_name + " Network Volume")
                        collateral_path = os.path.join(collateral_folder, file_name)
                        network_temp_path = os.path.join(network_temp_folder, file_name)
                        new_file_path = os.path.join(ot_folder, file_name) # create the new path with the prefix
                        window.label.setText(f"{file_name} scan complete.")
                        shutil.copy(file_path, collateral_path)
                        window.label.setText(f"{file_name} copying to  Network Volume.")
                        shutil.move(file_path, network_temp_path) # move the file to the new location
                        window.label.setText(f"{file_name} ready for processing.")
                        shutil.move(network_temp_path, new_file_path )
                        #clear()
                        time.sleep(1)
            except:
                window.label.setText("File in use: " + str(file_name))
                time.sleep(2)

class Window(QMainWindow):
    global isRunning
    isRunning = "0"
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        global isRunning
        self.setWindowTitle("Watch Folder")
        self.resize(600, 100)
        self.centralWidget = QWidget()
        self.setCentralWidget(self.centralWidget)
        # Create and connect widgets
        self.label = QLabel("Stopped.")
        self.label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        self.countBtn = QPushButton("Start", self)
        self.countBtn.clicked.connect(self.runTasks)
        # Set the layout
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.countBtn)
        self.centralWidget.setLayout(layout)

    def runTasks(self):
        #threadCount = QThreadPool.globalInstance().maxThreadCount()
        global isRunning
        if isRunning == "0":
            isRunning = "1"
            threadCount = 1
            self.countBtn.setText("Stop")
            self.label.setText(f"Running {threadCount} Threads")
            pool = QThreadPool.globalInstance()
            for i in range(threadCount):
                # 2. Instantiate the subclass of QRunnable
                runnable = Runnable(i)
                # 3. Call start()
                pool.start(runnable)
        else:
            #pool.terminate()
            isRunning = "0"
            self.countBtn.setText("Start")
            window.label.setText("Stopped.")

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec_())
