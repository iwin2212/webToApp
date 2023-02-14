from tendo import singleton
import pyautogui
import pygetwindow as gw
import ctypes
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication


def pasWindow(procs):
    # kiểm tra đã có cửa sổ pas.exe hay chưa
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


try:
    title = "pas.ntoc.com.vn"
    url = "http://pas.ntoc.com.vn/"
    # độ phân giải màn hình
    width, height = pyautogui.size()
    procs = gw.getWindowsWithTitle(title)

    # chỉ cho phép chạy 1 phiên bản (only 1 instance)
    pasWindow(procs)
    me = singleton.SingleInstance()

    hide_console()

    # hiển thị dưới dạng Webview
    app = QApplication(sys.argv)
    view = QWebEngineView()
    view.load(QUrl(url))
    view.setWindowTitle(title)
    view.show()
    procs = gw.getWindowsWithTitle(title)
    pasWindow(procs)
    sys.exit(app.exec_())
except Exception as ex:
    print(ex)
