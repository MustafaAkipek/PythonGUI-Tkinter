import tkinter as tk

form = tk.Tk()

form.title("Entry")
form.geometry("500x500+350+50")

entry = tk.Entry(form, fg="black", bg="green")
entry.pack()

entry2 = tk.Entry(form, fg="red", bg="blue")
entry2.pack(side=tk.LEFT)

  

form.mainloop()