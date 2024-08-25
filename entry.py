import tkinter as tk

form = tk.Tk()

form.title("Entry")
form.geometry("500x500+350+50")

entry = tk.Entry()
entry.pack()

entry2 = tk.Entry(show="*")
entry2.pack()

def verial():
    etiket["text"] = entry.get()

def verisil():
    entry.delete(0, "end")
    entry2.delete(0, "end")

    





button = tk.Button(form, text="verileri al", fg="red", bg="green", command=verial)
button.pack()


buttonsil = tk.Button(form, text="verileri sil", fg="red", bg="green", command=verisil)
buttonsil.pack()


etiket = tk.Label(form, text="verilerin buraya getirilmesi lazım")
etiket.pack()

form.mainloop()