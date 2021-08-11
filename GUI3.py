#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-

from tkinter import *
from selenium import webdriver

win=Tk()
win.title("github Log-in")
win.geometry("400x400")
# win.configure(bg="black")
win.option_add("*Font", "고딕 20")

#Logo
lab_b=Label(win)
img=PhotoImage(file="/Applications/DEV/gui/github.png",master=win)
img=img.subsample(4)
lab_b.config(image=img)
lab_b.pack()

#id Label
lab1=Label(win)
lab1.config(text="ID")
lab1.pack()

#id input
ent1=Entry(win)
ent1.insert(0, "Username or E-mail Address")
def clear(event):
    if ent1.get()=="E-mail Address":
        ent1.delete(0,len(ent1.get()))
ent1.bind("<Button-1>", clear)
ent1.pack()

#password label
lab2=Label(win)
lab2.config(text="Password")
lab2.pack()

#password input
ent2=Entry(win)
ent2.config(show="#")
ent2.pack()

#Log-in Button
btn=Button(win)
btn.config(text="Sign In")
def login():
    
    driver=webdriver.Chrome("/Users/t1ryanlee/downloads/chromedriver")
    url="https://github.com/login"
    driver.get(url)
    driver.implicitly_wait(10)
    xpath1="//input[@name='login']"
    driver.find_element_by_xpath(xpath1).send_keys(ent1.get())
    driver.implicitly_wait(10)
    xpath2="//input[@name='password']"
    driver.find_element_by_xpath(xpath2).send_keys(ent2.get())
    driver.implicitly_wait(10)
    xpath3="//input[@class='btn btn-primary btn-block']"
    driver.find_element_by_xpath(xpath3).click()
    lab3.config(text="You are successfully Logged in")
btn.config(command=login)
btn.pack()

#Notification
lab3=Label(win)


lab3.pack()

win.mainloop()