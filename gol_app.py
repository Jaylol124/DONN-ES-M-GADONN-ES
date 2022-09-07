import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QWidget, QLabel, QScrollBar, QVBoxLayout, QHBoxLayout, QPushButton, QGroupBox
import random

from __feature__ import snake_case, true_property


from gameOfLifeQuimarche import GOLEngine


class GOLApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.__gol_engine = GOLEngine(50, 50)
        
        self.set_window_title('Color picker')
        
        self.__gol_view = QLabel()
        self.__gol_view.alignment = Qt.AlignRight
                
        # self.set_central_widget(self.__gol_view)
        
        self.__timer = QtCore.QTimer()
        self.__timer.timeout.connect(self.__process_simulation)
        self.__timer.start(100)
        
        self.__process_simulation()

        self.__pause_button = QPushButton()
        self.__one_step_button = QPushButton()
        self.__speed_scrollBar = QScrollBar()
        value = QLabel('0')

        small_mixed_layout = QVBoxLayout()
        small_mixed_layout.add_widget(self.__pause_button)
        small_mixed_layout.add_widget(self.__one_step_button)
        small_mixed_layout.add_widget(self.__speed_scrollBar)
        small_mixed_layout.add_widget(value)

        self.__speed_scrollBar.orientation = Qt.Horizontal
        self.__speed_scrollBar.minimum_width = 10
        self.__speed_scrollBar.valueChanged.connect(value.set_num)

        value.alignment = Qt.AlignCenter

        self.__pause_button.text = "start"
        self.__one_step_button.text = "one step button"

        small_mixed_layout.add_stretch()

        small_mixed_gbox = QGroupBox()
        small_mixed_gbox.set_layout(small_mixed_layout)

        mixed_layout = QHBoxLayout()
        mixed_layout.add_widget(small_mixed_gbox)
        mixed_layout.add_widget(self.__gol_view)


        central_widget = QWidget()
        central_widget.set_layout(mixed_layout)

        self.set_central_widget(central_widget)






        
    @Slot()
    def __process_simulation(self):
        self.__gol_engine.process()
        self.__show_gol()

    def __show_gol(self):
        image = QtGui.QImage(self.__gol_engine.width, self.__gol_engine.height, QtGui.QImage.Format_ARGB32)
        #mettre tout noir
        image.fill(QtGui.QColor(Qt.black).rgb())
        
        # dessiner
        for i in range(self.__gol_engine.width):
            for j in range(self.__gol_engine.height):
                if self.__gol_engine._GOLEngine__world[i][j]:
                    image.set_pixel_color(i, j, QtGui.QColor(255,255,255))
        pixmap = QtGui.QPixmap.from_image(image.scaled(self.__gol_view.width, self.__gol_view.height, Qt.KeepAspectRatio, Qt.FastTransformation))
        self.__gol_view.set_pixmap(pixmap)
        
    

def main():
    app = QtWidgets.QApplication(sys.argv)

    w = GOLApp()
    w.show()
    sys.exit(app.exec())
    

if __name__ == '__main__':
    main()