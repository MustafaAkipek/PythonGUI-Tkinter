import tkinter as tk
import random as rd

form = tk.Tk()
form.title("Tekrar Uygulaması")
form.geometry("500x500+350+50")


mylist = []

def randomnumber():   
    global mylist
    while len(mylist) != 6:
        a = rd.randint(1, 50)
        if a not in mylist:
            mylist.append(a)

    return mylist






def show():
    global mylist
    randomnumber()
    label.config(text=mylist, bg="green") # label' ın özelliklerini al demek

def transparency():
    form.wm_attributes("-alpha", 0.3)

def turn():
    form.wm_attributes("-alpha", 0.9)

def minwin():
    form.state("iconic")

def maxwin():
    form.state("zoomed")


label = tk.Label(form, fg="red", bg="red", font="Times 20 bold")
label.pack()

show = tk.Button(form, text="Show", fg="black", bg="yellow", command=show)
show.pack(side=tk.LEFT)

transparency = tk.Button(form, text="transparency", fg="black", bg="yellow", command=transparency)
transparency.pack(side=tk.LEFT)

turn = tk.Button(form, text="turn", fg="black", bg="yellow", command=turn)
turn.pack(side=tk.LEFT)

minwin = tk.Button(form, text="minwin", fg="black", bg="yellow", command=minwin)
minwin.pack(side=tk.LEFT)

maxwin = tk.Button(form, text="maxwin", fg="black", bg="yellow", command=maxwin)
maxwin.pack(side=tk.LEFT)

form.mainloop()