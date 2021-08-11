#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from datetime import datetime


win = Tk() #창 생성
win.geometry("500x500")
win.configure(bg='beige') 
win.title("새로운시작")
win.option_add("*Font","맑은고딕 18")

def time_():
    ptime=datetime.now().replace(microsecond=0)
    dtime = ptime.strftime("%d/%m/%Y  %H:%M:%S")
    btn.config(text=dtime)


btn = Button(win, text="현재시각") #버튼 생성
# btn.config(text="현재시각")
btn.config(width=20, height=2)
btn.config(command=time_)

btn.pack() #버튼 배치


win.mainloop() #창 실행





