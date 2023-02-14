from tendo import singleton
import pyautogui
import webview
import pygetwindow as gw
import ctypes
import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QApplication


pw = gw.getWindowsWithTitle('pas')


def pasWindow():
    # kiểm tra đã có cửa sổ pas.exe hay chưa
    if len(pw) > 0:
        for p in pw:
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


# độ phân giải màn hình
width, height = pyautogui.size()


# chỉ cho phép chạy 1 phiên bản (only 1 instance)
pasWindow()
me = singleton.SingleInstance()


# ẩn tiến trình với tên pas.exe
# try:
#     frgrnd_wndw = win32gui.GetForegroundWindow()
#     wndw_title = win32gui.GetWindowText(frgrnd_wndw)
#     if wndw_title.endswith("pas.exe"):
#         win32gui.ShowWindow(frgrnd_wndw, win32con.SW_HIDE)
# except:
#     pass


hide_console()

# hiển thị dưới dạng Webview
app = QApplication(sys.argv)
view = QWebEngineView()
view.load(QUrl("http://pas.ntoc.com.vn/"))
view.show()
sys.exit(app.exec_())
