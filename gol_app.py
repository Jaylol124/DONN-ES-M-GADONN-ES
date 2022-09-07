import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QWidget, QLabel, QScrollBar, QVBoxLayout, QHBoxLayout
import random

from __feature__ import snake_case, true_property


from gol_engine import GOLEngine


class GOLApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.__gol_engine = GOLEngine(50, 40)
        
        self.set_window_title('Color picker')
        
        self.__gol_view = QLabel()
        self.__gol_view.alignment = Qt.AlignCenter
                
        self.set_central_widget(self.__gol_view)
        
        self.__timer = QtCore.QTimer()
        self.__timer.timeout.connect(self.__process_simulation)
        self.__timer.start(100)
        
        self.__process_simulation()
        
    @Slot()
    def __process_simulation(self):
        self.__gol_engine.process()
        self.__show_gol()

    def __show_gol(self):
        image = QtGui.QImage(self.__gol_engine.width, self.__gol_engine.height, QtGui.QImage.Format_ARGB32)
        # dessiner
        for i in range(20):
            image.set_pixel_color(i, i, QtGui.QColor(random.randint(0,255),0,0))
        pixmap = QtGui.QPixmap.from_image(image.scaled(self.__gol_view.width, self.__gol_view.height, Qt.KeepAspectRatio, Qt.FastTransformation))
        self.__gol_view.set_pixmap(pixmap)
        
    

def main():
    app = QtWidgets.QApplication(sys.argv)

    w = GOLApp()
    w.show()
    sys.exit(app.exec())
    

if __name__ == '__main__':
    main()