import ctypes
from selenium import webdriver
import psutil
import pygetwindow as gw


def showWebview():
    options = webdriver.ChromeOptions()
    options.add_argument("--app=http://pas.ntoc.com.vn/")
    options.add_experimental_option("useAutomationExtension", False)
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("detach", True)

    webdriver.Chrome(options=options)


def checkInstance():
    for process in psutil.process_iter():
        if process.name() == 'chrome.exe' and '--test-type=webdriver' in process.cmdline():
            return True
    return False


def pasWindow():
    try:
        p = gw.getWindowsWithTitle('pas.ntoc.com.vn')[0]
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
    if checkInstance():
        pasWindow()
    else:
        showWebview()
        pasWindow()
        hide_console()
except Exception as ex:
    print(ex)
