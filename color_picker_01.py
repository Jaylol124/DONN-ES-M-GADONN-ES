# Introduction à Qt (1/3)
#
# Cet exemple introductif présente comment créer une application de type sélection de couleur avec Qt.
#
# Le schéma suivant présente les widgets utilisé.
#   __________________________________________________________________
#  |__________________________________________________________________|
#  |             ________________________           _____     _____   |
#  |  Rouge     |__________________|_|___|   212   |_____|   |     |  |
#  |             ________________________           _____    |     |  |
#  |  Vert      |_|______________________|    0    |_____|   |     |  |
#  |             ________________________           _____    |     |  |
#  |  Bleu      |_____________|_|________|   188   |_____|   |_____|  |
#  |__________________________________________________________________|
# 
#    \____/     \________________________/  \____/ \_____/   \_____/
#      |                     |                |       |         |
#      |                     |                |       |          \_ QLabel : affiche une image de la couleur finale
#      |                     |                |        \_ QLabel : affiche une image pour chaque bande de couleur (intensité de rouge, vert, bleu)
#      |                     |                 \_ QLabel : affiche un texte pour la valeur de chaque bande de couleur (intensité de rouge, vert, bleu)
#      |                      \_ QScrollBar : sélection de la valeur pour chaque bande de couleur (intensité de rouge, vert, bleu)
#       \_ QLabel : affiche un titre pour chaque bande de couleur
#
#
# Cet exemple est constitué de plusieurs "layout" imbriqués les uns dans les autres. Les "layouts" permettent une gestion automatisée de la disposition à l'écran.
# Le schéma suivant présente quelle est la disposition des 6 "layouts" utilisés.
# 
#   _________________________________________________________________________________________
#  |_________________________________________________________________________________________|
#  |                                                                                         |
#  |   ___________________________________________________________________________________   |
#  |  6                                                                                   |  |
#  |  |   _____________________________________________________________________________   |  |
#  |  |  5                                                                             |  |  |
#  |  |  |   ______________________________________________________________            |  |  |
#  |  |  |  4                                                              |           |  |  |
#  |  |  |  |   ________________________________________________________   |           |  |  |
#  |  |  |  |  1             ________________________           _____   |  |   _____   |  |  |
#  |  |  |  |  |  Rouge     |__________________|_|___|   212   |_____|  |  |  |     |  |  |  |
#  |  |  |  |  |________________________________________________________|  |  |     |  |  |  |
#  |  |  |  |                                                              |  |     |  |  |  |     
#  |  |  |  |   ________________________________________________________   |  |     |  |  |  |     
#  |  |  |  |  2             ________________________           _____   |  |  |     |  |  |  |
#  |  |  |  |  |  Vert      |_|______________________|    0    |_____|  |  |  |     |  |  |  |
#  |  |  |  |  |________________________________________________________|  |  |     |  |  |  |
#  |  |  |  |                                                              |  |     |  |  |  |     
#  |  |  |  |   ________________________________________________________   |  |     |  |  |  |     
#  |  |  |  |  3             ________________________           _____   |  |  |     |  |  |  |
#  |  |  |  |  |  Bleu      |_____________|_|________|   188   |_____|  |  |  |_____|  |  |  |
#  |  |  |  |  |________________________________________________________|  |           |  |  |
#  |  |  |  |                                                              |           |  |  |
#  |  |  |  |______________________________________________________________|           |  |  |
#  |  |  |                                                                             |  |  |
#  |  |  |_____________________________________________________________________________|  |  |
#  |  |                                                                                   |  |
#  |  |___________________________________________________________________________________|  |
#  |                                          /                                              |
#  |                                         /                                               |
#  |                                         \                                               |
#  |                                          \  (stretch)                                   |
#  |                                           \                                             |
#  |                                           /                                             |
#  |__________________________________________/______________________________________________|
#
#  Informations sur les layouts :
#   - (1), (2) et (3) : 
#       - QHBoxLayout
#       - gère la disposition horizontale de 4 widgets : 
#           - le titre
#           - la barre de défilement
#           - la valeur de la couleur
#           - l'image de la couleur
#   - (4) :
#       - QVBoxLayout
#       - gère la disposition verticale des trois "layouts" (1), (2) et (3)
#   - (5) :
#       - QHBoxLayout
#       - gère la disposition horizontale entre le "layout" (4) et l'image de la couleur finale
#   - (6) :
#       - QHBoxLayout
#       - gère la disposition verticale du "layout" (5) et de l'application
#
# L'implémentation suivante est plutôt simple et vise une compréhension de base. Les exemples suivants pourront approfondir quelques aspects supplémentaires.


