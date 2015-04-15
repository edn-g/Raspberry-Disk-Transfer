#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'edn-g <edn.g@free.fr>'

import argparse

from PyQt4.QtCore import *
from PyQt4.QtGui import *


class USBTransfer(QApplication):
    """Application window"""

    def __init__(self, width, height, touchscreen=False, translation_file=None):
        QApplication.__init__(self, [])

        # Load translation file
        if translation_file is not None:
            self.__trans = QTranslator()
            self.installTranslator(self.__trans)
            self.__trans.load(translation_file)

        # Main window
        self._main_window = QMainWindow()
        self._main_window.resize(width, height)
        self._main_window.setWindowTitle('USBDiskReader')
        self._main_window.setWindowIcon(QIcon('icon.png'))

        if touchscreen:
            self._main_window.setCursor(Qt.BlankCursor)

        # Main widget
        main_widget = QWidget(self._main_window)
        self._main_window.setCentralWidget(main_widget)

        # Elements layout
        main_layout = QHBoxLayout(self._main_window.centralWidget())

    # Run and display application
    def run(self):
        self._main_window.show()
        self.exec_()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='USB Transfer tool for RaspberryPI.')
    parser.add_argument('width', type=int, help='interface width in pixel')
    parser.add_argument('height', type=int, help='interface height in pixel')
    parser.add_argument('-t', '--touchscreen', help='touchscreen environment', action='store_true', default=False)
    args = parser.parse_args()

    app = USBTransfer(args.width, args.height, touchscreen=args.touchscreen)
    app.run()
