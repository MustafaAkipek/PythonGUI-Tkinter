import tkinter as tk

form = tk.Tk()
form.geometry("500x500+350+50")
form.title("Tkinter")

form.state("normal")
#form.state("zoomed") # tam ekran yapar
#form.state("iconic") # araç çubuğu kısmında açılır

form.wm_attributes("-alpha", 0.8) # saydamlığı ayarlar

form.mainloop()