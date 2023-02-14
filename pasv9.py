import tkinter as tk
from tkinter import ttk
from tkinter import font
from urllib.request import urlopen
from bs4 import BeautifulSoup


def open_website(url):
    content = urlopen(url).read()
    soup = BeautifulSoup(content, "html.parser")
    return soup.prettify()


root = tk.Tk()
root.title("Web Browser")
root.geometry("600x400")
root.config(bg="#F0F0F0")

frame = ttk.Frame(root)
frame.pack(expand=True, fill="both")

text = tk.Text(frame, wrap="word", font=font.Font(family="Arial", size=12))
text.pack(expand=True, fill="both")

open_website("http://pas.ntoc.com.vn/", text)

root.mainloop()
