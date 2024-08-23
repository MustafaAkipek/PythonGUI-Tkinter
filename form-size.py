import tkinter as tk

form = tk.Tk()
form.title("Tkinter")
form.geometry("500x500+500+150") # pencere boyutunu ayarlamak için, + kısımları ise pencerenin başlangıç konumunu kaydırmak için

# form.minsize(450,400) # pencerenin min boyutunu ayarlamak için
# form.maxsize(750,750) # pencerenin max boyutunu ayarlamak için
form.resizable(False,False) # x veya y ekseninde oynama yapmamamızı sağlıyor

label = tk.Label(form, text="Tkinter")
label.pack()



form.mainloop()