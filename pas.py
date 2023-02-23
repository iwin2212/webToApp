import ctypes
import os
import sys
from xml.dom import minidom

import pygetwindow as gw
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication


def pasWindow(procs):
    # kiểm tra đã có cửa sổ fids.exe hay chưa
    if len(procs) > 0:
        for p in procs:
            try:
                p.activate()
                p.maximize()
            except:
                pass


def hide_console():
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    SW_HIDE = 0
    hWnd = kernel32.GetConsoleWindow()
    user32.ShowWindow(hWnd, SW_HIDE)


def get_xml_data():
    fn = '{}\configs.xml'.format(os.getcwd())
    items = minidom.parse(fn).getElementsByTagName('item')
    return items[0].attributes['dns'].value


try:
    title = get_xml_data()
    url = "http://{}/".format(title)

    procs = gw.getWindowsWithTitle(title)
    if procs:
        pasWindow(procs)
    else:
        # hiển thị dưới dạng Webview
        app = QApplication(sys.argv)
        view = QWebEngineView()
        view.load(QUrl(url))
        view.setWindowTitle(title)
        view.show()

        procs = gw.getWindowsWithTitle(title)
        pasWindow(procs)

        hide_console()

        sys.exit(app.exec_())
except Exception as ex:
    print(ex)
    os.system("pause")
