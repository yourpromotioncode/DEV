#!/Library/Frameworks/Python.framework/Versions/3.9/bin/python3
# -*- coding: utf-8 -*-


from tkinter import *

win=Tk()
win.geometry("600x600")
win.title("pack")
win.option_add("*Font","굴림 20")


#Pack


# ent = Entry(win)
# ent.insert(0, "Pack location")
# def clear(event):
# if ent.get()=="Pack location":
    # ent.delete(0,len(ent.get()))
# ent.bind("<Button-1>", clear)
# ent.pack(side="top", pady=10)
# 
# ent2= Entry(win)
# ent2.insert(0, "Pad X Value")
# def clear2(event):
# if ent2.get()=="Pad X Value":
    # ent2.delete(0,len(ent2.get()))
# ent2.bind("<Button-2>", clear2)
# ent2.pack(side='top', pady=5)
# 
# ent3=Entry(win)
# ent3.insert(0, "Pad Y Value")
# def clear3(event):
# if ent3.get()=="Pad Y Value":
    # ent3.delete(0,len(ent3.get()))
# ent3.bind("<Button-3>", clear3)
# ent3.pack(side='top',pady=5)

# btn=Button(win)
# btn.config(text="확인")
# buttons=["top",'bottom','left','right']
# for a in buttons:
# def movement():
        # if ent.get() == buttons:
    # btn.pack(side=ent.get(), padx=ent2.get(), pady=ent3.get())
# btn.config(command=movement)
# btn.pack()

# btn1=Button(win)
# btn1.config(text="(0,0)")
# btn1.grid(calumn=0, row=0)
# 
# btn2=Button(win)
# btn2.config(text="(0,1)")
# btn2.grid(column=0,row=1)
# 
# btn3=button(win)
# btn3.config(text="(1,0)")
# btn3.grid(column=1,row=0)



#GRid

# 
# btn_list=[]
# 
# col_num=4
# 
# row_num=3

# for j in range(0,row_num):

    # for i in range(0,col_num):

        # btn=Button(win)

        # btn.config(text="({},{})".format(i,j))

        # btn.grid(column=i,row=j, padx = 10, pady = 10)
  
        # btn_list.append(btn)
# 

# 
# btn=Button(win)
# 
# btn.config(text="span")
# 
# btn.grid(column = 3, row=0, rowspan =2)
# 

# 
# btn1=Button(win)
# 
# btn.config(text="span2")
# btn.grid(column=0, row=2, columnspan=3)





#Place

X_Value = 0.5
Y_Value = 0.5

btn=Button(win)
btn.config(text="({},{})".format(X_Value,Y_Value))
btn.place(relx=X_Value,rely=Y_Value)

win.mainloop()