import tkinter as tk

form = tk.Tk()
form.title("Tkinter")
form.geometry("500x500+350+50")

def topla():
    pass

button = tk.Button(form, text="click", fg="black", bg="green", command="topla") # command ile tuşa basıldığına yapılması istenilen görev gerçekleştiriliyor
button.pack(side=tk.LEFT)

button2 = tk.Button(form, text="click2", command="topla")
button2.pack(side=tk.RIGHT)

form.mainloop()