import subprocess
import os
import pygetwindow as gw
import psutil
from datetime import datetime


def find_chrome_win():
    import winreg as reg  # import registry

    chrome_path = None
    reg_path = r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\chrome.exe"

    for install_type in (reg.HKEY_CURRENT_USER, reg.HKEY_LOCAL_MACHINE):
        try:
            reg_key = reg.OpenKey(install_type, reg_path, 0, reg.KEY_READ)
            chrome_path = reg.QueryValue(reg_key, None)
            reg_key.Close()
            if not os.path.isfile(chrome_path):
                continue
        except WindowsError:
            chrome_path = None
        else:
            break

    for browser in ("google-chrome", "chrome", "chromium", "chromium-browser"):
        a = os.popen("where " + browser).read()
        if a == "":
            pass
        else:
            chrome_path = a[:-1]

    return chrome_path


def oneInstance(title):
    # pw = gw.getWindowsWithTitle(title)
    # if len(pw) > 0:
    #     pasWindow(title)
    #     return True
    # return False
    pid = 0
    ntime = datetime.now()
    ctime = 0
    for process in psutil.process_iter():
        if process.name() == 'chrome.exe':
            print(process.pid, datetime.fromtimestamp(
                process.create_time()))
            if (pid == 0):
                pid = process.pid
                ctime = process.create_time()
            else:
                if (datetime.fromtimestamp(process.create_time()) > datetime.fromtimestamp(ctime)):
                    pid = process.pid
                    ctime = process.create_time()

            # return True
    print(pid, datetime.fromtimestamp(ctime))
    return False


def pasWindow(title):
    pw = gw.getWindowsWithTitle(title)
    for p in pw:
        try:
            p.activate()
            p.maximize()
        except:
            pass


def get_chrome_pid(title):
    pid = 0
    ntime = datetime.now()
    ctime = 0
    for process in psutil.process_iter():
        if process.name() == 'chrome.exe':
            print(process.pid, datetime.fromtimestamp(
                process.create_time()))
            if (pid == 0):
                pid = process.pid
                ctime = process.create_time()
            else:
                if (datetime.fromtimestamp(process.create_time()) > datetime.fromtimestamp(ctime)):
                    pid = process.pid
                    ctime = process.create_time()

            # return True
    print(pid, datetime.fromtimestamp(ctime))


def Pas():
    title = "pas.ntoc.com.vn"
    if not oneInstance(title):
        url = "http://pas.ntoc.com.vn/"
        proc = subprocess.Popen(('"{}" --incognito --app={}').format(find_chrome_win(), url), stdout=subprocess.PIPE, shell=True)
        # time.sleep(10)
        # get_chrome_pid(title)
        # pasWindow(title)


if __name__ == '__main__':
    Pas()