import sys
from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtCore import Qt, Signal, Slot
from PySide6.QtWidgets import QWidget, QLabel, QScrollBar, QVBoxLayout, QHBoxLayout


class MyApp(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle('Color picker')
        # self.setWindowIcon(QtGui.QIcon('...'))
        
        fixed_widget_length = 75
        
        self.__red_scroll = QScrollBar()
        self.__red_color = QLabel()
        self.__green_scroll = QScrollBar()
        self.__green_color = QLabel()
        self.__blue_scroll = QScrollBar()
        self.__blue_color = QLabel()
        self.__mixed_color = QLabel()
        self.__mixed_color.setFixedWidth(fixed_widget_length)
        
        red_layout = self.__create_channel('Rouge', self.__red_scroll, self.__red_color, fixed_widget_length)
        green_layout = self.__create_channel('Vert', self.__green_scroll, self.__green_color, fixed_widget_length)
        blue_layout = self.__create_channel('Bleu', self.__blue_scroll, self.__blue_color, fixed_widget_length)
        channel_layout = QVBoxLayout()
        channel_layout.addLayout(red_layout)
        channel_layout.addLayout(green_layout)
        channel_layout.addLayout(blue_layout)
        
        mixed_layout = QHBoxLayout()
        mixed_layout.addLayout(channel_layout)
        mixed_layout.addWidget(self.__mixed_color)
        
        central_layout = QVBoxLayout()
        central_layout.addLayout(mixed_layout)
        central_layout.addStretch()
        
        central_widget = QWidget()
        central_widget.setLayout(central_layout)
        
        self.setCentralWidget(central_widget)
        
    def __create_channel(self, text, scroll, color, width):
        title = QLabel(text)
        value = QLabel('0')
        
        title.setFixedWidth(width)
        scroll.setMinimumWidth(2 * width)
        scroll.setOrientation(Qt.Horizontal)
        scroll.setRange(0, 255)
        scroll.setValue(0)
        value.setAlignment(Qt.AlignCenter)
        value.setFixedWidth(width)
        color.setFixedWidth(width)
        
        scroll.valueChanged.connect(value.setNum)
        scroll.valueChanged.connect(self.__update_all_colors)
        
        layout = QHBoxLayout()
        layout.addWidget(title)
        layout.addWidget(scroll)
        layout.addWidget(value)
        layout.addWidget(color)      
        
        return layout
    
    @Slot()
    def __update_all_colors(self):
        r = self.__red_scroll.value()
        g = self.__green_scroll.value()
        b = self.__blue_scroll.value()
        self.__update_color(self.__red_color, QtGui.QColor(r, 0, 0))
        self.__update_color(self.__green_color, QtGui.QColor(0, g, 0))
        self.__update_color(self.__blue_color, QtGui.QColor(0, 0, b))
        self.__update_color(self.__mixed_color, QtGui.QColor(r, g, b))
    
    
    def __update_color(self, label, color):
        pixmap = QtGui.QPixmap(label.size())
        pixmap.fill(color)
        label.setPixmap(pixmap)
        


def main():
    app = QtWidgets.QApplication(sys.argv)

    w = MyApp()
    w.show()
    sys.exit(app.exec())
    

if __name__ == '__main__':
    main()



