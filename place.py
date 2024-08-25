import tkinter as tk

form = tk.Tk()
form.title("Place")
form.geometry("500x500+350+50")

button = tk.Button(form, text="Deneme", fg="red", bg="green", font="Times 17 bold")
button.place(width=150, height=95, relx=0.5, rely=0.5) # buton konumu dinamik ayarlandı




form.mainloop()