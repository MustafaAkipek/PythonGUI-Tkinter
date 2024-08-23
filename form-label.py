import tkinter as tk # kütüphaneyi çağırdı

form = tk.Tk() 
form.title("Tkinter Penceresi") # Pencereye isim verildi

etiket = tk.Label(form, text="Tkinter")  # Etiket koyuldu
etiket.pack()  # Etiketin ekranda kalmasını sağlıyor

form.mainloop() # Pencerenin ekranda durmasını sağlıyor

