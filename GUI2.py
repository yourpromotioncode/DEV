#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *

win=Tk()
win.geometry("300x200")
win.configure(bg='black')
win.option_add("*Font", "굴림 20")

ent=Entry(win)
ent.pack()

def p(a):
    print(a)

def lotto_p():    
    import requests
    from bs4 import BeautifulSoup
    n=ent.get()
    url = "https://dhlottery.co.kr/gameResult.do?method=byWin&drwNo={}".format(n)
    #div class="win_result"
    req=requests.get(url)
    soup=BeautifulSoup(req.text, "html.parser")
    txt=soup.find("div", attrs={"class","win_result"}).get_text()
    lot_result=txt.split("\n")[7:13]
    bonus=txt.split("\n")[-4]    
    p("당첨번호")    
    p(lot_result)    
    p("보너스번호")    
    p(bonus)    
    
def p(a):    
    print(a)

btn=Button(win)
btn.config(text="Lottery result check")
btn.config(command=lotto_p)
btn.pack()


win.mainloop()
