from tendo import singleton
import pyautogui
import webview
import win32gui
import win32con
import pygetwindow as gw


pw = gw.getWindowsWithTitle('pas')
print(len(pw))


def pasWindow():
    # kiểm tra đã có cửa sổ pas.exe hay chưa
    if len(pw) > 0:
        for p in pw:
            try:
                p.maximize()
            except:
                pass


# độ phân giải màn hình
width, height = pyautogui.size()


# chỉ cho phép chạy 1 phiên bản (only 1 instance)
pasWindow()
me = singleton.SingleInstance()


# ẩn tiến trình với tên pas.exe
try:
    frgrnd_wndw = win32gui.GetForegroundWindow()
    wndw_title = win32gui.GetWindowText(frgrnd_wndw)
    if wndw_title.endswith("pas.exe"):
        win32gui.ShowWindow(frgrnd_wndw, win32con.SW_HIDE)
except:
    pass


# hiển thị dưới dạng Webview
window = webview.create_window(
    "PAS", "http://pas.ntoc.com.vn/", height=height, width=width, confirm_close=True)
webview.start()
