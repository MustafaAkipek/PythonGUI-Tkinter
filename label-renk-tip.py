import tkinter as tk

form = tk.Tk()
form.title("Tkinter")

label = tk.Label(form, text="Label 1")
label.pack() 

label2 = tk.Label(form, text="Label 2", fg="red") # fg ile yazının rengini belirledik
label2.pack()

label3 = tk.Label(form, text="Label 3", fg="black", bg="green") # bg ile arka plan rengini belirledik
label3.pack()

label4 = tk.Label(form, text="Label 4", fg="red", bg="green", font="Times 15 italic") # bg ile arka plan rengini belirledik
label4.pack()

form.mainloop()     