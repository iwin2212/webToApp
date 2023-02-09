import pyautogui
import webview
import win32gui
import win32con
import time
# chỉ cho phép chạy 1 phiên bản (only 1 instance)
from tendo import singleton
me = singleton.SingleInstance()


# ẩn tiến trình với tên pas.exe
try:
    frgrnd_wndw = win32gui.GetForegroundWindow()
    wndw_title = win32gui.GetWindowText(frgrnd_wndw)
    if wndw_title.endswith("pas.exe"):
        win32gui.ShowWindow(frgrnd_wndw, win32con.SW_HIDE)
except:
    pass


def change_title(window):
    """changes title every 3 seconds"""
    for i in range(1, 100):
        time.sleep(3)
        window.set_title('Hệ thống phát thanh PAS AI')


# độ phân giải màn hình
width, height = pyautogui.size()

# hiển thị dưới dạng Webview
window = webview.create_window(
    "PAS", "http://pas.ntoc.com.vn/", height=height, width=width)
webview.start(change_title, window)
