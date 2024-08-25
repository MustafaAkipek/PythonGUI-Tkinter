import tkinter as tk

form = tk.Tk()
form.geometry("500x500+350+50")

label = tk.Label(form, text="Geometrik Yöneticiler")
label.pack(side=tk.TOP)

#button = tk.Button(form, text="Pack()", bg="red")
#button.pack(side=tk.BOTTOM, fill=tk.X)

#button = tk.Button(form, text="Pack()", bg="red")
#button.pack(side=tk.LEFT, fill=tk.Y)

#button = tk.Button(form, text="Pack()", bg="red")
#button.pack(side=tk.LEFT, fill=tk.Y, expand = tk.YES) # expand ortalanmasını sağlıyor


# n-yukarı; s-aşağı; e-sağ; w-sol; ne-yukarı sağ; nw-yukarısol; se-aşağı sol; sw-aşağısol; center-orta 

#button = tk.Button(form, text="Pack()", bg="red")
#button.pack(expand = 1, anchor='nw')

button = tk.Button(form, text="Pack()", bg="red")
button.pack(padx=150, pady=50, ipadx=50, ipady=80) # ilk parametre x eksenine göre öteliyor, ikinci parametre y eksenine göre öteliyor
# üçüncü parametre butonun yatay büyüklüğünü, dördüncü parametre dikey yüksekliğini ayarlıyor


form.mainloop()